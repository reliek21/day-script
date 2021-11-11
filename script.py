import time
import os
import subprocess
from colorama import init, Fore

# Init colorama
init()


# Send notifications function
def sendNotification(message, text=""):
    subprocess.Popen(["notify-send", message, text])
    return


# Init application function
def initApps(appname, link=""):
    os.system(f'{appname} {link}')


# Menu
def menu():
    print(Fore.CYAN + "=============================================")
    print("Hello, let's get started!")
    print(Fore.CYAN + "=============================================")
    print("Select what you want to do: ")
    print(Fore.GREEN + "1.- Practice English")
    print(Fore.BLUE + "2.- Programming")
    print(Fore.MAGENTA + "3.- Reading")
    print(Fore.WHITE + "4.- Practice Typing")
    print(Fore.RED + "5.- Exit")
    print(Fore.CYAN + "=============================================")


while (True):

    try:
        menu()
        go = int(input(Fore.BLUE + "Select a number: "))
    except:
        menu()

    if (go == 1):
        # Practice English
        initApps("google-chrome", "https://www.duolingo.com/learn")
    elif (go == 2):
        # Programming
        initApps("google-chrome", "https://www.freecodecamp.org/espanol/learn/")
        initApps("google-chrome", "https://www.coursera.org/programs/")
    elif (go == 3):
        # Reading
        initApps("google-chrome", "https://getpocket.com/my-list")
    elif (go == 4):
        # Practice Typing
        initApps("google-chrome", "https://www.keybr.com/")
    elif (go == 5):
        print(Fore.RED + "See you soon...")
        exit()
    else:
        print("It is not a number, please try again.")


    # Show menu after 3 seconds
    time_sec = 3
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        time.sleep(1)
        time_sec -= 1

    # Send notification
    sendNotification("All applications started", "Have a nice day...")
