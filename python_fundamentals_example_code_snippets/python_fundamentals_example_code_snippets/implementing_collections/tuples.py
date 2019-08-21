def tuples():
    #ordered and indexed
    t = (1,246,574,4,8)
    for i in t :
        print(i)
    t[5] = 24 # raises an error as it is immutable
    del t[4] # raises an error as it is immutable
    print(t.index(574))
    print(t.count(1))


if __name__ == "__main__":
    tuples()