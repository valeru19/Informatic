# test_my_lib.py
import pytest
import my_lib


# Тесты для функции чисел Фибоначчи
class TestFibonacci:

    def test_fibonacci_correct(self):
        assert my_lib.fibonacci(5) == [0, 1, 1, 2, 3]

    def test_fibonacci_zero(self):
        with pytest.raises(ValueError):
            my_lib.fibonacci(0)

    def test_fibonacci_negative(self):
        with pytest.raises(ValueError):
            my_lib.fibonacci(-5)


# Тесты для функции сортировки пузырьком
class TestBubbleSort:

    def test_bubble_sort_correct(self):
        assert my_lib.bubble_sort([3, 2, 1]) == [1, 2, 3]

    def test_bubble_sort_empty(self):
        assert my_lib.bubble_sort([]) == []

    def test_bubble_sort_already_sorted(self):
        assert my_lib.bubble_sort([1, 2, 3]) == [1, 2, 3]


# Тесты для функции калькулятора
class TestCalculator:

    def test_addition(self):
        assert my_lib.calculator(3, 2, '+') == 5

    def test_subtraction(self):
        assert my_lib.calculator(5, 3, '-') == 2

    def test_multiplication(self):
        assert my_lib.calculator(4, 2, '*') == 8

    def test_division(self):
        assert my_lib.calculator(6, 3, '/') == 2

    def test_division_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            my_lib.calculator(4, 0, '/')

    def test_invalid_operation(self):
        with pytest.raises(ValueError):
            my_lib.calculator(4, 2, '%')