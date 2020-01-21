from time import sleep
from random import randint


responses = [
    'It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'You may rely on it', 'As I see it', 'Yes',
    'Most Likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Don’t count on it', 'My reply is no', 'My sources say no',
    'Outlook not so good', 'Very doubtful'
]

while input('Ask a question... ') != 'quit':
    print('Thinking...')
    sleep(3)
    rand_num = randint(0,16)
    response = responses[rand_num]
    print(response)
    print('Are you satisfied? Ask another question, or type quit to quit.')
    pass
