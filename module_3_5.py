#def get_multiplied_digits(number):
    #str_1 = ( 0, 1, 2, 3, 4)
    #str_number = str_1
    #first = int(1)
    #if str_number == 0:
        #return 0
    #elif str_number > 1:

    #else:
       # str_number < 1
        #return first

# return first *get_multiplied_digits(int(str_number[1:]))

def get_multiplied_digits(number):  # str_1 = (0, 1, 3, 4,)
    str_1 = (0, 1, 2, 3, 4)
    str_number = str_1
    if str_1 == 0:
        return 0
    else:
        return str_1 + (number - 1)


stack = []
stack.append(1)
print("Добавили элемент", stack)
stack.append(2)
print("Добавили элемент", stack)
stack.append(3)
print("Добавили элемент", stack)
stack.append(4)
print("Добавили элемент", stack)
print(stack)
stack.pop()
print("Убрали элемент", stack)
stack.pop()
print("Убрали элемент", stack)
stack.pop()
print("Убрали элемент", stack)
stack.pop()
print("Убрали элемент", stack)































