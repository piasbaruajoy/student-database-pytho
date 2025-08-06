#যে কোনো ২ টি ইন্ডেক্স এর মান যোগ করে টার্গেট মান পাওয়া জায় কি না
#
#
#
my_list=[]
user_list_input=int(input("How many value want to input:"))
for x in range(0,user_list_input):
    my_list.append(int(input("Enter your value:")))
targer_number=int(input("Enter your target number:"))

#print(my_list)
for x in range(0,1):
    for j in range(0,len(my_list)):
        if (my_list[x]+my_list[j]==targer_number):
            print(f"[{x},{j}]")
        
