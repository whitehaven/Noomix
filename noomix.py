import random

in_file = open('textinput.txt', mode='r')

for line in in_file:
    test_line = line.split()
    for word in test_line:
        test_word = word.strip('.:,-')
        if len(test_word) == 1:
            print(test_word, end=' ')
        else:
            random_inner = list(test_word[1:-1])
            random.shuffle(random_inner)
            finished_word = test_word[0] + ''.join(random_inner) + test_word[-1]
            print(finished_word, end=' ')
    print()

in_file.close()
