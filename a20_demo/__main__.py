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

    dict = {}
    with open('scanner-data.json', 'r') as f:
        import json
        dict = json.load(f)
        # print(f"\nScanner Data: {dict}")

    # for k, v in dict.items():
    #     print(f"{k}: {v}")

    positions2 = [(p[0], p[1]) for p in positions if len(p) > 2]  # filter out aim values for exercise 1
    # print(positions2)

    scanned_positions = {}
    for k,v in dict.items():
        for p in positions2:
            if k == f"({p[0]},{p[1]})":
                print(f"Match found for position {p}: {v}")
                scanned_positions[p] = v

    # TODO: use filter() to remove duplicates (if needed)
    # print(f"Scanned Positions: {scanned_positions}")

    map = {}
    for k,v in scanned_positions.items():
        for i in range(len(v)):
            x, y = k
            if i == 0:                
                map[(x-1, y-1)] = v[i]  
            elif i == 1:
                map[(x, y-1)] = v[i]    
            elif i == 2:
                map[(x+1, y-1)] = v[i]                
            elif i == 3:
                map[(x-1, y)] = v[i]                
            elif i == 4:
                map[(x, y)] = v[i]
            elif i == 5:
                map[(x+1, y)] = v[i]                
            elif i == 6:
                map[(x-1, y+1)] = v[i]
            elif i == 7:
                map[(x,y+1)] = v[i]
            elif i == 8:
                map[(x+1, y+1)] = v[i]
            else:
                pass

    max_x = max(map.keys(), key=lambda k: k[0])[0]
    max_y = max(map.keys(), key=lambda k: k[1])[1]

    print(f"Map Size: {max_x} x {max_y}")
    
    map_list = []
    for y in range(max_y+1):
        li = [' ' for  x in range(max_x+1)]
        map_list.append(li)

    # print(len(map_list), len(map_list[0]))

    for k, v in map.items():
        x, y = k
        if 0 <= x <= max_x and 0 <= y <= max_y:
            map_list[y][x] = v

    print("Map:")
    for row in map_list:
        print(" ".join(row))        

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
        if random.random() > 0.1:
            run_crazy_animation(positions)
        else:
            run_animation(positions)