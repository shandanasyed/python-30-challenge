def pin(length):
    import random
    pin = ""
    for i in range(length):
        pin += str(random.randint(0, length))
    return pin


myPin = pin(5)
print(myPin)
