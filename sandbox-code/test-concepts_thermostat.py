

from enum import Enum

# Themostat -------------------------------------

from typing import TypeVar

# This example is from Introduction to Software Testing, Chapter 8, code is on page 210.
# It is a better example of why java sucks.

Period = Enum('Period', 'morning, afternoon, evening')
Day    = Enum('Day', 'weekend, weekday')

P = TypeVar('P', bound=Period)                  # I'm not sure how to use these well…
D = TypeVar('D', bound=Day)

class Themostat:

    def __init__(self):
        
        self._current_temp: int = 0
        self._threshold: int    = 0
        self._time_since_last :int = 0
        self._min_lag: int      = 0
        self._override: bool    = False
        self._overtemp: int     = 0
        self._runtime: int      = 0
        self._heater_on: bool   = False
        self._period: P         = None
        self._day: D            = None

        self._settings          = {(Period.morning, Day.weekend): 65,
                                   (Period.morning, Day.weekday): 65,
                                   (Period.afternoon, Day.weekend): 69,
                                   (Period.afternoon, Day.weekday): 69,
                                   (Period.evening, Day.weekend): 72,
                                   (Period.evening, Day.weekday): 72}

    def turn_heat_on(self, period: P, day :D) -> bool:

        dtemp = self._settings[(period, day)]

        if (self._current_temp < (dtemp - self._threshold)) or \
           (self._override and (self._current_temp < (self._overtemp - self._threshold))) and \
           (self._time_since_last > self._min_lag):

           time_needed: int = self._current_temp - dtemp

           if self._override:
               time_needed = self._current_temp - self._overtemp

           self.set_runtime(time_needed)
           self.set_heater_on(True)
            
           return True

        else:
            self.set_heater_on(False)

        return False

    def set_current_temp(self, temp: int):
        self._current_temp = temp
    
    def set_threshold_diff(self, delta: int):
        self._threshold = delta

    def set_time_since_last_run(self, minutes: int):
        self._time_since_last = minutes

    def set_min_lag(self, minutes: int):
        self._min_lag = minutes

    def set_override(self, value: bool):
        self._override = bool(value)

    def set_over_temperature(self, temp: int):
        self._overtemp = temp

    def set_period(self, period: P):
        self._period = period

    def set_day(self, day: D):
        self._day = day

    def set_runtime(self, minutes: int):
        self._runtime = minutes

    def set_heater_on(self, on: bool):
        self._heater_on = on

    # This isn't really needed
    def set_setting(self, period: P, day: D, temp: int):
        self._settings[(period, day)] = temp

    # helper methods to make it more testable
    @property
    def heater_on(self):
        return self._heater_on

    @property
    def desired_temp(self):
        return self._settings[(self._period, self._day)]

# ==============================================================

thermo = Themostat()

thermo.set_setting(Period.morning, Day.weekday, 69)
thermo.set_period(Period.morning)
thermo.set_day(Day.weekday)

# clause a
thermo.set_current_temp(63)
thermo.set_threshold_diff(5)

# clause b
thermo.set_override(True)

# clause c
thermo.set_over_temperature(70)

# clause d
thermo.set_min_lag(10)
thermo.set_time_since_last_run(12)

# the test
thermo.turn_heat_on(Period.morning, Day.weekday)

print(thermo.heater_on)

# ==============================================================

thermo.set_current_temp(63)
thermo.set_threshold_diff(5)
thermo.set_override(True)
thermo.set_over_temperature(65)
thermo.set_min_lag(10)
thermo.set_time_since_last_run(12)

print(thermo.heater_on)

thermo.set_current_temp(66)
thermo.set_threshold_diff(5)
thermo.set_override(True)
thermo.set_over_temperature(65)
thermo.set_min_lag(10)
thermo.set_time_since_last_run(12)

print(thermo.heater_on)


thermo.set_current_temp(66)
thermo.set_threshold_diff(5)
thermo.set_override(True)
thermo.set_over_temperature(72)
thermo.set_min_lag(10)
thermo.set_time_since_last_run(12)

print(thermo.heater_on)

thermo.set_current_temp(66)
thermo.set_threshold_diff(5)
thermo.set_override(False)
thermo.set_over_temperature(70)
thermo.set_min_lag(10)
thermo.set_time_since_last_run(12)

print(thermo.heater_on)


thermo.set_current_temp(63)
thermo.set_threshold_diff(5)
thermo.set_override(True)
thermo.set_over_temperature(70)
thermo.set_min_lag(10)
thermo.set_time_since_last_run(12)

print(thermo.heater_on)

thermo.set_current_temp(63)
thermo.set_threshold_diff(5)
thermo.set_override(True)
thermo.set_over_temperature(70)
thermo.set_min_lag(10)
thermo.set_time_since_last_run(8)

print(thermo.heater_on)


# page 213
clause_a = lambda T: T._current_temp < (T.desired_temp - T._threshold)
clause_b = lambda T: T._override
clause_c = lambda T: T._current_temp < (T._overtemp - T._threshold)
clause_d = lambda T: T._time_since_last > T._min_lag


