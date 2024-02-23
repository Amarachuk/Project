def announce(f):
    def wrapper():
        print("We are about to run a function...")
        f()
        print("The function has been ran successfully.")
    return wrapper
    
@announce
def hello():
    print("Hello, World!")

hello()    