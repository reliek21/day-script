import os
import subprocess


# Send notifications function
def sendNotification(message, text=""):
    subprocess.Popen(["notify-send", message, text])
    return


# Init appliacation function
def initApps(appname, link=""):
    os.system(f'{appname} {link}')


lest_go = input("Are you ready to start? ")


if lest_go == "yes" or lest_go == "Yes" or lest_go == "y":
    sendNotification("Good Morning, Keiler!", "Les´t Go")

    # Open applications
    # Google App
    initApps("google-chrome", "https://coderadio.freecodecamp.org/")
    initApps("google-chrome", "https://www.keybr.com/")
    initApps("google-chrome", "https://www.duolingo.com/learn")
    initApps("google-chrome", "https://www.coursera.org/programs/6a5623ed-f681-4fc5-a937-941c849c0944?currentTab=MY_COURSES&eoc=true")
    initApps("google-chrome", "https://www.freecodecamp.org/espanol/learn/")
    initApps("google-chrome", "https://getpocket.com/my-list")
    initApps("google-chrome", "https://github.com/")
    initApps("google-chrome", "https://podcasts.google.com/")
    initApps("google-chrome", "https://blog.facialix.com/")

    # Other applications
    initApps("google-calendar")

    # Send notification
    sendNotification("All applications started", "Have a nice day, Keiler...")
    exit()
else:
    sendNotification("Don´t worry", "Ok see you later")
    exit()
