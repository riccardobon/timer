Timer 
================
First version developed on 
2019-03-26

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
