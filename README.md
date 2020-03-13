# Golem Tests

Tests for the [Golem](https://github.com/golemhq/golem) project.

Read the full documentation here: http://golem-framework.readthedocs.io/


# Install

## Requirements

* Python 3.5+

## Install Golem

```bash
pip install golem-framework
```

## Clone This Repo

```bash
git clone https://github.com/golemhq/golem-tests.git
cd golem-tests
```

## Download Webdrivers

```bash
webdriver-manager update
```

# Suites

This repository contains three projects: **golem_api**, **golem_gui** and **golem_integration**

## golem_gui

These are Golem tests that test the Golem GUI. So meta... (⌐■_■)

A Golem GUI instance must to be running in port 8000.
This will be considered the System Under Test. 

Open a new console pointing to a different location than before and run:

```
golem-admin createdirectory test
cd test
golem gui -p 8000
```

Then from the first console run:

```
golem run golem_gui regression
```

## golem_integration

These are tests that ensure the Browser class, Element class and actions module work as expected.

### Stage environment

Points to https://www.web-playground.net/

```
golem run golem_integration regression -e stage
```

### Test environment (local)

An instance of the [Web Playground](https://github.com/golemhq/web-playground) must be running in port 6565.

Open a second console and run:

```
pip install web-playground
web-playground
```

From the first console:
```
golem run golem_integration regression -e test
```

# Open the Reports

Start the Golem GUI:

```
golem run gui
```

Then the reports are available here:
    
http://localhost:5000/report/project/golem_gui/

http://localhost:5000/report/project/golem_integration/