# Pomodoro Timer

## Overview

A simple command-line **Pomodoro Timer** to boost productivity by following the Porodoro Technique:
- **25-minute work session**
- **5-minute short breaks**
- **4 cycles by default**

## Installation

No external dependencies needed - just Python!

## How to use

1. Clone the repository:
    ```sh
    git clone https://github.com/Aditya15267/pomodoro-timer.git
2. Run with default settings (25-minute work, 5-minute break, 4 cycles):
    ```sh
    python pomodoro_timer.py
3. Customise work time, break time, and cycles:
    ```sh
    python pomodoro_timer.py -w 30 -b 10 -c 3
    ```
    Here:
    - ```-w 30``` -> Work for **30 minutes**
    - ```-b 10``` -> Break for **10 minutes**
    - ```-c 3``` -> Run **3 Pomodoro cycles**

## Example Output
```
Cycle 1: Time to work! (25 minutes)
Break Time! (5 minutes)
...
Pomodoro session completed!
```