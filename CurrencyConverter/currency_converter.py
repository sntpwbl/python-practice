from dotenv import load_dotenv
import os

load_dotenv()

def print_and_save_operation_history(operation):
    print(operation)
    history = open('./values.txt', 'a')
    history.write(f'{operation}\n')
    history.close()

def clear_history():
    history = open('./values.txt', 'w')
    history.write('')

def show_options():
    option = int(input(f"{os.environ.get('OPTION')} "))
    return option

def get_values_and_convert():
    currencies = ['EUR', 'USD', 'JPY']
    while True:
        try:
            print(f'{'-'*5} BRL CONVERTER [TYPE CTRL + C TO EXIT ANY TIME!] {'-'*5}')
            value = float(input(f'{os.environ.get('GET_VALUE')} '))

            currency = str(input(f'{os.environ.get('GET_NEW')} ')).upper()

            if currency not in currencies:
                print('Invalid currency value. Try again.')
            else:
                symbol = '$' if currency=='USD' else '¥' if currency=='JPY' else '€'

                conversion_tax = 0.15947581 if currency=='EUR' else 0.16604882 if currency=='USD' else 25.870705

                print_and_save_operation_history(f'R${value:.2f} -> {symbol}{value*conversion_tax:.2f}')

                option = show_options()
                if option == 2:
                    clear_history()
                    print('History successfully cleared. Running the converter once again.')
                elif option == 3: break

        except ValueError:
            print(f'{os.environ.get('VALUE_ERROR')} ')
        except:
            print('Something went wrong. Stopping application.')
            break
    
get_values_and_convert()