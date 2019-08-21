from contextlib import contextmanager


class Transaction:
    x_id = 123
    def __init__(self):
        pass
    def transact(self):
        Transaction.x_id += 1
        print("Processing transaction {}".format(Transaction.x_id))
    def rollback(self):
        print("Rolling transaction {} back".format(Transaction.x_id))
        Transaction.x_id -= 1

@contextmanager
def transaction():
    tx = Transaction()
    try:
        yield tx
        tx.transact()
    except:
        tx.rollback()

def main():
    with transaction() as t:
        raise ValueError("Error")

if __name__ == "__main__":
    main()

