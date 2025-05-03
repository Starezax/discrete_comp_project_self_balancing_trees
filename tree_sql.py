import argparse
import shlex
from data_manager import DataManager

class TreeSQL:
    def __init__(self):
        """Ініціалізація класу TreeSQL"""
        # Створити екземпляр менеджера даних
        self.data_manager = DataManager()
    
    def parse_command(self, command):
        """Розбір та виконання SQL-подібної команди
        
        :param command: SQL-подібна команда для виконання
        :return: Результат виконання команди
        """
        # TODO: Розділити команду на токени
        # TODO: Привести всі токени до нижнього регістру, окрім рядків у лапках
        # TODO: Розібрати команду за першим токеном (create, use, insert, select, update, delete)
        pass
    
    def create_table_command(self, tokens):
        """Розбір та виконання команди CREATE TABLE
        
        :param tokens: Список токенів команди, без "CREATE TABLE"
        :return: Результат виконання команди
        """
        # TODO: Отримати назву таблиці
        # TODO: Встановити тип дерева за замовчуванням (avl)
        # TODO: Перевірити наявність USING та витягнути тип дерева
        # TODO: Розібрати визначення стовпців
        # TODO: Повернути результат виклику create_table з data_manager
        pass
    
    def insert_command(self, tokens):
        """Розбір та виконання команди INSERT
        
        :param tokens: Список токенів команди
        :return: Результат виконання команди
        """
        # TODO: Перевірити правильність формату команди
        # TODO: Отримати назву таблиці
        # TODO: Розібрати значення
        # TODO: Обробити значення (числа, рядки)
        # TODO: Повернути результат виклику insert з data_manager
        pass
    
    def select_command(self, tokens):
        """Розбір та виконання команди SELECT
        
        :param tokens: Список токенів команди
        :return: Відформатований результат запиту
        """
        # TODO: Отримати назву таблиці
        # TODO: Розібрати умови, якщо є
        # TODO: Викликати select з data_manager
        # TODO: Відформатувати результат у вигляді таблиці
        pass
    
    def update_command(self, tokens):
        """Розбір та виконання команди UPDATE
        
        :param tokens: Список токенів команди
        :return: Результат виконання команди
        """
        # TODO: Перевірити правильність формату команди
        # TODO: Отримати назву таблиці
        # TODO: Знайти WHERE, якщо є
        # TODO: Розібрати частину SET (оновлення)
        # TODO: Розібрати умову WHERE, якщо є
        # TODO: Повернути результат виклику update з data_manager
        pass
    
    def delete_command(self, tokens):
        """Розбір та виконання команди DELETE
        
        :param tokens: Список токенів команди
        :return: Результат виконання команди
        """
        # TODO: Перевірити правильність формату команди
        # TODO: Отримати назву таблиці
        # TODO: Розібрати умову WHERE, якщо є
        # TODO: Повернути результат виклику delete з data_manager
        pass


def main():
    """Головна функція для обробки аргументів командного рядка"""
    # TODO: Створити аргументи командного рядка
    # TODO: Розібрати аргументи
    # TODO: Створити екземпляр TreeSQL
    # TODO: Виконати команду або запустити інтерактивний режим
    pass

if __name__ == "__main__":
    main()