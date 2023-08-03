import os

filename = input("Input Name Of the File : ")

if not os.path.exists(filename + ".csv"):
    with open(f"{filename}.csv", 'x'):
        pass

with open(f"{filename}.csv", 'w') as f:
    print("enter q to quit and save file")
    data = input("Enter Data : ")
    while(data != "q"):
        data = data.replace(" ", "")
        f.write(data + "\n")
        data = input("Enter Data : ")
