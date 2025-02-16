import math

class Circle:
    """Класс, представляющий окружность."""

    def __init__(self, center_x: float, center_y: float, radius: float):
        """
        Инициализирует объект окружности.

        Args:
            center_x (float): Координата X центра окружности.
            center_y (float): Координата Y центра окружности.
            radius (float): Радиус окружности.
        """
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def area(self) -> float:
        """
        Возвращает площадь окружности.
        
        Returns:
            float: Площадь окружности.
        """
        return math.pi * self.radius * self.radius
    
    def circumference(self) -> float:
        """
        Возвращает длину окружности.
        
        Returns:
            float: Площадь окружности.
        """
        return 2 * math.pi * self.radius
    
    def contains_point(self, x: float, y: float) -> bool:
        """
        Проверяет, содержится ли точка внутри окружности.
        
        Args:
            x (float): Координата X точки.
            y (float): Координата Y точки.
        
        Returns:
            bool: True, если точка внутри окружности, иначе False.
        """
        return (x - self.center_x)**2 + (y - self.center_y)**2  <= self.radius**2
        
    def intersects(self, other: "Circle") -> bool:
        """
        Проверяет, пересекается ли окружность с другой окружностью.
        
        Args:
            other (Circle): Другая окружность.
        
        Returns:
            bool: True, если окружности пересекаются, иначе False.
        """
        if isinstance(other, Circle):
            d2 = (self.center_x - other.center_x)**2 + (self.center_y - other.center_y)**2
            return d2 <= (self.radius + other.radius)**2

class Rectangle:
    """Класс, представляющий прямоугольник."""

    def __init__(self, x: float, y: float, width: float, height: float):
        """
        Инициализирует объект прямоугольника.

        Args:
            x (float): Координата X левого верхнего угла.
            y (float): Координата Y левого верхнего угла.
            width (float): Ширина прямоугольника.
            height (float): Высота прямоугольника.
        """
        if width <= 0 or height <= 0:
            raise ValueError("Такой прямоугольник невозможен, потому что стороны должны быть больше 0")
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.x1, self.y1 = (x, y)
        self.x2, self.y2 = (x + width, y)
        self.x3, self.y3 = (x + width, y + height) 
        self.x4, self.y4 = (x, y + height)

    def area(self) -> float:
        """
        Возвращает площадь прямоугольника.
        
        Returns:
            float: Площадь прямоугольника.
        """
        return self.width * self.height
    
    def perimeter(self) -> float:
        """
        Возвращает периметр прямоугольника.
        
        Returns:
            float: Периметр прямоугольника.
        """
        return 2 * (self.width + self.height)
    
    def contains_point(self, x: float, y: float) -> bool:
        """
        Проверяет, содержится ли точка внутри прямоугольника.
        
        Args:
            x (float): Координата X точки.
            y (float): Координата Y точки.
        
        Returns:
            bool: True, если точка внутри прямоугольника, иначе False.
        """
        cond1 = (self.x1 <= x) and (self.y1 <= y)
        cond2 = (self.x2 >= x) and (self.y2 <= y)
        cond3 = (self.x3 >= x) and (self.y3 >= y)
        cond4 = (self.x4 <= x) and (self.y4 >= y)
        return cond1 and cond2 and cond3 and cond4
    
    def intersects(self, other: "Rectangle") -> bool:
        """
        Проверяет, пересекается ли прямоугольник с другим прямоугольником.
        
        Args:
            other (Rectangle): Другой прямоугольник.
        
        Returns:
            bool: True, если прямоугольники пересекаются, иначе False.
        """
        left1 = self.x1
        right1 = self.x2
        top1 = self.y1
        bottom1 = self.y4

        left2 = other.x1
        right2 = other.x2
        top2 = other.y1
        bottom2 = other.y4

        x_intersect = not (right1 < left2 or right2 < left1)

        y_intersect = not (bottom1 < top2 or bottom2 < top1)

        return x_intersect and y_intersect
        
    def contains_rectangle(self, other) -> bool:
        """
        Проверяет, содержится ли прямоугольник внутри прямоугольника.
        
        Args:
            other (Rectangle): Другой прямоугольник.
        
        Returns:
            bool: True, если прямоугольник внутри прямоугольника, иначе False.
        """
        if isinstance(other, Rectangle):
            cond1 = (self.x1 <= other.x1) and (self.y1 <= other.y1)
            cond2 = (self.x2 >= other.x2) and (self.y2 <= other.y2)
            cond3 = (self.x3 >= other.x3) and (self.y3 >= other.y3)
            cond4 = (self.x4 <= other.x4) and (self.y4 >= other.y4)
            return cond1 and cond2 and cond3 and cond4

class Triangle:
    """Класс, представляющий треугольник."""
    
    def __init__(self, a: tuple, b: tuple, c: tuple):
        """
        Инициализирует объект треугольника.
        
        Args:
            a (tuple): Координаты первой вершины.
            b (tuple): Координаты второй вершины.
            c (tuple): Координаты третьей вершины.
        """
        self.ab = math.sqrt((a[0]-b[0])**2 + ((a[1]-b[1])**2))
        self.bc = math.sqrt((b[0]-c[0])**2 + ((b[1]-c[1])**2))
        self.ca = math.sqrt((c[0]-a[0])**2 + ((c[1]-a[1])**2))
        self.edges = [(a, b), (b, c), (c, a)]
        if not (self.ab + self.bc > self.ca and self.bc + self.ca > self.ab and self.ca + self.ab > self.bc):
            raise ValueError("Такой треугольник невозможен, потому что не собюдается правило существования треугольника")
        self.a = a
        self.b = c
        self.c = c

    def area(self) -> float:
        """
        Возвращает площадь треугольника.
        
        Returns:
            float: Площадь треугольника.
        """
        half_perimetr = Triangle.perimeter(self) / 2
        return math.sqrt(half_perimetr*(half_perimetr-self.ab)*(half_perimetr-self.bc)*(half_perimetr-self.ca))
    
    def perimeter(self) -> float:
        """
        Возвращает периметр треугольника.
        
        Returns:
            float: Периметр треугольника.
        """
        return self.ab + self.bc + self.cs

    def is_valid(self) -> bool:
        """Проверяет, является ли треугольник допустимым."""
        return self.ab + self.bc > self.ca and self.bc + self.ca > self.ab and self.ca + self.ab > self.bc 
    
    def contains_point(self, p: tuple) -> bool:
        """
        Проверяет, находится ли точка внутри треугольника.
        
        Args:
            p (tuple): Координаты точки.
        
        Returns:
            bool: True, если точка внутри треугольника, иначе False.
        """
        c1 = (self.a[0] - p[0]) * (self.b[1] - self.a[1]) - (self.b[0] - self.a[0]) * (self.a[1] - p[1])
        c2 = (self.b[0] - p[0]) * (self.c[1] - self.b[1]) - (self.c[0] - self.b[0]) * (self.b[1] - p[1])
        c3 = (self.c[0] - p[0]) * (self.a[1] - self.c[1]) - (self.a[0] - self.c[0]) * (self.c[1] - p[1])
        return (c1 > 0 and c2 > 0 and c3 > 0) or (c1 < 0 and c2 < 0 and c3 < 0) or (c1 == 0 or c2 == 0 or c3 == 0)

    @staticmethod
    def _ccw(A, B, C):
        """
        Вспомогательная функция для определения ориентации трех точек.
        Возвращает:
        - положительное число, если точки A, B, C расположены против часовой стрелки,
        - отрицательное, если по часовой стрелке,
        - 0, если точки коллинеарны.
        """
        return (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0])

    @staticmethod
    def _intersect_segments(A, B, C, D):
        """
        Проверяет, пересекаются ли два отрезка AB и CD.
        """
        ccw1 = Triangle._ccw(A, B, C)
        ccw2 = Triangle._ccw(A, B, D)
        ccw3 = Triangle._ccw(C, D, A)
        ccw4 = Triangle._ccw(C, D, B)

        if ((ccw1 * ccw2 < 0) and (ccw3 * ccw4 < 0)):
            return True

        if ccw1 == 0 and Triangle._is_point_on_segment(A, B, C):
            return True
        if ccw2 == 0 and Triangle._is_point_on_segment(A, B, D):
            return True
        if ccw3 == 0 and Triangle._is_point_on_segment(C, D, A):
            return True
        if ccw4 == 0 and Triangle._is_point_on_segment(C, D, B):
            return True

        return False

    @staticmethod
    def _is_point_on_segment(A, B, P):
        cross = (P[0] - A[0]) * (B[1] - A[1]) - (P[1] - A[1]) * (B[0] - A[0])
        if abs(cross) > 1e-12: 
            return False
        dot = (P[0] - A[0]) * (B[0] - A[0]) + (P[1] - A[1]) * (B[1] - A[1])
        if dot < 0:
            return False
        squared_length = (B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2
        if dot > squared_length:
            return False
        return True

    def intersects(self, other: "Triangle") -> bool:
        """
        Проверяет, пересекается ли треугольник с другим прямоугольником.
        
        Args:
            other (Triangle): Другой треугольник.
        
        Returns:
            bool: True, если треугольники пересекаются, иначе False.
        """
        for edge1 in self.edges:
            for edge2 in other.edges:
                if self._intersect_segments(edge1[0], edge1[1], edge2[0], edge2[1]):
                    return True
        return False


