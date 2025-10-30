# KT_3_Test_PY - Параметризованное тестирование с pytest

Проект для демонстрации параметризованного тестирования Python кода с использованием pytest.

## 📋 Описание

Проект содержит реализацию и тестирование трех функций:
1. **is_even** - проверка четности числа
2. **calculate_area** - вычисление площади прямоугольника
3. **classify_triangle** - классификация треугольников по типу

Все тесты используют параметризацию pytest для проверки множества различных входных данных.

## 🚀 Установка

### Клонирование репозитория
```bash
git clone <your-repo-url>
cd KT_3_Test_PY
```

### Создание виртуального окружения
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

### Установка зависимостей
```bash
pip install -r requirements.txt
```

## 🧪 Запуск тестов

```bash
# Запуск всех тестов
pytest

# Запуск с подробным выводом
pytest -v

# Запуск конкретного файла тестов
pytest tests/test_math_operations.py -v
pytest tests/test_geometry.py -v

# Запуск с отчетом о покрытии кода
pytest --cov=src --cov-report=html

# Запуск конкретного теста
pytest tests/test_math_operations.py::TestIsEven::test_is_even_parametrized -v
```

## 📁 Структура проекта

```
KT_3_Test_PY/
├── src/
│   ├── __init__.py
│   ├── math_operations.py    # Математические операции
│   └── geometry.py           # Геометрические операции
├── tests/
│   ├── __init__.py
│   ├── test_math_operations.py  # Тесты для math_operations
│   └── test_geometry.py         # Тесты для geometry
├── requirements.txt
└── README.md
```

## ✨ Функциональность

### 1. MathOperations.is_even(number)

Проверяет, является ли число четным.

**Параметры:**
- `number` (int) - число для проверки

**Возвращает:**
- `bool` - True если четное, False если нечетное

**Примеры:**
```python
from src.math_operations import MathOperations

MathOperations.is_even(4)   # True
MathOperations.is_even(5)   # False
MathOperations.is_even(0)   # True
MathOperations.is_even(-2)  # True
```

**Тесты:** 19 параметризованных тестов
- Четные числа: 0, 2, 4, 10, 100, 1000
- Нечетные числа: 1, 3, 5, 99, 1001
- Отрицательные четные: -2, -4, -100
- Отрицательные нечетные: -1, -3, -99

---

### 2. MathOperations.calculate_area(length, width)

Вычисляет площадь прямоугольника.

**Параметры:**
- `length` (float) - длина прямоугольника
- `width` (float) - ширина прямоугольника

**Возвращает:**
- `float` - площадь прямоугольника

**Исключения:**
- `ValueError` - если длина или ширина <= 0

**Примеры:**
```python
from src.math_operations import MathOperations

MathOperations.calculate_area(5, 3)      # 15.0
MathOperations.calculate_area(10, 2.5)   # 25.0
MathOperations.calculate_area(0, 5)      # ValueError
```

**Тесты:** 20 параметризованных тестов
- Корректные значения:
  - Целые числа: 1×1, 2×3, 5×4, 10×10, 7×8
  - Дробные числа: 2.5×4, 3.5×2.5, 10.5×5.2, 0.5×0.5
  - Большие числа: 100×200, 1000×1000
  - Маленькие числа: 0.1×0.1, 0.01×0.01
- Некорректные значения:
  - Нулевые: (0,5), (5,0), (0,0)
  - Отрицательные: (-1,5), (5,-1), (-10,-10)

---

### 3. Geometry.classify_triangle(a, b, c)

Классифицирует треугольник по длинам его сторон.

**Параметры:**
- `a` (float) - длина первой стороны
- `b` (float) - длина второй стороны
- `c` (float) - длина третьей стороны

**Возвращает:**
- `str` - тип треугольника:
  - "равносторонний" - все стороны равны
  - "равнобедренный" - две стороны равны
  - "разносторонний" - все стороны разные
  - "не треугольник" - стороны не образуют треугольник

**Исключения:**
- `ValueError` - если любая сторона <= 0

**Примеры:**
```python
from src.geometry import Geometry

Geometry.classify_triangle(5, 5, 5)    # "равносторонний"
Geometry.classify_triangle(5, 5, 3)    # "равнобедренный"
Geometry.classify_triangle(3, 4, 5)    # "разносторонний"
Geometry.classify_triangle(1, 2, 10)   # "не треугольник"
```

**Тесты:** 31 параметризованный тест
- Равносторонние: (1,1,1), (5,5,5), (10,10,10), (3.5,3.5,3.5)
- Равнобедренные: (5,5,3), (5,5,8), (3,5,5), (5,3,5)
- Разносторонние: (3,4,5), (5,12,13), (7,8,9), (2,3,4)
- Не треугольники: (1,2,5), (1,1,3), (10,1,1)
- Прямоугольные: (3,4,5), (5,12,13), (8,15,17)
- Некорректные значения: нули и отрицательные числа

## 📊 Статистика тестов

| Класс | Методов | Тестов | Параметризованных |
|-------|---------|--------|-------------------|
| TestIsEven | 3 | 21 | 19 |
| TestCalculateArea | 4 | 22 | 20 |
| TestClassifyTriangle | 6 | 39 | 31 |
| **Всего** | **13** | **82** | **70** |

## 🔧 Технологии

- **Python 3.13+**
- **pytest 7.4.3** - фреймворк для тестирования
- **pytest-cov 4.1.0** - плагин для измерения покрытия кода

## 📝 Особенности реализации

### Параметризация тестов

Используется декоратор `@pytest.mark.parametrize` для запуска одного теста с множеством различных входных данных:

```python
@pytest.mark.parametrize("number,expected", [
    (0, True),
    (2, True),
    (1, False),
    (3, False),
])
def test_is_even_parametrized(self, number, expected):
    result = MathOperations.is_even(number)
    assert result == expected
```

### ООП структура

Все функции организованы в классы с использованием статических методов:
- `MathOperations` - математические операции
- `Geometry` - геометрические операции

### Обработка ошибок

Все функции валидируют входные данные и выбрасывают `ValueError` при некорректных значениях.

## 👨‍💻 Автор

Игорь

## 📝 Лицензия

MIT