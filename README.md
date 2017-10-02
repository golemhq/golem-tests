
# Golem Demo Projects

This repo contains example projects using the Golem framework.

Check the Golem repo here: https://github.com/lucianopuccio/golem
Check the full documentation here: http://golem-framework.readthedocs.io/

# Requirements

Firefox 55+

Chrome 58+

Selenium 3.5+

PIP

Virtualenv (optional)


# Install

## Create a virtualenv (optional)

```
virtualenv env
```

Activate the virtualenv in Linux & Mac
```
souce env/bin/activate
```

Activate the virtualenv in Windows:

```
env\scripts\activate
```

## Clone & Install

```
git clone https://github.com/lucianopuccio/golem-demo

pip install -r requirements.txt
```

# Point to the appropiate webdriver executables

The drivers/ folder has the required webdriver executables for each platform. Check that in the settings.json, the path points to the correct executable.

For example: for Mac, the chrome_driver_path should be:
"chrome_driver_path": "./drivers/mac/chromedriver_mac_2.32",

And so on..


# Start the web module

```
python golem.py gui
```

The web module is accesible at http://localhost:5000/

Credentials:
User: admin
Password: admin


# Run a test suite from the console:

```
python golem.py run store_demoqa regression
```

