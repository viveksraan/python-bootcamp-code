def hello(display_name="No functionality for name provided"):
    return f"Hi {display_name()}"

def display_name():
    return "Smith"

print(hello(display_name))



