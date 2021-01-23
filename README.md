Timer 
================
First version developed on 2019-03-26

## Introduction

This is a timer implementation in Python based on **asyncio** library.
It requires Python version 3.7 in order to run properly.

## Basic usage example:

``` python
""" Timer basic usage example """
import asyncio
from datetime import datetime
from timer_module.timer import Timer


class DemoTimer():
    """Timer demonstration"""
    async def task(self):
        """This is a dummy method: it will be called every time the event
        will be triggered. Replace the function with your own task"""
        print(f"Begin task {datetime.now()}")
        await asyncio.sleep(4)  # Simulates some activity, 4 seconds
        print(f"End task: {datetime.now()}")
        return

    def __init__(self):
        """Setting up timer essential parameters"""
        self.timer = Timer()
        self.timer.interval = 0.3  # Repeat every 0.3 seconds
        self.timer.num_ticks = 5  # Repeat the event 5 times

    def run_demo(self):
        """Startup the timer"""
        self.timer.run(self.task)


if __name__ == '__main__':
    d = DemoTimer()
    d.run_demo()
```


## Advanced usage: passing arguments to the task function

``` python
""" Timer advanced usage example """
import asyncio
from random import sample
from datetime import datetime
from timer_module.timer import Timer


class DemoTimer():
    """Timer demonstration"""
    async def task(self, *s):
        """This is a dummy method: it will be called every time the event
        will be triggered. Replace the function with your own task"""
        print(f"Begin task: { datetime.now()}")
        print(f"Arguments: {s}")
        await asyncio.sleep(4)  # Simulates some activity, 4 seconds
        print(f"End task: {datetime.now()}")
        return

    def __init__(self):
        """Setting up timer parameters"""
        self.timer = Timer()
        self.timer.interval = 0.3  # Repeat every 0.3 seconds
        self.timer.num_ticks = 5  # Repeat the event 5 times
        # Sampling 60 random integers from a large population,
        # and passing them to timer's task as argument:
        self.timer.arguments = sample(range(10000000), 60)

    def run_demo(self):
        """Startup the timer"""
        self.timer.run(self.task, *self.timer.arguments)


if __name__ == '__main__':
    d = DemoTimer()
    d.run_demo()
```


## Creating a development environment
The following are some notes for creating from scratch a Python development environment,
setting up **virtualenv** and installing all the needed packages for this project.

In case it shoud be missing, install from root the package installer **pip**. For example in Debian 10 
we can do it in this way:

``` bash
apt-get update
apt-get install python3-pip
```

Upgrade **pip** and install **virtualenv** (run only once from the standard user):

``` bash
python3 -m pip install --upgrade pip --user
python3 -m pip install virtualenv --user
```

Also it is a good idea to add the **~/.local/bin** folder to the **PATH** environment variable.
Now move to the project folder and create a virtual envirnoment:

``` bash
virtualenv --python=python3.7 .vrtenv
```

For activating the virtual environment we run:

``` bash
source .vrtenv/bin/activate
```

Simply we deactivate with:

``` bash
deactivate
```

We need to install some tools for unit testing:

``` bash
python -m pip install nose rednose pytest coverage pytest-cov
```

We might also want to perform some *code linting* and maybe some *static type checking* too:

``` bash
python -m pip install flake8 pylint mypy
```
