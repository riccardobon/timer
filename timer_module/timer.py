"""Implements a timer in Python3 by means of asyncio"""

import asyncio
from typing import Any
from typing import Callable


class Timer():
    """For using the timer, first define "interval" and "num_ticks"
    properties. Hence write a coroutine to associate to a timer
    tick event; finally activate the timer with the "run" method.
    """
    async def events_scheduler(self) -> None:
        """Schedules all the programmed events for the timer"""
        for i in range(self._num_ticks):
            asyncio.create_task(self._function(*self._args))
            if i < self._num_ticks-1:
                await asyncio.sleep(self._interval)
        # Wait for the completion of  all the scheduled tasks
        # (including the scheduler itself)
        while len(asyncio.all_tasks()) > 1:
            await asyncio.sleep(self._wait_loop)

    async def dummy_method(self):  # pragma: no cover
        """dummy method"""
        return

    def __init__(self, interval: float = 1.0, num_ticks: int = 1) -> None:
        self.set_interval(interval)
        self.set_num_ticks(num_ticks)
        self._wait_loop = 0.1
        self._loop = asyncio.new_event_loop()
        self._function = self.dummy_method
        self._args: Any = tuple()

    def get_interval(self) -> float:  # pragma: no cover
        """getter for interval property"""
        return self._interval

    def set_interval(self, value: float) -> None:
        """setter for interval property"""
        if not isinstance(value, (int, float, )):
            raise TypeError("interval must be integer or floating point")
        if value <= 0:
            raise ValueError("interval must be greater than zero.")
        self._interval = value

    # interval property
    interval = property(get_interval, set_interval)

    def get_num_ticks(self) -> int:  # pragma: no cover
        """getter for num_ticks property"""
        return self._num_ticks

    def set_num_ticks(self, value: int) -> None:
        """setter for num_ticks property"""
        if not isinstance(value, int):
            raise TypeError("num_ticks must be integer")
        if value < 1:
            raise ValueError("num_ticks must be greater or equal to one.")
        self._num_ticks = value

    # num_ticks property
    num_ticks = property(get_num_ticks, set_num_ticks)

    def run(self, function: Callable, *args: Any) -> None:
        """Entry point for the timer
        :param function: coroutine to execute for each event of the timer
        :param *args: argument to be passed to the coroutine "function"
        """
        self._function = function
        self._args = args
        self._loop.run_until_complete(self.events_scheduler())
        self._loop.close()
