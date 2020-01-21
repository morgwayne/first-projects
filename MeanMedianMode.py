list_of_numbers = []


def light_find_mean():
    mean = 0
    r_total = 0
    for i in list_of_numbers:
        r_total += i
    r_total = float(r_total)
    mean = r_total / float(len(list_of_numbers))
    return mean


def find_mean():
    mean = 0
    r_total = 0
    for i in list_of_numbers:
        r_total += i
    r_total = float(r_total)
    mean = r_total / float(len(list_of_numbers))
    rounding = int(input('How many decimals to round to? '))
    mean = round(mean, rounding)
    print('The mean is {}.'.format(mean))
    return mean


def find_mode():
    multiple_mode = []
    mode = int
    is_new = None
    dic = {'none': 0}
    current_highest = 0
    for i in list_of_numbers:
        for entry in dic:
            if str(i) != entry:
                is_new = True
            else:
                is_new = False
                break
        if is_new:
            dic[str(i)] = 1
        elif not is_new:
            dic[str(i)] += 1
    for key in dic:
        if key == 'none':
            pass
        elif dic[key] >= current_highest:
            if dic[key] > current_highest:
                current_highest = dic[key]
                mode = key
            else:
                multiple_mode.append(key)
    multiple_mode.append(mode)
    if len(multiple_mode) > 1:
        print('The modes are {}, each occurring {} times.'.format(multiple_mode, dic[mode]))
    else:
        print('The mode is {} occurring {} times'.format(mode, dic[mode]))


def find_median():
    if len(list_of_numbers) % 2 == 0:
        print('The median is {} and {}.'.format(list_of_numbers[int(len(list_of_numbers) / 2 - 1)],
                                                list_of_numbers[int(len(list_of_numbers) / 2)]))
    else:
        print('The median is {}.'.format(list_of_numbers[int(len(list_of_numbers) / 2)]))


def find_sd():
    mean = light_find_mean()
    deviations = []
    SD = 0
    for i in list_of_numbers:
        deviations.append(i - mean)
    for i in range(len(deviations)):
        deviations[i] = deviations[i] ** 2
    for i in deviations:
        SD += i
    SD = (SD / (len(deviations) - 1)) ** 0.5
    print('The standard deviation is {}.'.format(SD))


def initialize_list():
    global list_of_numbers
    string_list_of_numbers = input('Please enter a list of numbers with commas between each number: ')
    try:
        list_of_numbers = [float(s) for s in string_list_of_numbers.split(',')]
    except ValueError:
        print('Please enter a valid list.')
        initialize_list()
        return
    list_of_numbers.sort()


def start_command():
    command = input('Would you like to find the mean, median, mode, sd, or change list? ')
    if command == 'mean':
        find_mean()
    elif command == 'median':
        find_median()
    elif command == 'mode':
        find_mode()
    elif command == 'change list':
        initialize_list()
    elif command == 'sd':
        find_sd()
    else:
        print('Please enter a valid command.')
        start_command()


while True:
    if not list_of_numbers:
        initialize_list()
    else:
        start_command()
