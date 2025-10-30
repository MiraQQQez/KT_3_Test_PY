class MathOperations:
    """
    Класс для математических операций.
    Предоставляет методы для работы с числами и геометрическими вычислениями.
    """

    @staticmethod
    def is_even(number: int) -> bool:
        """
        Проверяет, является ли число четным.
        
        Args:
            number (int): Число для проверки
            
        Returns:
            bool: True если число четное, False если нечетное
            
        Examples:
            >>> MathOperations.is_even(4)
            True
            >>> MathOperations.is_even(5)
            False
        """
        return number % 2 == 0

    @staticmethod
    def calculate_area(length: float, width: float) -> float:
        """
        Вычисляет площадь прямоугольника.
        
        Args:
            length (float): Длина прямоугольника
            width (float): Ширина прямоугольника
            
        Returns:
            float: Площадь прямоугольника
            
        Raises:
            ValueError: Если длина или ширина отрицательные или равны нулю
            
        Examples:
            >>> MathOperations.calculate_area(5, 3)
            15.0
            >>> MathOperations.calculate_area(10, 2.5)
            25.0
        """
        if length <= 0:
            raise ValueError("Длина должна быть положительным числом")
        if width <= 0:
            raise ValueError("Ширина должна быть положительным числом")
        
        return length * width