"""Tesing suite for Timer class"""

import unittest
import asyncio
import random
from datetime import datetime
from time import monotonic
from typing import List
from timer_module.timer import Timer


class TestTimer(unittest.TestCase):
    """Tesing interval and num_ticks properties; as well as the run method"""
    def setUp(self) -> None:
        # Array for registering the start and the end times for each event
        self._start_times: List[float] = []
        self._end_times: List[float] = []
        random.seed()
        self.timer = Timer()

    async def demo_callable(self, min_duration, max_duration) -> None:
        """Testing coroutine scheduled by the timer"""
        # With time.monotonic() we have a reliable way for
        # measuring time intervals
        self._start_times.append(monotonic())
        duration = random.uniform(min_duration, max_duration)
        print(f"Begin task. The time is now: {datetime.now()}."
              f" Random duration in seconds: {duration}")
        # sleep simulates some work to do within the callable
        await asyncio.sleep(duration)
        print(f"End task. The time is now: {datetime.now()}")
        self._end_times.append(monotonic())

    def test_set_interval_check_raises_typeerror(self) -> None:
        """Check type error for interval"""
        with self.assertRaises(TypeError):
            self.timer.interval = ""  # must be integer or floating point

    def test_set_interval_check_raises_valueerror(self) -> None:
        """Check value error for interval"""
        with self.assertRaises(ValueError):
            self.timer.interval = 0  # must be > 0

    def test_set_num_ticks_check_raises_typeerror(self) -> None:
        """Check type error for num_ticks"""
        with self.assertRaises(TypeError):
            self.timer.num_ticks = 1.0  # must be integer

    def test_set_num_ticks_check_raises_valueerror(self) -> None:
        """Check value error for num_ticks"""
        with self.assertRaises(ValueError):
            self.timer.num_ticks = 0  # must be >= 1

    def test_run_check_time_intervals(self) -> None:
        """Check time intervals"""
        self.timer.interval = 1.19
        self.timer.num_ticks = 3
        random_duration = (5.0, 15.0, )
        self.timer.run(self.demo_callable, *random_duration)
        for i in range(1, len(self._start_times)):
            # Interval among successive schedules
            d_i = self._start_times[i] - self._start_times[i-1]
            print(f"Measured interval for the timer: {d_i}")
            # 0.01 seconds precision
            self.assertAlmostEqual(d_i, self.timer.interval, delta=0.01)

    def test_run_check_num_ticks(self) -> None:
        """Check num_ticks"""
        self.timer.interval = 0.12
        self.timer.num_ticks = 20
        random_duration = (0.1, 1.0)
        self.timer.run(self.demo_callable, *random_duration)
        self.assertEqual(len(self._start_times), self.timer.num_ticks)
        self.assertEqual(len(self._end_times), self.timer.num_ticks)


if __name__ == '__main__':
    unittest.main()
