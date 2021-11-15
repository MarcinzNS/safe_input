import re

NORMAL = "\033[0;37;40m"
ERROR = "\033[1;31;40m"

def safe_input(prompt, ret_type):
    while True:
        try:
            value = input(prompt)
            value = ret_type(value)
            return value
        except:
            type = str(ret_type)[8:-2]
            print(f"{ERROR}The program expects data of the type {type}.{NORMAL}")

def regex_safe_input(prompt, pattern):
    while True:
        try:
            value = safe_input(prompt, str)
            regex = re.findall(pattern, value)
            value = regex[0]
            return value
        except:
            print(f"{ERROR}The program expects data in the format {pattern}.{NORMAL}")

def range_safe_input(prompt, ret_type, a, b):
    while True:
        value = safe_input(prompt, ret_type)
        if a <= value <= b:
            return value
        else:
            print(f"{ERROR}The program expects data in the range from {a} to {b}.{NORMAL}")

def bool_safe_input(prompt):
    while True:
        value = safe_input(prompt, str)
        if value in ["True", "true", "1", "Yes", "yes"]:
            return True
        elif value in ["False", "false", "0", "Yes", "yes"]:
            return False
        else:
            print(f"{ERROR}The program expects logical data [True/False].{NORMAL}")

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
        if ", " in value:
            value = value.split(", ")
            lista = []
            for i in value:
                lista.append( __element_find_type(i) )
        else:
            lista[ __element_find_type(i) ]

if __name__ == '__main__':
    regex_safe_input("Enter your date of birth: ", str, "\d\d-\d\d-\d\d\d\d")
    range_safe_input("Enter age: ", int, 3, 99)
    range_safe_input("Enter the side of the square: ", float, 0, 99)
    bool_safe_input("Enter a logical value: ")
    list_safe_input("Enter a list: ")
