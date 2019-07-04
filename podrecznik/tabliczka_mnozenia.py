print("  |", end = "\t")
[print(i, end = '\t') for i in range(1,10)]
print('')
print('---------------------------------------')
for i in range(1,10):
    print('{} |'.format(i), end = "\t")
    for j in range(1,10):
        x = i*j
        print(x, end="\t")
    print('')

