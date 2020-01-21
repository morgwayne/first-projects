coin_values = {
    'dollar': 1.00,
    'quarter': .25,
    'dime': .10,
    'nickel': .05,
    'penny': .01
}

num_of_each_coin_reset = {
    'dollar': 0,
    'quarter': 0,
    'dime': 0,
    'nickel': 0,
    'penny': 0
}

num_of_each_coin = {
    'dollar': 0,
    'quarter': 0,
    'dime': 0,
    'nickel': 0,
    'penny': 0
}

price_of_item = float
money_in_hand = float
change_amount = float
quit_command = ''


def start_command():
    global price_of_item
    global quit_command
    try:
        price_of_item = float(input('Please enter price of item(s): '))
    except ValueError:
        print('Please enter a valid price.')
        start_command()


def ask_for_money_in_hand():
    global price_of_item
    global money_in_hand
    try:
        money_in_hand = float(input('Please enter money amount given to you by customer: '))
    except ValueError:
        print('Please enter a valid price.')
        ask_for_money_in_hand()
    price_of_item = float(price_of_item)


def perform_calcs():
    global change_amount
    change_amount = money_in_hand - price_of_item
    if change_amount < 0:
        print('You fucked it up, read the prompts.')
        perform_program()
    else:
        rem = change_amount
        for i in coin_values:
            if rem != 0.0 and rem != 0 and rem != 0.00:
                num_of_each_coin[i] = int(rem / coin_values[i])
                rem = rem % coin_values[i]
                rem = round(rem, 2)


def reset_coins():
    global num_of_each_coin
    for i in num_of_each_coin:
        num_of_each_coin[i] = num_of_each_coin_reset[i]


def perform_program():
    global num_of_each_coin
    start_command()
    ask_for_money_in_hand()
    perform_calcs()
    print(num_of_each_coin)
    reset_coins()


while True:
    perform_program()
