from pathlib import Path

p = Path('running_total.txt')
if p.read_text() == '':
    p.write_text('0')
type_of_coin = ''
quit_action = ''
units = 'grams'
con_factor = 453.592  # Conversion factor between grams and pounds
running_total = int(p.read_text())  # Running total of coin values while program runs
weights = {  # Gram-based weights of U.S. coins
    'penny': 2.500,
    'nickel': 5.000,
    'dime': 2.268,
    'quarter': 5.670,
    'half dollar': 11.340,
    'dollar': 8.1
}

values = {  # Values (in cents) of U.S. coins
    'penny': 1,
    'nickel': 5,
    'dime': 10,
    'quarter': 25,
    'half dollar': 50,
    'dollar': 100
}

coin_wrapper = {  # How many of each coin can fit in one coin wrapper
    'penny': 50,
    'nickel': 40,
    'dime': 50,
    'quarter': 40,
    'half dollar': 20,
    'dollar': 25
}


# Changes units between grams and pounds
def change_units():
    while True:
        local_units = input('Please enter preferred units (grams or pounds): ')
        if local_units != 'grams' and local_units != 'pounds':
            print('Please enter \'pounds\' or \'grams\': ')
            continue
        else:
            print('Preferred units: ' + local_units)
            return local_units
        break


# Based on unit type, changes values in {weights} to grams or pounds
def convert_weights():
    if units == 'grams' and weights['penny'] != 2.500:
        for i in weights:
            weights[i] *= con_factor
    elif units == 'pounds' and weights['penny'] != 1133.98:
        for i in weights:
            weights[i] /= con_factor


# Changes the type of coin in question
def change_type_of_coin():
    global type_of_coin
    type_of_coin = input('Please enter a type of coin (penny, nickel, dime, quarter, half dollar, dollar: ')
    for i in values:
        if type_of_coin == i:
            is_coin = True
            break
        else:
            is_coin = False
    if is_coin != True:
        print('Please enter a valid coin: ')
        change_type_of_coin()

def write_running_total(num):
    global p
    p.write_text(num)

def start_command():
    global type_of_coin
    global running_total
    global units
    global quit_action
    # Based on user input, determines what the program will execute. Should probably nest each
    # of these inside functions.
    print('Your running total is: ' + str(running_total) + ' dollars')
    quit_action = input(
        'Please choose an option: begin, quit, change units (currently ' + units + '), wipe running total: ')
    if quit_action == 'quit':
        pass
    elif quit_action == 'change units':
        units = change_units()
        convert_weights()
        start_command()
        pass
    elif quit_action == 'wipe running total':
        running_total = 0
        p.write_text('0')
        print('Total successfully wiped.')
        start_command()
        pass
    elif quit_action == 'begin':
        change_type_of_coin()
        weight_of_coin = int(input('Please enter weight of coins (in ' + units + '): '))
        number_of_coins = int(weight_of_coin / weights[type_of_coin])  # Finds number of coins based on weight from {
        # weights}
        amount_of_money = int(number_of_coins * values[type_of_coin] / 100)  # Determines dollar amount of money from
        # {values}
        fit_in_wrapper = int(number_of_coins / coin_wrapper[type_of_coin])  # Determines how many wrappers are needed
        # to hold number_of_coins
        running_total += amount_of_money # Increments running total
        print('You have approximately {} {}, worth {} dollars and you can fill approximately {} coin wrappers.'.format(
            number_of_coins, type_of_coin, amount_of_money, fit_in_wrapper))
        write_running_total(str(running_total))
        start_command()
        pass
    else:
        print('Please enter a valid command: ')
        start_command()
        pass


start_command()
