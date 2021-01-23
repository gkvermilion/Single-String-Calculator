def Calculate():
    symbols = input('Please type in the math operation:\n')
    operation = ''.join([o for o in symbols if o not in '0123456789'])


    if '+' in symbols:
        symbols = list(symbols.split(sep='+'))
    elif '-' in symbols:
        symbols = list(symbols.split(sep='-'))
    elif '/' in symbols:
        symbols = list(symbols.split(sep='/'))
    elif '*' in symbols:
        symbols = list(symbols.split(sep='*'))
    else:
        print('Unavailable command.')


    for symbol in range(len(symbols)):
        symbols[symbol] = int(symbols[symbol])
    a, b = symbols[0], symbols[1]

    # Addition
    if operation == '+':
        print('{} + {} = '.format(a, b) + str(a + b))
    # Subtraction
    elif operation == '-':
        print('{} - {} = '.format(a, b) + str(a - b))
    # Division
    elif operation == '/':
        try:
            print('{} / {} = '.format(a, b) + str(a / b))
        except ZeroDivisionError:
            print('Second number mustn\'t be equal to 0.')
    # Multiplication
    elif operation == '*':
        print('{} * {} = '.format(a, b) + str(a * b))
    Again()


def Again():
    calc_again = input('Do you want to calculate again?\n'
                       'Please type Y for YES or N for NO.\n')
    if calc_again.upper() == 'Y':
        Calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        Again()


def Welcome():
    print('Welcome to Calculator')


Welcome()
Calculate()