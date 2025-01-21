from dotenv import load_dotenv
import os

load_dotenv()

def get_values_and_convert():
    try:
        value = float(input(os.environ.get('GET_VALUE') + ' '))
        old_currency = str(input(os.environ.get('GET_OLD') + ' ')).upper()
        old_symbol = '$' if old_currency=='USD' else 'R$' if old_currency=='BRL' else '€'
        currency = str(input(os.environ.get('GET_NEW') + ' ')).upper()
        if(old_currency==currency):
            raise ValueError
        symbol = '$' if currency=='USD' else 'R$' if currency=='BRL' else '€'
        conversion_tax = float(input(os.environ.get('GET_TAX') + ' '))
        return {'origin': value, 'value': value*conversion_tax, 'old_currency': old_currency, 'old_symbol': old_symbol, 'currency': currency, 'symbol': symbol, 'tax': conversion_tax}
    except ValueError:
        print('You cannot use the same currency two times.')
    
def save_operation_history(value_to_append):
    history = open('./values.txt', 'a')
    history.write(value_to_append)
    history.close()

def show_options():
    option = int(input(os.environ.get('OPTION') + ' '))
    return option

while True:
    try:
        conversion_result = get_values_and_convert()
        format_value = f'VALUE {conversion_result['old_symbol']}{conversion_result['origin']}\nFROM {conversion_result['old_currency']}\nTO {conversion_result['currency']}\nUSING TAX {conversion_result['old_symbol']}{conversion_result['tax']}\nEQUALS {conversion_result['symbol']}{conversion_result['value']}.'
        save_operation_history(format_value)
        print(format_value)

        options = show_options()
        if(options==2):
            print('Bye')
            break
    except ValueError:
        print(os.environ.get('VALUE_ERROR'))
    except:
        print('Something went wrong. Stopping application.')
        break