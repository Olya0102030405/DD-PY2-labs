# TODO Написать 3 класса с документацией и аннотацией типов

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
from abc import ABC, abstractmethod


from abc import ABC, abstractmethod

class Table(ABC):  # Абстрактный класс для стола
    def __init__(self, material: str, height: float, width: float):
        if height <= 0 or width <= 0:
            raise ValueError("Размеры стола должны быть положительными числами.")
        self.material = material  # Материал (например, дерево, стекло)
        self.height = height  # Высота стола
        self.width = width  # Ширина стола


    def fold(self):
        """Сложить стол"""
        ...


    def move(self, new_location: str):
        """Переместить стол в другое место"""
        ...


class Tree(ABC):  # Абстрактный класс для дерева
    def __init__(self, species: str, age: int, height: float):
        if age < 0:
            raise ValueError("Возраст дерева не может быть отрицательным.")
        if height <= 0:
            raise ValueError("Высота дерева должна быть положительным числом.")
        self.species = species  # Вид дерева (например, дуб, сосна)
        self.age = age  # Возраст в годах
        self.height = height  # Высота дерева


    def grow(self):
        """Дерево растет"""
        ...


    def photosynthesize(self):
        """Процесс фотосинтеза"""
        ...


class Facebook(ABC):  # Абстрактный класс для социальной сети
    def __init__(self, users_count: int, daily_active_users: int):
        if users_count < 0 or daily_active_users < 0:
            raise ValueError("Количество пользователей не может быть отрицательным.")
        if daily_active_users > users_count:
            raise ValueError("Число активных пользователей не может превышать общее количество.")
        self.users_count = users_count  # Общее количество пользователей
        self.daily_active_users = daily_active_users  # Число активных пользователей в день


    def post_content(self, content_type: str):
        """Размещение контента (текст, фото, видео)"""
        ...


    def analyze_trends(self):
        """Анализ трендов в социальной сети"""
        ...
