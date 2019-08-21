
def lists():
    l = [1,3,5,4,2,6,11,'8','9']

    for i in l:
        print(i)
    print("length(l):",len(l))
    l[7] = 8
    l.append("10")
    l.remove("10")
    del l[8]


    reversed(l)
    print("l after reversed(l)", l)
    sorted(l)
    print("l after sorted(l)", l)

    #proves mutable
    sort_l = l.sort()
    print("l after l.sort",l)
    reverse_l = l.reverse()
    print("l after l.reverse", l)


    #proves only shallow copy is done
    l_copy = l.copy()
    print("l[0] is l_copy[0]:",l[0] is l_copy[0])
    print("l_copy == m ", l == l_copy)


    nested_list = [[1, 2], [2, 3]]
    nested_copy = nested_list.copy()
    print("nested_copy[0] is nested_list[0]",nested_copy[0] is nested_list[0])

if __name__ == "__main__":
    lists()