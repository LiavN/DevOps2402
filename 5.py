ifTrue = False

a = 2
b = 2.5
str_one = "one"
str_three = "Three"
first_array = []
second_array = []

if a < b and str_one != str_three or ifTrue:
    print("a is lower then b")
elif a == b or str_one == "3":
    print("a equals b")
else:
    print("a is not lower then b")

if 0 <= a <= 4:
    print("a between 0 and 4")

if first_array:
    print("first_array has elements")

if len(second_array) > 2:
    print("second array has more then 2 elements")
a = 54
c = 5
d = 5
e = [1, 2, 3]
f = [1, 2, 3]
if c == d:
    print("c equals d")
if c is d:
    print("c is d")
if e == f:
    print("e equals f")
if e is f:
    print("")
