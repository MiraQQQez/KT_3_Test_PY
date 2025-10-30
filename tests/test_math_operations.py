import pytest
from src.math_operations import MathOperations


class TestIsEven:
    """
    Класс для тестирования функции is_even.
    Использует параметризацию для проверки различных чисел.
    """

    @pytest.mark.parametrize("number,expected", [
        # Четные числа
        (0, True),
        (2, True),
        (4, True),
        (10, True),
        (100, True),
        (1000, True),
        # Отрицательные четные
        (-2, True),
        (-4, True),
        (-100, True),
        # Нечетные числа
        (1, False),
        (3, False),
        (5, False),
        (99, False),
        (1001, False),
        # Отрицательные нечетные
        (-1, False),
        (-3, False),
        (-99, False),
    ])
    def test_is_even_parametrized(self, number, expected):
        """
        Параметризованный тест для проверки четности числа.
        Проверяет положительные, отрицательные, четные и нечетные числа.
        """
        result = MathOperations.is_even(number)
        assert result == expected, f"Для числа {number} ожидался {expected}, получено {result}"

    def test_is_even_zero(self):
        """Отдельный тест для нуля - ноль считается четным."""
        assert MathOperations.is_even(0) is True

    def test_is_even_returns_bool(self):
        """Проверяет, что функция возвращает булево значение."""
        result = MathOperations.is_even(5)
        assert isinstance(result, bool), f"Ожидался тип bool, получен {type(result)}"


class TestCalculateArea:
    """
    Класс для тестирования функции calculate_area.
    Использует параметризацию с несколькими параметрами.
    """

    @pytest.mark.parametrize("length,width,expected_area", [
        # Целые числа
        (1, 1, 1),
        (2, 3, 6),
        (5, 4, 20),
        (10, 10, 100),
        (7, 8, 56),
        # Дробные числа
        (2.5, 4, 10.0),
        (3.5, 2.5, 8.75),
        (10.5, 5.2, 54.6),
        (0.5, 0.5, 0.25),
        # Большие числа
        (100, 200, 20000),
        (1000, 1000, 1000000),
        # Маленькие числа
        (0.1, 0.1, 0.01),
        (0.01, 0.01, 0.0001),
    ])
    def test_calculate_area_parametrized(self, length, width, expected_area):
        """
        Параметризованный тест для вычисления площади прямоугольника.
        Проверяет различные комбинации длины и ширины.
        """
        result = MathOperations.calculate_area(length, width)
        assert result == pytest.approx(expected_area, rel=1e-9), \
            f"Для length={length}, width={width} ожидалась площадь {expected_area}, получено {result}"

    @pytest.mark.parametrize("length,width", [
        (0, 5),      # Нулевая длина
        (5, 0),      # Нулевая ширина
        (-1, 5),     # Отрицательная длина
        (5, -1),     # Отрицательная ширина
        (-10, -10),  # Обе отрицательные
        (0, 0),      # Обе нулевые
    ])
    def test_calculate_area_invalid_values(self, length, width):
        """
        Параметризованный тест для проверки некорректных значений.
        Должно вызываться исключение ValueError.
        """
        with pytest.raises(ValueError):
            MathOperations.calculate_area(length, width)

    def test_calculate_area_returns_float(self):
        """Проверяет, что функция возвращает числовое значение."""
        result = MathOperations.calculate_area(5, 3)
        assert isinstance(result, (int, float)), f"Ожидался числовой тип, получен {type(result)}"

    def test_calculate_area_square(self):
        """Отдельный тест для квадрата (длина = ширина)."""
        result = MathOperations.calculate_area(5, 5)
        assert result == 25, f"Площадь квадрата 5x5 должна быть 25, получено {result}"