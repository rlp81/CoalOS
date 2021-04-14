from logging import fatal
import time
import json

sysopen = False
Topen = False
Fopen = False
Adpan = False

with open("first.json", "r") as f:
    first = json.load(f)

with open("permissions.json", 'r') as f:
    per = json.load(f)

with open("name.json", "r") as f:
    Termname = json.load(f)

while True:
    if first["First"] == "True":
        print("To access the admin account login with User: Admin and Password 4670")
        first["First"] = "False"
        with open("first.json", "w") as f:
            json.dump(first, f)
    print("Open: Classified, System")
    command = input("")
    if command == ("Open Classified"):
        print("sorry that's illegal")
    if command == ("Open System"):
        print("Starting System")
        print("Created by Coal#7238")
        time.sleep(5)
        print(Termname["TerminalName"])
        time.sleep(.5)
        print("All rights reserved")
        time.sleep(3)
        sysopen = True
        while sysopen == True:
            print("Please Login by typing: Login Or type: Exit to exit the terminal computer")
            print("You can also make an account by typing CreateAcc")
            syscommand = input("")
            if syscommand == "Exit":
                sysopen = False
            if syscommand == "Login":
                with open("users.json", 'r') as f:
                    users = json.load(f)
                user = input("Username: ")
                if str(user) in users:
                    passw = input("Password: ")
                    if users[str(user)] == str(passw):
                        Topen = True
                        print("Hello and Welcome to The Terminal computer")
                        print("What application would you like too open? To list the applications type list.")
                        print("To exit the computer or any application type: Exit")
                        while Topen == True:
                            syscommand = input('')
                            if syscommand == ("list"):
                                if per[str(user)]["AP"] == "True":
                                    print("Applications: File Explorer, Admin Panel")
                                else:
                                    print("Applications: File Explorer")
                            if syscommand == ("Exit"):
                                Topen = False

                            if syscommand == ("File Explorer"):
                                with open("permissions.json", 'r') as f:
                                    per = json.load(f)
                                if per[str(user)]["EF"] == "True":
                                    print("To create a file type: CreateFile")
                                print("To open files type: Open {File Name}")
                                print("files: Cake.txt, Custom Files")
                                with open("cfiles.json", "r") as f:
                                    cfile = json.load(f)
                                syscommand = input()
                                if syscommand == "Open Custom Files":
                                    print("What is the name of the custom file?")
                                    file = input()
                                    if str(file) in cfile:
                                        print("File contents:")
                                        print(cfile[str(file)])
                                    if not str(file) in cfile:
                                        print("File doesn't exist.")
                                if file == "CreateFile":
                                    with open("cfiles.json", "r") as f:
                                        cfile = json.load(f)
                                    print("What is the name of the file?")
                                    file = input()
                                    print("What will it contain?")
                                    file1 = input()
                                    cfile[file] = file1
                                    with open("cfiles.json", "w") as f:
                                        cfile = json.dump(cfile, f, indent=4)
                                if file == "Open Cake.txt":
                                    print("To make the Cake:")
                                    print("One 18.25 ounce package chocolate cake mix.")
                                    print("One can prepared coconut pecan frosting.")
                                    print("Three slash four cup vegetable oil.")
                                    print("Four large eggs. One cup semi-sweet chocolate chips.")
                                    print("Three slash four cups butter or margarine.")
                                    print("One and two third cups granulated sugar.")
                                    print("Two cups all purpose flower.")
                                    print("Don't forget garnishes such as:")
                                    print("Fish shaped crackers.")
                                    print("Fish shaped candies.")
                                    print("Fish shaped solid waste.")
                                    print("Fish shaped dirt.")
                                    print("Fish shaped ethyl benzene.")
                                    print("Pull and peel licorice.")
                                    print("Fish shaped volatile organic compounds and sediment shaped sediment.")
                                    print("Candy coated peanut butter pieces. Shaped like fish.")
                                    print("One cup lemon juice.")
                                    print("Alpha resins.")
                                    print("Unsaturated polyester resin.")
                                    print("Fiberglass surface resins.")
                                    print("And volatile malted milk impoundments.")
                                    print("Nine large egg yolks.")
                                    print("Twelve medium geosynthetic membranes.")
                                    print("One cup granulated sugar.")
                                    print("An entry called 'how to kill someone with your bare hands'.")
                                    print("Two cups rhubarb, sliced.")
                                    print("Two slash three cups granulated rhubarb.")
                                    print("One tablespoon all-purpose rhubarb.")
                                    print("One teaspoon grated orange rhubarb.")
                                    print("Three tablespoons rhubarb, on fire.")
                                    print("One large rhubarb.")
                                    print("One cross borehole electro-magnetic imaging rhubarb.")
                                    print("Two tablespoons rhubarb juice.")
                                    print("Adjustable aluminum head positioner.")
                                    print("Slaughter electric needle injector.")
                                    print("Cordless electric needle injector.")
                                    print("Injector needle driver.")
                                    print("Injector needle gun.")
                                    print("Cranial caps.")
                                    print("And it contains proven preservatives, deep penetration agents, and gas and odor control chemicals.")
                                    print("That will deodorize and preserve putrid tissue.")

                            if per[str(user)]["AP"] == "True":
                                if syscommand == "Admin Panel":
                                    print("To view commands type: list")
                                    print("To exit type: Exit")
                                    Adpan = True
                                    while Adpan == True:
                                        syscommand  = input()
                                        if syscommand == 'list':
                                            print("DelApp")
                                            print("DelUser")
                                            print("ManageSystem")
                                        if syscommand == "Exit":
                                            Adpan = False
                                        if syscommand == "ManageSystem":
                                            print("For a list of commands type: list")
                                            print("To exit type: Exit")
                                            ms = True
                                            while ms == True:
                                                syscommand = input()
                                                if syscommand == "list":
                                                    print("ChangeTerminalName")
                                                    print("Permissions")
                                                    print("ChangePass")
                                                if syscommand == "ChangePass":
                                                    with open("users.json", 'r') as f:
                                                        users = json.load(f)
                                                    print("What User's password do you want to change?")
                                                    user = input("User:")
                                                    if str(user) in users:
                                                        print("What is the new password?")
                                                        passw = input("Password:")
                                                        users[str(user)] = passw
                                                        with open("users.json", "w") as f:
                                                            json.dump(users, f, indent=4)
                                                    if not str(user) in users:
                                                        print("Error no such user.")
                                                if syscommand == "Exit":
                                                    ms = False
                                                    print("To view commands type: list")
                                                    print("To exit type: Exit")
                                                if syscommand == "Permissions":
                                                    perms = True
                                                    while perms == True:
                                                        print("What user would you like to change permissions for?")
                                                        user = input("User:")
                                                        if user == "Admin":
                                                            print("Error you cannot change permissions for this account.")
                                                        with open('users.json', 'r') as f:
                                                            users = json.load(f)
                                                        if not str(user) in users:
                                                            print("Error this User does not exist.")
                                                        if str(user) in users:
                                                            with open("permissions.json", "r") as f:
                                                                per = json.load(f)
                                                            print("To see permission commands type: list")
                                                            perw = True
                                                            while perw == True:
                                                                syscommand = input()
                                                                if syscommand == "Edit Files":
                                                                    print("Type True or False")
                                                                    access = input("")
                                                                    if access == "True":
                                                                        per[str(user)]["EF"] = "True"
                                                                        print(f"User {user} can now create files.")
                                                                        with open("permissions.json", 'w') as f:
                                                                            json.dump(per, f, indent=4)
                                                                    if access == "False":
                                                                        per[str(user)]["EF"] = "False"
                                                                        print(f"User {user} can not create files.")
                                                                        with open("permissions.json", 'w') as f:
                                                                            json.dump(per, f, indent=4)
                                                                if syscommand == "Access AP":
                                                                    print("Type True or False")
                                                                    access = input("")
                                                                    if access == "True":
                                                                        per[str(user)]["AP"] = "True"
                                                                        print(f"User {user} can now access the Admin Panel.")
                                                                        with open("permissions.json", 'w') as f:
                                                                            json.dump(per, f, indent=4)
                                                                    if access == "False":
                                                                        per[str(user)]["AP"] = "False"
                                                                        print(f"User {user} can not access the Admin Panel.")
                                                                        with open("permissions.json", 'w') as f:
                                                                            json.dump(per, f, indent=4)
                                                                if syscommand == "list":
                                                                    print("Access AP(Admin Panel)")
                                                                    print("Edit Files(In File Explorer)")
                                                                

                                                if syscommand == "ChangeTerminalName":
                                                    print("What would you like to change the terminal name to?")
                                                    with open('name.json', 'r') as f:
                                                        Tname = json.load(f)
                                                    NewName = input("Name:")
                                                    Tname["TerminalName"] = NewName
                                                    with open('name.json', 'w') as f:
                                                        json.dump(Tname, f)
                                                    print("For a list of commands type: list")
                                                    print("To exit type: Exit")
                                                            
                                            

                                                    
                                        if syscommand == "DelUser":
                                            delu = True
                                            print("Type the user you want to delete.")
                                            print("Type Exit to exit DelUser.")
                                            while delu == True:
                                                user = input("User:")
                                                with open("users.json", 'r') as f:
                                                    users = json.load(f)
                                                if user == "Exit":
                                                    delu = False
                                                    print("To view commands type: list")
                                                    print("To exit type: Exit")
                                                if str(user) in users:
                                                    users.pop(str(user))
                                                    with open("users.json", "w") as f:
                                                        json.dump(users, f)
                                        

                            if syscommand == ("Exit"):
                                print("Hello and Welcome to The Terminal computer")
                                print("What application would you like too open? To list the applications type list.")
                                print("To exit the computer or any application type: Exit")
                    else:
                        print("Incorrect PassWord")
                else:
                    print("Incorrect Username")
                    
            if syscommand == "CreateAcc":
                user = input("NewUsername:")
                passw = input("NewPassword:")
                with open('users.json', 'r') as f:
                    users = json.load(f)
                with open("permissions.json", "r") as p:
                    perm = json.load(p)
                if str(user) in users:
                    print("Error this usernamme already exists.")
                users[user] = passw
                perm[user] = {}
                perm[user]['AD'] = "False"
                perm[user]['EF'] = "False"
                with open('users.json', 'w') as f:
                    json.dump(users, f, indent = 4)
                with open("permissions.json", "w") as p:
                    json.dump(perm, p, indent = 4)
                

    if command == ("Quit"):
        quit()
