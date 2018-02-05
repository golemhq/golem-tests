
# Golem Demo Projects

This repo contains example projects using the Golem framework.

Check the Golem repo here: https://github.com/lucianopuccio/golem
Check the full documentation here: http://golem-framework.readthedocs.io/

# Requirements

Firefox 55+

Chrome 58+

Python 3.4+

PIP

Virtualenv (optional)


# Install

## Create a virtualenv (optional)

```
virtualenv env
```

Activate the virtualenv (Linux & Mac):
```
source env/bin/activate
```

Activate the virtualenv (Windows):

```
env\scripts\activate
```

## Install Golem

```
pip install golem-framework
```

## Clone repo

```
git clone https://github.com/lucianopuccio/golem-demo
cd golem-demo
```

# Point to the appropiate webdriver executables

The /drivers/ folder must have the webdriver executables. Download them and make sure that the settings.json points to the correct files.

For example:
```
"chromedriver_path": "./drivers/chromedriver",
```


# Start the web module

```
golem gui
```

The web module is accesible at http://localhost:5000/

Default credentials:

User: admin

Password: admin


# Run a test suite from the console:

```
golem run store_demoqa regression
```


# Run the Golem test suite:

To run the Golem test suite, an instance of the Golem GUI must be running in port 8000 using another console.
Open a new console and run:

```
golem-admin createdirectory test
cd test
golem gui -p 8000
```

Then from the first console:

```
golem run golem regression
```