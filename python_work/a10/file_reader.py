with open("D:\py\python_work\\a10\pi_digits.txt") as file_object:
    lines=file_object.readlines()
for line in lines:
    print(line.rstrip())
pi_string=""
for line in lines:
    pi_string+=line.strip()
print(f"{pi_string} {len(pi_string)}")
print("----------------")
with open("python_work\\a10\pi_digits.txt") as a_object:
    for line in a_object:
        print(line,end="")

with open("python_work\\a10\\learning_python.txt") as obj:
    contents=obj.read()
    lines=obj.readlines()
    for line in lines:
        print(line,end="")
print(contents.rstrip())
message=contents.replace("i","?")
print(message)

with open("python_work\\a10\\programming.txt","r+") as writea:
    strs="I love WangQQ"
    writea.write(strs)
    writea.write("呃逆惠风和")

with open("python_work\\a10\\programming.txt","r+") as writea:
    contenss=writea.read()
    print(contenss)

while True:
    num1=input("enter q to quit ")
    if num1=='q':
        print("Thanks")
        break
    else:
        num2=input("num 2 ")
    try:
        answer=int(num1)/int(num2)
    except ZeroDivisionError:
        print("you cannot divide a num by 0")
    else:
        print(answer)

def plus(num_1,num_2):
    try:
        num_1=int(num_1)
        num_2=int(num_2)
    except ValueError:
        print("Wrong NUMBER")
    else:
        try:
            answer=num_1/num_2
        except ZeroDivisionError:
            print("Cannot 0")
        else:
            print(answer)
while True:
    num1=input("enter q to quit ")
    if num1=='q':
        print("Thanks")
        break
    else:
        num2=input("num 2 ")
    print(num1)
    print(num2)
    plus(num1,num2)