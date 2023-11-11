from random import randint
counter = 0
first_loop = True
second_loop = True
while first_loop:
    print("first while loop run")
    print("starting: "+ str(counter))
    if counter == 6:
        first_loop = False
    while second_loop:
        counter += 1
        print(counter)
        if counter == 6:
            print("end at:" + str(counter))
            second_loop = False
            break
new_list = [1,0,0,0]
# print(new_list.index("a"))
pos = 0
new_list[pos] = pos + 1
print(new_list)
print(len("[0, 0, 0, 0]"))
string_list = "[0, 0, 0, 0]"
string_list = eval(string_list)
print(string_list[0])