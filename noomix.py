import random

test_words = ["r", "revolt", "objection"]

for test_word in test_words:
    if len(test_word) == 1:
        print(test_word)
    else:
        random_inner = list(test_word[1:-1])
        random.shuffle(random_inner)
        finished_word = test_word[0] + ''.join(random_inner) + test_word[-1]
        print(finished_word)
