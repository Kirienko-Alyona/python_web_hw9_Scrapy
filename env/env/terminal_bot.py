from termcolor import colored

from decor import input_error
from search import search_name, search_tag, return_quote

FUNCTIONS = {
    "name": search_name,
    "tags": search_tag,
    "tag": search_tag
}


@input_error
def handler(input_string: str) -> list:

    command = ""
    data = ""
    input_string = input_string.strip()
    for key in FUNCTIONS:
        if input_string.startswith(key):
            command = key
            data = input_string[len(command):].strip().split(":")
            data = data[1].strip().split(",")
            break
    if data[0] != (''):
        return FUNCTIONS[command](data)
    else:
        raise ValueError


def terminal_input():
    while True:
        input_string = input(colored("\nInput words, please: ", "blue"))

        if input_string.lower() == "exit":
            print(colored("Good bye :)", "blue"))
            exit()
            
        list_quote = handler(input_string)
        
        if len(list_quote) == 0:
            raise IndexError
        elif not (isinstance(list_quote, str)): #if list_quote is str
            for quote in list_quote:
                quote = return_quote(quote)
                print(colored(quote, "magenta")) 
        else:       
            print(list_quote)

if __name__ == '__main__':
    terminal_input()
