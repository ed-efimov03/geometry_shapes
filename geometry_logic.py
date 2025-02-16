from geometry import Rectangle, Circle, Triangle

def check_placement(shapes: list):
    pass

def simulate_field(shapes: list, area_width: int, area_height: int) -> dict:
    """
    Симулирует размещение фигур на поле и определяет, какие из них выходят за границы.

    Args:
        shapes (list): Список фигур (Rectangle, Circle, Triangle).
        area_width (int): Ширина поля.
        area_height (int): Высота поля.

    Returns:
        dict: Словарь с количеством фигур внутри поля и списком выходящих за границы фигур.
    """
    inside_count = 0
    outside_figures = []

    for shape in shapes:
        if isinstance(shape, Rectangle):
            # Проверяем прямоугольник
            if (0 <= shape.x and 0 <= shape.y and 
                shape.x + shape.width <= area_width and 
                shape.y + shape.height <= area_height):
                inside_count += 1
            else:
                reason = ""
                if shape.x < 0:
                    reason = "выходит за левую границу"
                elif shape.x + shape.width > area_width:
                    reason = "выходит за правую границу"
                elif shape.y < 0:
                    reason = "выходит за верхнюю границу"
                elif shape.y + shape.height > area_height:
                    reason = "выходит за нижнюю границу"
                outside_figures.append({"figure": shape, "reason": reason})

        elif isinstance(shape, Circle):
            # Проверяем круг
            if (shape.center_x - shape.radius >= 0 and 
                shape.center_x + shape.radius <= area_width and
                shape.center_y - shape.radius >= 0 and 
                shape.center_y + shape.radius <= area_height):
                inside_count += 1
            else:
                reason = ""
                if shape.center_x - shape.radius < 0:
                    reason = "выходит за левую границу"
                elif shape.center_x + shape.radius > area_width:
                    reason = "выходит за правую границу"
                elif shape.center_y - shape.radius < 0:
                    reason = "выходит за верхнюю границу"
                elif shape.center_y + shape.radius > area_height:
                    reason = "выходит за нижнюю границу"
                outside_figures.append({"figure": shape, "reason": reason})

        elif isinstance(shape, Triangle):
            # Проверяем треугольник
            vertices = [shape.a, shape.b, shape.c]
            outside = False
            for vertex in vertices:
                x, y = vertex
                if x < 0 or x > area_width or y < 0 or y > area_height:
                    outside = True
                    break
            if outside:
                reason = "выходит за границы"
                outside_figures.append({"figure": shape, "reason": reason})
            else:
                inside_count += 1

    return {
        "inside_count": inside_count,
        "outside_figures": outside_figures
    }

class Area:
    """
    Класс, представляющий игровое поле с возможностью размещения прямоугольников.
    """
    def __init__(self, width: int, height: int):
        """
        Инициализирует объект игрового поля.

        Args:
            width (int): Ширина поля.
            height (int): Высота поля.
        """
        self.width = width
        self.height = height
        self.rectangles = []

    def can_place(self, rect: Rectangle):
        """
        Проверяет, можно ли разместить прямоугольник на поле без пересечений.

        Args:
            rect (Rectangle): Прямоугольник для размещения.

        Returns:
            bool: True, если размещение возможно, иначе False.
        """
        if rect.x + rect.width > self.width or rect.y + rect.height > self.height:
            return False
        for existing_rect in self.rectangles:
            if not (rect.x + rect.width <= existing_rect.x or rect.x >= existing_rect.x + existing_rect.width or
                    rect.y + rect.height <= existing_rect.y or rect.y >= existing_rect.y + existing_rect.height):
                return False
        return True

    def place_rectangle(self, rect: Rectangle) -> bool:
        """
        Размещает прямоугольник на поле, если это возможно.

        Args:
            rect (Rectangle): Прямоугольник для размещения.

        Returns:
            bool: True, если размещение успешно, иначе False.
        """
        if self.can_place(rect):
            self.rectangles.append(rect)
            return True
        return False

def fill_area_with_rectangles(area_width: int, area_height: int, rect_width: int, rect_height: int) -> dict:
    """
    Заполняет игровое поле прямоугольниками заданного размера.

    Args:
        area_width (int): Ширина игрового поля.
        area_height (int): Высота игрового поля.
        rect_width (int): Ширина прямоугольника.
        rect_height (int): Высота прямоугольника.

    Returns:
        dict: Словарь с количеством размещенных прямоугольников и их координатами.
    """
    area = Area(area_width, area_height)
    x = 0
    y = 0
    placed_count = 0
    rectangles = []
    
    while y + rect_height <= area_height:
        while x + rect_width <= area_width:
            rect = Rectangle(x, y, rect_width, rect_height)
            if area.place_rectangle(rect):
                rectangles.append({"x": rect.x, "y": rect.y})
                placed_count += 1
            x += rect_width
        x = 0
        y += rect_height

    return {
        "placed_count": placed_count,
        "rectangles": rectangles
    }