#====================Student Database======================
#
#
import time
#universal value
Students_all=[
    {"name":"Pias",
     "roll": 101,
     "marks":{"math":80,
     "english":75,
     "bangla":82
     }
    },
    {"name":"Rony Nath",
     "roll": 102,
     "marks":{"math":85,
     "english":78,
     "bangla":87
     }
     },

    {"name":"Pabel Barua",
     "roll": 103,
     "marks":{"math":90,
     "english":65,
     "bangla":95
     }
     },

    {"name":"Anoy Talukder",
     "roll": 104,
     "marks":{"math":80,
     "english":89,
     "bangla":90
     }
     }
    ,
    {"name":"Raihan Chowdhuri",
     "roll": 105,
     "marks":{"math":78,
     "english":77,
     "bangla":92
    }
    }
]

def all_student_info():
    print(Fore.CYAN+"===================="+Style.RESET_ALL)
    for x in Students_all:
        print("Name:",x["name"])
        print("Roll:",x["roll"])
        print("Math:",x["marks"]["math"])
        print("English:",x["marks"]["english"])
        print("Bangla:",x["marks"]["bangla"])
        print(Fore.CYAN+"=" *20+Style.RESET_ALL)
def search_by_name():
    print("Loading...", end='')
    for i in range(20):
        print(Fore.LIGHTRED_EX+"█", end='', flush=True)
        time.sleep(0.1)  
    print(" Done!"+Style.RESET_ALL)
    for x in Students_all:
        print(x["name"])
    
def add_new_student():
    print()
    set=0
    while set!=1:
        name=input("Enter your name:")
        roll=int(input("Enter your roll:"))
        for x in Students_all:
            if(x['roll']==roll):
                print("Student alredy exsist")
                break
        math=int(input("Enter Marks in Math:"))
        english=int(input("Enter Marks in English:"))
        bangla=int(input("Entery Marks in Bangla:"))
        set=1
    new_student={
        "name":name,
        "roll":roll,
        "marks":{
            "math":math,
            "english":english,
            "bangla":bangla,
        }
    }
    Students_all.append(new_student)
    all_student_info()
def student_search_by_roll():
    print("Loading...", end='')
    for i in range(20):
        print(Fore.LIGHTRED_EX+"█", end='', flush=True)
        time.sleep(0.1)  
    print(" Done!")
    
    roll_number=int(input("Enter roll please:"))
    print("=" *20)
    found = False
    for student in Students_all:
        if student["roll"] == roll_number:
            print(Fore.LIGHTGREEN_EX+"|Student Found!")
            print("|Roll:", student["roll"])
            print("|Name:", student["name"])
            print("|Math:", student["marks"]["math"])
            print("|English:", student["marks"]["english"])
            print("|Bangla:", student["marks"]["bangla"])
            print("=" *20,end=Style.RESET_ALL)
            found = True
            break
    if not found:
        print(Fore.RED+"Student with roll", roll_number, "not found.")


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from colorama import Fore, Style
print(Fore.RED + "++++++++++++++++++++++++++++++++++++++")
print(Fore.GREEN +"|==========Student Database==========|")
print(Fore.RED + "++++++++++++++++++++++++++++++++++++++")
print(Style.RESET_ALL)
menu=None
while menu!=6:
    print("")
    print(Fore.YELLOW+"1.for see all students data".title())
    print(Fore.BLUE+"2.for see all students name".title())
    print(Fore.GREEN+"3.insert Students details".title())
    print(Fore.LIGHTBLUE_EX+"4.search by Roll".title())
    print(Fore.MAGENTA+"5.update student information".title())
    print(Fore.RED+"6.Exit",end=Style.RESET_ALL)
    print("")
    menu=int(input("Entery your chose:"))
    if(menu==1):
        all_student_info()
    elif(menu==2):
        search_by_name()
    elif(menu==3):
        add_new_student()
    elif(menu==4):
        student_search_by_roll()
    elif(menu==5):
        exit()
    else:
        print("Thanks for searching")
