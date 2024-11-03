import inspect

class Car:
    def __init__(self, model, vin, numbers):
        if self.__is_valid_vin(vin) and self.__is_valid_numbers(numbers):
            self.model = model
            self.__vin = vin
            self.__numbers = numbers

    def __is_valid_vin(self, vin_number):
        return True

    def __is_valid_numbers(self, numbers):
        return True

def introspection_info(obj):
    info = {}
    info['type'] = type(obj)
    info['attributes'] = []
    info['methods'] = []
    for element in dir(obj):
        _atr = getattr(obj, element)
        if callable(_atr):
            info['methods'].append(element)
        else:
            info['attributes'].append(element)
    info['module'] = inspect.getmodule(obj)
    return info


some_car = Car('Model1', 1000000, 'f123dj')

number_info = introspection_info(some_car)
print(number_info)

