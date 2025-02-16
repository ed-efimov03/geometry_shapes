# Геометрическая библиотека

## Описание

Данная библиотека предоставляет классы для работы с основными геометрическими примитивами:
окружностями, прямоугольниками и треугольниками. Реализованы методы для вычисления площади, периметра,
проверки принадлежности точки, а также пересечения фигур.

## Установка

Для использования данной библиотеки достаточно скопировать исходный код в ваш проект и импортировать необходимые классы.

## Классы и методы

### 1. `Circle` (Окружность)

#### Конструктор
```python
Circle(center_x: float, center_y: float, radius: float)
```
- `center_x` (float): Координата X центра окружности.
- `center_y` (float): Координата Y центра окружности.
- `radius` (float): Радиус окружности.

#### Методы

- `area() -> float` - Возвращает площадь окружности.
- `circumference() -> float` - Возвращает длину окружности.
- `contains_point(x: float, y: float) -> bool` - Проверяет, содержится ли точка внутри окружности.
- `intersects(other: Circle) -> bool` - Проверяет, пересекается ли окружность с другой окружностью.

---

### 2. `Rectangle` (Прямоугольник)

#### Конструктор
```python
Rectangle(x: float, y: float, width: float, height: float)
```
- `x` (float): Координата X левого верхнего угла.
- `y` (float): Координата Y левого верхнего угла.
- `width` (float): Ширина прямоугольника.
- `height` (float): Высота прямоугольника.

#### Методы

- `area() -> float` - Возвращает площадь прямоугольника.
- `perimeter() -> float` - Возвращает периметр прямоугольника.
- `contains_point(x: float, y: float) -> bool` - Проверяет, содержится ли точка внутри прямоугольника.
- `intersects(other: Rectangle) -> bool` - Проверяет, пересекается ли прямоугольник с другим прямоугольником.
- `contains_rectangle(other: Rectangle) -> bool` - Проверяет, содержится ли прямоугольник внутри другого прямоугольника.

---

### 3. `Triangle` (Треугольник)

#### Конструктор
```python
Triangle(a: tuple, b: tuple, c: tuple)
```
- `a` (tuple): Координаты первой вершины.
- `b` (tuple): Координаты второй вершины.
- `c` (tuple): Координаты третьей вершины.

#### Методы

- `area() -> float` - Возвращает площадь треугольника.
- `perimeter() -> float` - Возвращает периметр треугольника.
- `is_valid() -> bool` - Проверяет, является ли треугольник допустимым.
- `contains_point(p: tuple) -> bool` - Проверяет, находится ли точка внутри треугольника.
- `intersects(other: Triangle) -> bool` - Проверяет, пересекается ли треугольник с другим треугольником.

## Примеры использования

#### **Примитивы:**
```python
from geometry import Circle, Rectangle, Triangle

# Создание кругов
circle1 = Circle(center_x=4, center_y=4, radius=5)
circle2 = Circle(center_x=6, center_y=6, radius=3)

# Проверка пересечения кругов
print("Круги пересекаются:", circle1.intersects(circle2))  # Ожидаемый результат: True

# Создание прямоугольников
rect1 = Rectangle(x=0, y=0, width=10, height=5)
rect2 = Rectangle(x=5, y=2, width=3, height=2)

# Проверка вложенности прямоугольников
print("rect2 находится внутри rect1:", rect1.contains_rectangle(rect2))  # Ожидаемый результат: True

# Проверка пересечения прямоугольников
print("Прямоугольники пересекаются:", rect1.intersects(rect2))  # Ожидаемый результат: True

# Создание треугольника
triangle = Triangle(a=(0, 0), b=(4, 0), c=(2, 3))

# Проверка валидности треугольника
print("Треугольник валиден:", triangle.is_valid())  # Ожидаемый результат: True

# Проверка принадлежности точки треугольнику
print("Точка (1, 1) принадлежит треугольнику:", triangle.contains_point((1, 1)))  # Ожидаемый результат: True
```

#### **Сценарии:**
```python
from geometry_logic import check_placement, simulate_field, fill_area_with_rectangles
from geometry import Circle, Rectangle

# Сценарий 1: Проверка размещения фигур
shapes = [
    Circle(center_x=3, center_y=3, radius=5),
    Rectangle(x=0, y=0, width=4, height=3)
]

# Анализ взаимного расположения фигур
analysis = check_placement(shapes)
print("Анализ расположения фигур:", analysis)
# Ожидаемый результат: список групп фигур, которые пересекаются или находятся одна внутри другой.

# Сценарий 2: Симуляция поля
shapes = [
    Circle(center_x=14, center_y=14, radius=5),
    Rectangle(x=20, y=20, width=10, height=5)
]

# Проверка, какие фигуры выходят за границы поля
out_of_bounds = simulate_field(shapes, area_width=50, area_height=50)
print("Фигуры за границами поля:", out_of_bounds)
# Ожидаемый результат: информация о фигурах, которые выходят за границы поля.

# Сценарий 3: Заполнение области прямоугольниками
rectangles = fill_area_with_rectangles(area_width=20, area_height=10, rect_width=3, rect_height=2)
print("Размещенные прямоугольники:", rectangles)
# Ожидаемый результат: количество и координаты размещенных прямоугольников.
```
