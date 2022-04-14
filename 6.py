my_range = list(range(-2, 5, 3))
print(my_range)

for i in range(5):
    print(i)

names = ["yekutiel", "ginal", "adi", "elisaf"]

for name in names:
    if name == "elisaf":
        continue
    print(name)
    if name == "adi":
        print("I've found adi, exiting...")
        break
for i in range(len(names)):
    print(names[i])
print("loop finished successfully")
a = 0
while a < 5:
    print(a)
    a = a + 1
else:
    print("done")

if a == 0:
    pass
else:
    print("a is bor 0")
    