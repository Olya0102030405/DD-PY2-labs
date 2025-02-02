if __name__ == "__main__":
    # Write your solution here
    pass


class Vehicle:
    """
    Базовый класс для всех транспортных средств.

    Attributes:
        make (str): Производитель транспортного средства.
        model (str): Модель транспортного средства.
        year (int): Год выпуска транспортного средства.
    """

    def __init__(self, make: str, model: str, year: int) -> None:
        """
        Инициализация транспортного средства.

        Args:
            make (str): Производитель транспортного средства.
            model (str): Модель транспортного средства.
            year (int): Год выпуска транспортного средства.
        """
        self.make = make
        self.model = model
        self.year = year

    def __str__(self) -> str:
        """Возвращает строковое представление транспортного средства."""
        return f"{self.year} {self.make} {self.model}"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление транспортного средства."""
        return f"Vehicle(make='{self.make}', model='{self.model}', year={self.year})"


class Car(Vehicle):
    """
    Класс для легковых автомобилей, наследующий от Vehicle.

    Attributes:
        doors (int): Количество дверей в легковом автомобиле.
    """

    def __init__(self, make: str, model: str, year: int, doors: int) -> None:
        """
        Инициализация легкового автомобиля.

        Args:
            make (str): Производитель легкового автомобиля.
            model (str): Модель легкового автомобиля.
            year (int): Год выпуска легкового автомобиля.
            doors (int): Количество дверей в легковом автомобиле.
        """
        super().__init__(make, model, year)  # Вызов конструктора базового класса
        self.doors = doors

    def __str__(self) -> str:
        """Возвращает строковое представление легкового автомобиля."""
        return super().__str__() + f" with {self.doors} doors"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление легкового автомобиля."""
        return f"Car(make='{self.make}', model='{self.model}', year={self.year}, doors={self.doors})"

    def honk(self) -> str:
        """
        Издает звук сигнала легкового автомобиля.

        Returns:
            str: Звук сигнала легкового автомобиля.
        """
        return "Beep! Beep!"


class Truck(Vehicle):
    """
    Класс для грузовых автомобилей, наследующий от Vehicle.

    Attributes:
        capacity (float): Грузоподъемность грузового автомобиля в тоннах.
    """

    def __init__(self, make: str, model: str, year: int, capacity: float) -> None:
        """
        Инициализация грузового автомобиля.

        Args:
            make (str): Производитель грузового автомобиля.
            model (str): Модель грузового автомобиля.
            year (int): Год выпуска грузового автомобиля.
            capacity (float): Грузоподъемность грузового автомобиля в тоннах.
        """
        super().__init__(make, model, year)  # Вызов конструктора базового класса
        self.__capacity = capacity  # Инкапсуляция атрибута

    def __str__(self) -> str:
        """Возвращает строковое представление грузового автомобиля."""
        return super().__str__() + f" with a capacity of {self.__capacity} tons"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление грузового автомобиля."""
        return f"Truck(make='{self.make}', model='{self.model}', year={self.year}, capacity={self.__capacity})"

    def load(self, weight: float) -> str:
        """
        Загружает груз в грузовой автомобиль.

        Args:
            weight (float): Вес груза в тоннах.

        Returns:
            str: Сообщение о загрузке.

        Raises:
            ValueError: Если вес груза превышает грузоподъемность.
        """
        if weight > self.__capacity:
            raise ValueError("Weight exceeds the truck's capacity.")
        return f"Loaded {weight} tons into the truck."


# Примеры использования классов
if __name__ == "__main__":
    my_car = Car("Toyota", "Corolla", 2020, 4)
    print(my_car)  # Вывод: 2020 Toyota
