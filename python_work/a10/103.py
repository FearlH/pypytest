name=input("name  ")
with open("python_work\\a10\\guests.txt","a") as guest_name:
    guest_name.write(name+"\n")
with open("python_work\\a10\\guest_book.txt","a") as hello:
    while True:
        name=input("name or q to quit\n")
        if name=="q":
            break
        else:
            print(f"Hello {name}")
            hello.write(f"{name}\n")

    