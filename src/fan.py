#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import pigpio

PWM_PIN = int(os.getenv("PWM_PIN", 18))
PWM_FREQ = 20000
WAIT_TIME = 5
FAN_OFF_TEMP = 58  # Turn off fan below this speed
FAN_START_TEMP = 60  # Lowest speed
FAN_FULL_TEMP = 80  # 100% speed
TEMP_AVG_CYCLES = 5

class CPUTemp:
    """Manage averaging of CPU temperature."""
    def __init__(self, avg_cycles):
        self._cpu = [ self._get_cpu_temp() ] * avg_cycles

    @property
    def cpu(self):
        self._cpu = self._cpu[1:] + [ self._get_cpu_temp() ]
        return round(sum(self._cpu) / len(self._cpu), 2)

    @staticmethod
    def _get_cpu_temp():
        """Get the CPU core temperature in °C"""
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            return float(f.read()) / 1000


def set_duty(duty_cycle_percent):
    """
    Set the PWM duty cycle between 0 and 100%
    where 0% is off, and 100% is fully on
    """
    print("Set duty to", duty_cycle_percent)
    pin.set_PWM_dutycycle(PWM_PIN, duty_cycle_percent)


def calc_duty(temperature):
    """
    Perform linear interpolation between temperature limits
    to get to the fan PWM duty cycle.
    """
    return 50  # TODO


pin = pigpio.pi()
pin.set_PWM_frequency(PWM_PIN, PWM_FREQ)
pin.set_PWM_range(PWM_PIN, 100)

try:
    print("Started fan PWM control on pin", PWM_PIN)
    temp = CPUTemp(TEMP_AVG_CYCLES)
    while True:
        cpu_temp = temp.cpu
        print("CPU temp:", cpu_temp)
        if cpu_temp < FAN_OFF_TEMP:
            set_duty(0)
        elif cpu_temp >= FAN_START_TEMP:
            set_duty(calc_duty(cpu_temp))
        time.sleep(WAIT_TIME)
except Exception as e:
    pin.stop()
    raise
