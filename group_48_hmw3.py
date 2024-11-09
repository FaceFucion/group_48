class Computer:
    def __init__(self, cpu: float, memory: int):
        self.__cpu = cpu
        self.__memory = memory

    # Геттеры и сеттеры для атрибутов cpu и memory
    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    # Метод для выполнения вычислений
    def make_computations(self):
        return self.__cpu * self.__memory

    # Переопределение магического метода __str__
    def __str__(self):
        return f"Computer(cpu={self.__cpu}, memory={self.__memory})"

    # Переопределение методов сравнения по атрибуту memory
    def __eq__(self, other):
        return self.memory == other.memory

    def __ne__(self, other):
        return self.memory != other.memory

    def __lt__(self, other):
        return self.memory < other.memory

    def __le__(self, other):
        return self.memory <= other.memory

    def __gt__(self, other):
        return self.memory > other.memory

    def __ge__(self, other):
        return self.memory >= other.memory


class Phone:
    def __init__(self, sim_cards_list: list):
        self.__sim_cards_list = sim_cards_list

    # Геттер и сеттер для атрибута sim_cards_list
    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    # Метод для симуляции звонка
    def call(self, sim_card_number: int, call_to_number: str):
        if 1 <= sim_card_number <= len(self.__sim_cards_list):
            sim_card = self.__sim_cards_list[sim_card_number - 1]
            print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - {sim_card}")
        else:
            print("Неверный номер сим-карты.")

    # Переопределение магического метода __str__
    def __str__(self):
        return f"Phone(sim_cards_list={self.__sim_cards_list})"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu: float, memory: int, sim_cards_list: list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    # Метод для симуляции использования GPS
    def use_gps(self, location: str):
        print(f"Построение маршрута до локации: {location}")

    # Переопределение магического метода __str__
    def __str__(self):
        return f"SmartPhone(cpu={self.cpu}, memory={self.memory}, sim_cards_list={self.sim_cards_list})"


# Создание объектов
computer = Computer(3.5, 16)
phone = Phone(["Beeline", "O!"])
smartphone1 = SmartPhone(2.8, 8, ["Beeline", "MegaCom"])
smartphone2 = SmartPhone(3.2, 12, ["O!", "MegaCom"])

# Вывод информации об объектах
print(computer)
print(phone)
print(smartphone1)
print(smartphone2)

# Тестирование методов
print("Вычисления на компьютере:", computer.make_computations())
phone.call(1, "+996 777 99 88 11")
smartphone1.use_gps("Ош Базар")
smartphone2.call(2, "+996 555 55 55 55")
print("Вычисления на смартфоне 1:", smartphone1.make_computations())

# Тестирование магических методов сравнения
print("Сравнение памяти компьютер и смартфон1:", computer > smartphone1)
print("Сравнение памяти смартфон1 и смартфон2:", smartphone1 < smartphone2)
print("Сравнение памяти компьютер и смартфон2:", computer == smartphone2)