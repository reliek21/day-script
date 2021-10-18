
# Daily Script

A small python script that executes the most frequent tasks such as: Study English, Learn a programming language and more.


## Features

- [x] Menu
- [x] Functions for add URLs
- [ ] Colors on console

  
## Run Locally

Clone the project

```bash
  git clone git@github.com:reliek21/daily-script.git
```

Go to the project directory

```bash
  cd daily-script
```

Run the project

```bash
  python3 daily-script
```

  
## Usage/Examples



Send notifications
```python
import subprocess

# Send notifications function
def sendNotification(message, text=""):
    subprocess.Popen(["notify-send", message, text])
    return

# Call the function
sendNotification("All applications started", "Have a nice day =)")
```

Appication function

```python
import os

# Init application function
def initApps(appname, link=""):
    os.system(f'{appname} {link}')

# Init app
initApps("google-chrome", "https://www.duolingo.com/learn")
```

  
## Authors

- [@reliek](https://www.github.com/reliek)

  
## License

[MIT](https://choosealicense.com/licenses/mit/)

  
