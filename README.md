# Raspberry Pi PWM cooling fan controller

## Hardware build
TODO

## Docker Compose file
This Compose file assumes you're running in Swarm mode and you want this service to run on all of your Pi's.

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
