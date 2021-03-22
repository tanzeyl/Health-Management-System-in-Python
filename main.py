def getdate():
    import datetime
    return datetime.datetime.now()

def func():
    print("Do you want to log new items or review already added items?\nSay 1 for logging and 2 for reviewing.")
    n = int(input())
    if n == 1:
        print("Whose file do you want to edit? Harry, Rohan or Hammad.")
        name = input()
        if name.lower() == "harry":
            print("What do you want to edit? Chose food or exercise.")
            action = input()
            if action.lower() == "food":
                f = open("Harry_food.txt", "a")
                f.write(str([str(getdate())]))
                f.write(input().capitalize())
                f.write("\n")
                f.close()
                print("Log Successful.")
            if action.lower() == "exercise":
                f = open("Harry_exercise.txt", "a")
                f.write(str([str(getdate())]))
                f.write(input().capitalize())
                f.write("\n")
                f.close()
                print("Log Successful.")
        if name.lower() == "rohan":
            print("What do you want to edit? Chose food or exercise.")
            action = input()
            if action.lower() == "food":
                f = open("Rohan_food.txt", "a")
                f.write(str([str(getdate())]))
                f.write(input().capitalize())
                f.write("\n")
                f.close()
                print("Log Successful.")
            if action.lower() == "exercise":
                f = open("Rohan_exercise.txt", "a")
                f.write(str([str(getdate())]))
                f.write(input().capitalize())
                f.write("\n")
                f.close()
                print("Log Successful.")
        if name.lower() == "hammad":
            print("What do you want to edit? Chose food or exercise.")
            action = input()
            if action.lower() == "food":
                f = open("Hammad_food.txt", "a")
                f.write(str([str(getdate())]))
                f.write(input().capitalize())
                f.write("\n")
                f.close()
                print("Log Successful.")
            if action.lower() == "exercise":
                f = open("Hammad_exercise.txt","a")
                f.write(str([str(getdate())]))
                f.write(input())
                f.write("\n")
                f.close()
                print("Log Successful.")



    if n == 2:
        print("Whose file do you want to review?")
        name = input()
        if name.lower() == "harry":
            print("What do you want to review? Chose food or exercise.")
            action = input()
            if action.lower() == "food":
                f = open("Harry_food.txt")
                print(f.read())
                f.close()
            if action.lower() == "exercise":
                f = open("Harry_exercise.txt")
                print(f.read())
                f.close()
        if name.lower() == "rohan":
            print("What do you want to review? Chose food or exercise.")
            action = input()
            if action.lower() == "food":
                f = open("Rohan_food.txt")
                print(f.read())
                f.close()
            if action.lower() == "exercise":
                f = open("Rohan_exercise.txt")
                print(f.read())
                f.close()
        if name.lower() == "hammad":
            print("What do you want to review? Chose food or exercise.")
            action = input()
            if action.lower() == "food":
                f = open("Hammad_food.txt")
                print(f.read())
                f.close()
            if action.lower() == "exercise":
                f = open("Hammad_exercise.txt")
                print(f.read())
                f.close()


func()
