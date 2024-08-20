import time

hour = int(input("enter hour : "))
minute = int(input("enter minute : "))
second = int(input("enter second : "))


def output():
    print(f"{hour}:{minute}:{second}")


def logic():
    global hour
    global minute
    global second

    second += 1
    if second == 60:
        minute += 1
        second = 0
    if minute == 60:
        hour += 1
        minute = 0
    if hour == 13:
        hour = 1


while True:
    time.sleep(1)
    logic()
    output()
    