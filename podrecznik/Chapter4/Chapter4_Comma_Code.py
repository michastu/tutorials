spam = ['tomatoes', 'grapes', 'apples', 'bananas', 'tofu', 'cats']


def rozdziel_liste(lista):
    for i in range(len(lista)):
        if i < len(lista)-2:
            print(lista[i], end=', ')
        elif i == len(lista)-2:
            print(lista[i], end=' ')
        elif i == len(lista)-1:
            print('and {}'.format(lista[-1]))


rozdziel_liste(spam)