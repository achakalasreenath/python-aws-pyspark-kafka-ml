def sets():
    #unordered and unindexed
    s = {1,2,66,5,8,643}

    #proves iterable
    for i in s:
        print(i)
        
    s.add(75)
    print("s after add",s)

    #proves mutable
    s.update({43,2524,52,45})
    print("s after update",s)
    s.remove(43)

if __name__ =='__main__':
    sets()