import random

w = open('words.txt', 'r', encoding='UTF-8')
words = w.read().split('\n')
w.close()

print(random.choice(words))