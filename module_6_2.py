class Vehicle:
    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def get_model(self, __model):
        print("Модель: ", self.__model)
        
    def get_horsepower(self, __engine_power):
        print("Мощность двигателя: ",self.__engine_power)

    def get_color(self, __color):
        print("Цвет: ", self.__color)

    def print_info(self):
        self.get_model(self)
        self.get_horsepower(self)
        self.get_color(self)
        print("Владелец: ", self.owner)

    def set_color(self, new_color):
        self.new_color = new_color
        if self.new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = self.new_color
        else:
            print("Нельзя сменить цвет на ", self.new_color)



class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
    pass


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
#
# # Проверяем что поменялось
vehicle1.print_info()