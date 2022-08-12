#Import your modules here

import sys
import clipboard
import json

#saved data variable.Name of file where we are gonna store the data which is getting copied by the clipboard

saved_data = "clipboard.json"

#Function to write the json file

def save_items(filepath, data):

    with open( filepath,"w") as f:
        json.dump(data,f)

#function to read the json file

def load_items(filepath):

    try:

        with open(filepath,"r") as f:
            data = json.load(f)
    except:
        return {}

# 2 command line argument, 1 being the name of the python file and another is the command we want to run.

if len(sys.argv) == 2:

    command = sys.argv[1] #which command we want to run
    data = load_items(sys.argv[1]) #load the data from json file

    if command == "save":

        key = input("Enter a key:")
        data[key] = clipboard.paste()
        save_items(saved_data,data)

    elif command == "load":

        key = input("Enter key:")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard.")
        else:
            print("Data doesn't exists")

    elif command == "list":

        print(data)

    else:

        print("unknown command")

else:
    print("Please pass exactly one command")



