vowels = 'aeiouAEIOU'

story = 'A vacation is when you take a trip to some {adjective #1} place with your {adjective #2} family. Usually you go to some place that is near ' \
        'a {noun #1} or up on a {noun #2}. A good vacation place is one where you can ride {plural noun #1} or play {a game} or go hunting for {plural noun #2}. I like to spend ' \
        'my time {verb ending in \'ing\' #1} or {verb ending in \'ing\' #2}. When  parents  go  on  a  vacation,  they  spend  their  time  eating  three {plural noun #3} a day, and fathers play ' \
        'golf, and mothers sit around {verb ending in \'ing\' #3}. Last summer, my little brother fell in a {noun #3} and  got  poison {a plant} all over his {a part of the body}.  My  ' \
        'family is going to go to (the) {a place}, and I will practice {verb ending in \'ing\' #4}. Parents need vacations more than kids because parents are ' \
        'always very {adjective #3} and because they have to work {a number} hours every day all year making enough {plural noun #4} to pay for the vacation.'

new_story = ''

list_of_blanks = {
    'adjective #1': '',
    'adjective #2': '',
    'noun #1': '',
    'noun #2': '',
    'plural noun #1': '',
    'a game': '',
    'plural noun #2': '',
    'verb ending in \'ing\' #1': '',
    'verb ending in \'ing\' #2': '',
    'plural noun #3': '',
    'verb ending in \'ing\' #3': '',
    'noun #3': '',
    'a plant': '',
    'a part of the body': '',
    'a place': '',
    'verb ending in \'ing\' #4': '',
    'adjective #3': '',
    'a number': '',
    'plural noun #4': ''
}


def start_command():
    global story
    global list_of_blanks
    for i in list_of_blanks:  #Fills list_of_blanks with user input
        list_of_blanks[i] = input('Please enter ' + i + ': ')
    new_story = story.format(**list_of_blanks)
    for vowel in vowels:
        for i in range(0, len(new_story)):
            if new_story[i] == 'a' and new_story[i+1] == ' ' and new_story[i+2] == vowel:
                new_story = new_story[:i+1] + 'n' + new_story[i+1:]
                continue
    return new_story

while True:
    print(start_command())
