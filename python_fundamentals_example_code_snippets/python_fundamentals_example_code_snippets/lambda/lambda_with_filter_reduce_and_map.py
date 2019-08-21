from functools import reduce


def lambda_with_filter(list):
    return filter(lambda x:x>2, list)

def lambda_with_reduce(list):
    return reduce(lambda x,y: x/x+y, list)

def lambda_with_map(list):
    return map(lambda x:x*2, list)

def main():
    li = [1, 2, 3, 4, 5, 6]
    lambda_with_filter(li)
    lambda_with_map(li)
    lambda_with_reduce(li)

if __name__ == "__main__":
    main()