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
    os.system(Fore.WHITE + f'{appname} {link}')


# Menu
def menu():
    print(Fore.CYAN + "=============================================")
    print("Hello, let's get started!")
    print(Fore.CYAN + "=============================================")
    print("Select what you want to do: ")
    print(Fore.GREEN + "1.- Learn English")
    print(Fore.BLUE + "2.- Study Programming")
    print(Fore.MAGENTA + "3.- Reading and Listen")
    print(Fore.WHITE + "4.- Practice Typing")
    print(Fore.BLUE + "5.- Write on FreeCodeCamp")
    print(Fore.YELLOW + "6.- Inspiration")
    print(Fore.RED + "7.- Exit")
    print(Fore.CYAN + "=============================================")


while (True):

    try:
        menu()
        go = int(input(Fore.BLUE + "Select a number: "))
    except:
        menu()

    if (go == 1):
        # Learn English
        initApps("google-chrome", "https://www.duolingo.com/learn")
        initApps("google-chrome", "https://podcasts.google.com/feed/aHR0cHM6Ly9mZWVkcy5zb3VuZGNsb3VkLmNvbS91c2Vycy9zb3VuZGNsb3VkOnVzZXJzOjMxMTc5ODczNi9zb3VuZHMucnNz?sa=X&ved=2ahUKEwjc18qv89LzAhXglIQIHfLoC20Q9sEGegQIARAJ")
        initApps("google-chrome", "https://www.youtube.com/c/AprendeIngl%C3%A9sconMovieMethod/videos")
        initApps("google-chrome", "https://podcasts.google.com/feed/aHR0cHM6Ly9lbnBvZGNhc3QubGlic3luLmNvbS9yc3M?sa=X&ved=2ahUKEwjc18qv89LzAhXglIQIHfLoC20Q9sEGegQIARAH")
    elif (go == 2):
        # Study Programming
        initApps("google-chrome", "https://www.freecodecamp.org/espanol/learn/")
        initApps("google-chrome", "https://www.sololearn.com/home")
        initApps("google-chrome", "https://www.coursera.org/programs/6a5623ed-f681-4fc5-a937-941c849c0944?currentTab=MY_COURSES&eoc=true")
    elif (go == 3):
        # Write on FreeCodeCamp
        initApps("google-chrome", "https://trello.com/b/52v0L3rp/fcc-articulos-al-espa%C3%B1ol")
        initApps("google-chrome", "https://www.freecodecamp.org/espanol/news/ghost/#/site")
        initApps("google-chrome", "https://www.deepl.com/es/translator")
        initApps("google-chrome", "https://languagetool.org/es/")
    elif (go == 4):
        # Reading and Listen
        initApps("google-chrome", "https://getpocket.com/my-list")
        initApps("google-chrome", "https://podcasts.google.com/feed/aHR0cHM6Ly9hbmNob3IuZm0vcy80YzIyNzM3OC9wb2RjYXN0L3Jzcw?sa=X&ved=2ahUKEwjc18qv89LzAhXglIQIHfLoC20Q9sEGegQIARAF")
        initApps("google-chrome", "https://www.youtube.com/c/freeCodeCampTalks/videos")
        initApps("google-chrome", "https://github.com/")
        initApps("google-chrome", "https://blog.facialix.com/")
    elif (go == 5):
        # Inspiration
        initApps("google-chrome", "https://dribbble.com/shots/popular/web-design")
        initApps("google-chrome", "https://dribbble.com/shots/popular/mobile")
        initApps("google-chrome", "https://www.uplabs.com/")
    elif (go == 6):
        # Practice Typing
        initApps("google-chrome", "https://www.keybr.com/")
    elif (go == 7):
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
    # sendNotification("All applications started", "Have a nice day, Keiler...")
