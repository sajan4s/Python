
x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print("Division cannot be done by 0")
finally:
    print('Division completed')