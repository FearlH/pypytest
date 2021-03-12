name="ada lovelace"
print(name.title())
first_name="ada"
last_name="lovelace"
full_name=f"{first_name} {last_name}"#把大括号内容替换为值
print(f"hello {full_name.title()}")

#
mess="  python  "
print(mess.rstrip())#删除字符串后面的空白，但是得到一个新的字符串,源字符串不变
#strip()删除两端空白字符，包括\t \n 空格，lstrip()删除左端，rstrip()删除右端

print(mess.lstrip())
print(mess.strip())
mess2="\t\n python  \t\n"
print("py")
print(mess2.strip())
print("py")