#yields onlt the first number of values in th iterable equal to count
def take(count, iterable):
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item
#eliminates duplicates
def distinct(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)


def run_distinct():

    for item in distinct([1,2,2,3,4,5]):
        print(item)

def run_pipeline():
    for item in take(3,distinct([1, 2, 2, 3, 4, 5])):
        print(item)

if __name__ == '__main__':
    run_pipeline()
