def dictionary():
    d = {'a':1,'b':2,'c':3}

    #values unpacking
    for x,y in d.items():
        print(x,y)
    print("d['a'] :",d['a'])
    print("d.get('b') :",d.get('b'))
    print("dict.values() :",d.values())
    print("dict.keys() :",d.keys())

    d["d"] = 4

    #dict has no method remove() like list
    d.pop("d")
    del d['c']

    #proves shallow copying
    d_copy = d.copy()
    print("d_copy['a'] is d['a'] :",d_copy['a'] is d['a'])

    #proves mutable
    d_update = d.update({'b': 3, 'e':5})
    print("d after d_update: ",d)


if __name__ == '__main__':
    dictionary()


