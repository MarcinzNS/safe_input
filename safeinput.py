import re

__NORMAL = "\033[0;37;40m"
__ERROR = "\033[1;31;40m"

def safe_input(prompt, ret_type):
    while True:
        try:
            value = input(prompt)
            value = ret_type(value)
            return value
        except:
            type = str(ret_type)[8:-2]
            print(f"{__ERROR}The program expects data of the type {type}.{__NORMAL}")

def regex_safe_input(prompt, pattern):
    while True:
        try:
            value = safe_input(prompt, str)
            regex = re.findall(pattern, value)
            if value == regex[0]:
                return value
            else:
                raise TypeError # Jump to 'except' section
        except:
            print(f"{__ERROR}The program expects data in the format {pattern}.{__NORMAL}")

def range_safe_input(prompt, ret_type, a, b):
    while True:
        value = safe_input(prompt, ret_type)
        if a <= value <= b or b <= value <= a:
            return value
        else:
            print(f"{__ERROR}The program expects data in the range from {a} to {b}.{__NORMAL}")

def bool_safe_input(prompt):
    while True:
        value = safe_input(prompt, str)
        if value.lower() in ["true", "1", "yes", "y"]:
            return True
        elif value.lower() in ["false", "0", "no", "n"]:
            return False
        else:
            print(f"{__ERROR}The program expects logical data [True/False].{__NORMAL}")

def __element_find_type(element):
    for single_type in [int, float, str]:
        try:
            element = single_type(element)
            if type == str:
                if element == "True":
                    element = True
                elif element == "False":
                    element = False
                else:
                    element = element[1:-1]
            return element
        except:
            continue

def list_safe_input(prompt):
    while True:
        value = safe_input(prompt, str)
        if value[0] == "[" and value[-1] == "]":
            value = value[1:-1]
            lista = []
            if "," in value:
                for i in value.split(","):
                    lista.append( __element_find_type(i) )
            else:
                lista[ __element_find_type(value)]
            return lista
        else:
            print(f"{__ERROR}The program expects data of the type list.{__NORMAL}")

if __name__ == '__main__':
    output = [
        regex_safe_input("Enter your date of birth: ", "\d\d-\d\d-\d\d\d\d"),
        range_safe_input("Enter age: ", int, 3, 99),
        range_safe_input("Enter the side of the square: ", float, 0, 99),
        bool_safe_input("Enter a logical value: "),
        # This function can only take as an input one dimention list.
        list_safe_input("Enter a list: ")
    ]
    for o in output:
        print(o)

