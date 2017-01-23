def oneedit(t, s):
    a=sorted(t)
    b=sorted(s)
    count = 0
    print(a,b)
    if (a == b):
        print('Not a one way edit')
    else:
        for x1 in a:
            if x1 in b:
                count += 1
                print(count)
            else:
                count -= 1
                print(count)
        print(count)
        if (count == (len(a) - 2)):
            print('It\'s one way edit')
        else:
            print('Its not')


oneedit('saiuz', 'saiu')
