from sub import Submarine
import sys
import argparse
import random

"""
options:
  -h, --help            show this help message and exit
  -e, --exercise {1,2}  The exercise number to run (must be integer 1-2).
  -t, --test_mode       Enable test mode; use example inputs and compare outputs (optional).
  -a, --animation       Enable antimation (optional).
"""

def get_args():
    parser = argparse.ArgumentParser(
    description="Navigate a submarine through exercises 1 and 2, and optionally run tests and/or run animations.")

    # required exercise flag followed by an integer 1 or 2
    parser.add_argument(
        '-e', '--exercise',
        type=int,
        choices=[1, 2],
        required=True,
        help='The exercise number to run (must be integer 1-2).'
    )

    # optional flag for enabling test mode 
    parser.add_argument(
        '-t', '--test_mode',
        action='store_true',
        help='Enable test mode; use example inputs and compare outputs (optional).'
    )

    # optional boolean flag for enabling animation
    parser.add_argument(
        '-a', '--animation',
        action='store_true',
        help='Enable antimation (optional).'
    )

    return parser.parse_args()
   
if __name__ == "__main__":
    args = get_args()
    sub = Submarine(args.exercise)
    positions = [] # log of positions for animation

    print(f"Submarine Exercise {args.exercise}")

    # get file name, open it, and read each line
    input_file = 'input.txt' if not args.test_mode else 'example.txt'
    with open(input_file, 'r') as f:
        for line in f:
            # split input line at space to get command name and value
            name, value = line.strip().split(' ')
            
            # call the appropriate method on the submarine object
            if name == 'forward':
                sub.forward(int(value))
            elif name == 'up':
                sub.up(int(value))
            elif name == 'down':
                sub.down(int(value))
            else:
                # shouldn't happen, but just in case. Note: would be more eff
                print(f"Invalid command: {name}. Must be one of 'forward', 'up', or 'down'.")
                sys.exit(1)

            print(f"{name[0].upper()}, {value} -> {sub}")
            # log position for future optional animation
            positions.append((sub.x, sub.y, getattr(sub, 'aim', None)))

    # print examlpe results if in test mode
    if input_file == 'example.txt':
        if args.exercise == 1:
            x, y = 15, 10
            print(f"\nEx1 Expected Position: (x:{x}, y:{y})")
            print(f"Ex1 Expected Result: {x*y}\n")
        elif args.exercise == 2:
            x, y, a = 15, 60, 10
            print(f"\nEx2 Expected Position: (x:{x}, y:{y}, a:{a})")
            print(f"Ex2 Expected Result: {x*y}\n")

    print(f"Final Position: {sub}")
    print(f"Final Result: {sub.x * sub.y}")

    # Run animation if enabled
    if args.animation:
        try:
            from animation import *
        except ImportError:
            print("Error importing animation.py... Skipping animation.")
            sys.exit(0)

        # add an element of chance to make it fun :)
        if random.random() > 0.9:
            run_crazy_animation(positions)
        else:
            run_animation(positions)