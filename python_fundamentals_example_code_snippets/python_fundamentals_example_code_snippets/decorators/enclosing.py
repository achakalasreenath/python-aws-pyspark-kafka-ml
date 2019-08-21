message = "global"

#global , enclosing, ocal scopes
#global, nonlocal keywords
def outer():
    message = "enclosing"
    def inner():
        nonlocal message
        message = "local"

    print(message)
    inner()
    print(message)

print(message)
outer()
print(message)
