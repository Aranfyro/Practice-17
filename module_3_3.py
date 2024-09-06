# Самостоятельная работа по уроку "Распаковка позиционных параметров".
# Задача "Распаковка":

# 1.Функция с параметрами по умолчанию:
def print_params (a = 1, b = 'строка', c = True):
    print (a, b, c)

print_params(b = 25)
print_params(c = [1,2,3])

# 2.Распаковка параметров:
values_list = ['string', False, 1.5]
values_dict = {'a' : 888, 'b' : 22, 'c' : 123}
print_params(*values_list)
print_params(**values_dict)

# 3.Распаковка + отдельные параметры:
values_list_2 = [2.4, 'двачетыре']
print_params(*values_list_2, 42)