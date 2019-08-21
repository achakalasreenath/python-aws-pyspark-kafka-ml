class File:
    def __init__(self,filename,method):
        print("initializing")
        self.filename = filename
        self.method = method
        self.f = open(self.filename, self.method)
        print("Initializing complete ...")

    def __enter__(self):
        print("entering ...")
        return self.f

    def __exit__(self,type,value,traceback):
        print("file closing ...")
        self.f.close()

def main():
    with File("test.txt",'rt') as f:
        print("before read")
        f.write("huhuh")
        print("after read")

if __name__ == '__main__':
    main()