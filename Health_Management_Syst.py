def getdate():
    import datetime
    return datetime.datetime.now()


f_a = open('f_a.txt', 'a+')
f_r = open('f_r.txt', 'a+')
f_t = open('f_t.txt', 'a+')
f_a_d = open('f_a_d.txt', 'a+')
f_r_d = open('f_r_d.txt', 'a+')
f_t_d = open('f_t_d.txt', 'a+')
print("Choose one of them:\n 1. To lock the the data \n 2. To retrieve the data")
a = int(input())
if a == 1:
    print("You want to lock data in Exercise or Diet.\n Choose one of them: \n 1. Exercise\n 2. Diet ")
    e = int(input())
    if e == 1:
        print(" Whose Exercise details you want to lock for:\n 1. Aman \n 2. Rahul \n 3. Tanya")
        l = int(input())
        if l == 1:
            print("-:Append in the Exercise file for Aman:-")
            # here the file for Aman will be accessed for Exercise
            print(getdate())
            f_a.write("[")
            f_a.write(str(getdate()))
            f_a.write("]")
            f_a.write(":\t")
            f_a.write(input())
            f_a.write("\n")
            f_a.close()
            f_a = open('f_a.txt', 'r+')
            print(f_a.read())
            f_a.close()
        elif l == 2:
            print("-:Append in the Exercise file for Rahul:-") #Append the exercise file
            # here the file for Rahul will be accessed for Exercise
            print(getdate())
            f_r.write("[")
            f_r.write(str(getdate()))
            f_r.write("]")
            f_r.write(":\t")
            f_r.write(input())
            f_r.write("\n")
            f_r.close()
            f_r = open('f_r.txt', 'r+')
            print(f_r.read())
            f_r.close()
        elif l == 3:
            print("-:Append in the Exercise file for Tanya:-") #Append in the exercise file
            # here the file for Tanya will be accessed for Exercise
            print(getdate())
            f_t.write("[")
            f_t.write(str(getdate()))
            f_t.write("]")
            f_t.write(":\t")
            f_t.write(input())
            f_t.write("\n")
            f_t.close()
            f_t = open('f_t.txt', 'r+')
            print(f_t.read())
            f_t.close()
        else:
            print("You choose the wrong option")
    elif e == 2:
        print(" Whose Diet details you want to lock for:\n 1. Aman\n 2. Rahul\n 3. Tanya")
        l = int(input())
        if l == 1:
            print("-:Append in the Diet file for Aman:-")
            # here the file for Aman will be accessed for Diet
            print(getdate())
            f_a_d.write("[")
            f_a_d.write(str(getdate()))
            f_a_d.write("]")
            f_a_d.write(":\t")
            f_a_d.write(input())
            f_a_d.write("\n")
            f_a_d.close()
            f_a_d = open('f_a_d.txt', 'r+')
            print(f_a_d.read())
            f_a_d.close()
        elif l == 2:
            print("-:Append in the Diet file for Rahul:-")
            # here the file for Rahul will be accessed for Diet
            print(getdate())
            f_r_d.write("[")
            f_r_d.write(str(getdate()))
            f_r_d.write("]")
            f_r_d.write(":\t")
            f_r_d.write(input())
            f_r_d.write("\n")
            f_r_d.close()
            f_r_d = open('f_r_d.txt', 'r+')
            print(f_r_d.read())
            f_r_d.close()
        elif l == 3:
            print("-:Append in the Diet file for Tanya:-")
            # here the file for Tanya will be accessed for Diet
            print(getdate())
            f_t_d.write("[")
            f_t_d.write(str(getdate()))
            f_t_d.write("]")
            f_t_d.write(":\t")
            f_t_d.write(input())
            f_t_d.write("\n")
            f_t_d.close()
            f_t_d = open('f_t_d.txt', 'r+')
            print(f_t_d.read())
            f_t_d.close()
        else:
            print("You choose the wrong option")

    else:
        print("You choose the wrong option")
elif a == 2:
    print("You want to Retrieve data in Exercise or Diet.\n Choose one of them: \n 1. Exercise\n 2. Diet ")
    e = int(input())
    if e == 1:
        print(" Whose details you want to Retrieve for:\n 1. Aman\n 2. Rahul\n 3. Tanya")
        l = int(input())
        if l == 1:
            print("Retrieve the Exercise file of Aman")
            # here the file for Aman will be accessed for Exercise
            f_a = open('f_a.txt', 'r+')
            print(f_a.read())
            f_a.close()
        elif l == 2:
            print("Retrieve the Exercise file for Rahul")
            # here the file for Rahul will be accessed for Exercise
            f_r = open('f_r.txt', 'r+')
            print(f_r.read())
            f_r.close()
        elif l == 3:
            print("Retrieve the Exercise file for Tanya") #read the exercise file for Tanya
            # here the file for Tanya will be accessed for Exercise
            f_t = open('f_t.txt', 'r+')
            print(f_t.read())
            f_t.close()
        else:
            print("You choose the wrong option")
    elif e == 2:
        print(" Whose details you want to Retrieve for:\n 1. Aman\n 2. Rahul\n 3.Tanya ")
        l = int(input())
        if l == 1:
            print("Retrieve the Diet file of Aman")
            # here the file for Aman will be accessed for Diet
            f_a_d = open('f_a_d.txt', 'r+')
            print(f_a_d.read())
            f_a_d.close()
        elif l == 2:
            print("Retrieve the Diet file for Rahul")
            # here the file for Rahul will be accessed for Diet
            f_r_d = open('f_r_d.txt', 'r+')
            print(f_r_d.read())
            f_r_d.close()
        elif l == 3:
            print("Retrieve the Diet file for Tanya")
            # here the file for Tanya will be accessed for Diet
            f_t_d = open('f_t_d.txt', 'r+')
            print(f_t_d.read())
            f_t_d.close()
        else:
            print("You choose the wrong option")

    else:
        print("You choose the wrong option")
else:
    print('Choose the appropriate option')
