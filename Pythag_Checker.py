while input('Type anything to begin or \'quit\' to quit: ') != 'quit':
    side1 = int(input('Please enter your first side: '))
    side2 = int(input('Please enter your second side: '))
    side3 = int(input('Please enter your third side: '))

    a = 0
    b = 0
    c = 0
    if side1 > side2 and side1 > side3:
       c = side1
       a = side2
       b = side3
    elif side2 > side1 and side2 > side3:
        c = side2
        a = side1
        b = side3
    else:
       c = side3
       b = side1
       a = side2

    if a**2 + b**2 == c**2:
        print('This triangle is a Pythagorean Triple.')
    else:
        print('This triangle is not a Pythagorean Triple.')



