# Raspberry Pi PWM cooling fan controller

## Hardware build
TODO

## Prerequisites
Firstly, you need [pigpio](http://abyz.me.uk/rpi/pigpio/index.html) running as a daemon on your Pi. This service exposes port 8888 that other services can then use to get low-level access to the Raspberry Pi's GPIO pins.

The easiest way to set up pigpio, if you are not already running it, is using [corbosman/node-red-gpiod](https://github.com/corbosman/node-red-gpiod)'s Docker image.

```
docker run -d -p 8888:8888 --privileged --name gpiod corbosman/pigpiod -s 2
```

`-s 2` is used by pigpio so that we can run the fan PWM at 20 kHz, mostly above human hearing range. Any lower and you will start to hear an audible hum from the fan motor coils.

Unfortunately Docker Swarm mode does not yet support the "privileged" directive, which pigpio needs to be able to get access to GPIO pins. You will need to run this command on each of your Pi's where you want to run the fan controller.

## Fan control

```
docker run -d .... TODO
```

If you are running in Swarm mode, add the following to your docker-compose.yaml file:

```
TODO
```

## Goals of the project
I run a cluster of Raspberry Pi 4B's at home, ostensibly to run Home Assistant for my [home automation projects](TODO), but mostly to learn about running my own 'bare metal' hardware and high availability services.

The CPU's in my Pi's have heatsinks and the cases are relatively well ventilated, but sometimes they run a bit hot (70+ °C) and so they need some active help. The fans that I have can be plugged in to the 5 V or 3V rails, but they are noisy, so I'd prefer that they didn't run at all.

**Goals**
1. Run as quietly as possible, ideally the fan should not run at all
2. The fewer system resources used the better: Small runtime, fast code, hardware PWM
3. Run as a Docker Service on each of the Pi's, let Swarm manage them

## Acknowledgements
- [Instructables: PWM Regulated Fan Based on CPU Temperature for Raspberry Pi](https://www.instructables.com/id/PWM-Regulated-Fan-Based-on-CPU-Temperature-for-Ras/)
