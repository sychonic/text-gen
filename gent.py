import random
import sys
import pickle
from collections import defaultdict, Counter

def save_(mod, name):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(mod, f, pickle.HIGHEST_PROTOCOL)

def load_(name):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)

def get_data(data, name):
    with open(name, 'r') as f:
        text = f.read()
    data.extend(text.split());
    
def train_(fileslist, mod_name):
    data = []
    for i in fileslist:
        get_data(data, i)
    model = defaultdict(Counter)
    for i in range(len(data) - 1):
        model[data[i]][data[i+1]] += 1
    save_(model, mod_name)
    print('Обучение завершено..')
    
def generate(word_count, model_name):
    model = load_(model_name)
    cur = random.choice(list(model))
    print(cur.title(), end = ' ')
    for i in range(word_count):
        cur = random.choice(list(model[cur]))
        print(cur, end = '')
        if ((cur[len(cur)-1] == '.') or (cur[len(cur)-1] == '!') or (cur[len(cur)-1] == '?')):
            print()
        else:
            print('', end = ' ')
    
print('Напишите 0, если хотите обучить модель, 1 - если напечатать текст. -1 - выход из программы')
a = input()
if (a == '0'):
    print('Введите имена файлов для обучения через пробел')
    files = input().split()
    print('Введите название модели')
    name = input()
    train_(files, name)
elif(a == '1'):
    print('Введите желаемое количество слов')
    word = int(input())
    print('Введите название модели')
    name = input()
    generate(word, name)
elif(a == '-1'):
    SystemExit
    