class Figure:
    unit = "cm"  # единица измерения

    def __init__(self):
        pass

    def calculate_area(self):
        raise NotImplementedError("Метод calculate_area должен быть переопределен в подклассе")

    def info(self):
        raise NotImplementedError("Метод info должен быть переопределен в подклассе")


class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length  # приватный атрибут длины стороны

    def calculate_area(self):
        return self.__side_length ** 2  # площадь квадрата

    def info(self):
        area = self.calculate_area()
        print(f"Square side length: {self.__side_length}{self.unit}, area: {area}{self.unit}^2")


class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.__length = length  # приватный атрибут длины
        self.__width = width    # приватный атрибут ширины

    def calculate_area(self):
        return self.__length * self.__width  # площадь прямоугольника

    def info(self):
        area = self.calculate_area()
        print(f"Rectangle length: {self.__length}{self.unit}, width: {self.__width}{self.unit}, area: {area}{self.unit}^2")


# Создаем список с 2 квадратами и 3 прямоугольниками
figures = [
    Square(5),
    Square(7),
    Rectangle(5, 8),
    Rectangle(10, 6),
    Rectangle(7, 3)
]

# Вызываем метод info для каждого объекта
for figure in figures:
    figure.info()