import time
import argparse

def pomodoro_timer(work_duration=25, short_break=5, cycles=2):
    """Simple Pomodoro Timer"""
    for cycle in range(1, cycles + 1):
        print(f"\nCycle {cycle}: Time to work! ({work_duration} minutes)")
        time.sleep(work_duration * 60) # convert minutes to seconds

        if cycle < cycles:
            print(f"Break Time! ({short_break} minutes)")
            time.sleep(short_break * 60)

    print("\nPomodoro session completed!")

if __name__ == "__main__":
    parse = argparse.ArgumentParser(description="Pomodoro Timer Script")
    parse.add_argument("-w", "--work", type=int, default=25, help="Work duration in minutes")
    parse.add_argument("-b", "--break_", type=int, default=5, help="Short break duration in minutes")
    parse.add_argument("-c", "--cycles", type=int, default=2, help="Number of work cycles")

    args = parse.parse_args()
    pomodoro_timer(args.work, args.break_, args.cycles)