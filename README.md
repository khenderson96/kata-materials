# Augustwenty Submarine Adventure

This collection of scripts allows a user to navigate the seas in their very own submarine. To get started, follow the steps below.

1. install python3
2. using your command line, navigate to the top level of this project directory
3. create a virtual environment:  
```python3 -m venv <yourvenvname>```
4. activate your virtual environment:
    - windows:  ```<yourvenvname>/Scripts/Activate```
    - unix:  ```source <yourvenvname>/bin/activate```
4. install requirements:  
```pip install -r requirements.txt```
5. execute ```python a20_demo -h``` to see options. For example, run ```python a20_demo -e 2 -a``` to run example 2 with animation enabled.

## Contents:
- Options
- Testing
- Questions and Considerations
- Architectural Reasoning and Analysis
- Developmental timeline
- Future improvements
- Easter Egg

## Options
The script can be executed in various modes
```
  -h, --help            show this help message and exit
  -e, --exercise {1,2}  The exercise number to run (must be integer 1-2).
  -t, --test_mode       Enable test; use example inputs and compare outputs (optional).
  -a, --animation       Enable antimation (optional).
```

## Testing
Each script in the repository can be executed as a standalone module to validate class functionality and demonstrate functions.

```sub.py```: prints the position of the submarine after a series of simple, easily verifiable moves.  

```animation.py```: demonstrates simple animation without relying on ```sub.py``` or file parsing logic.  

```a20_demo -e X -t```: use rules from exercise X to calculate a position using the example input and compare calculated position to example result for verification.

## Questions and Considerations
I considered various approaches both before and throughout the development processs.

Is it more important to demonstrate a highly optimized but sparcely featured product compared to a more well rounded product?

Should the animation be interleaved with the file parsing, or executed as a standalone option? A standalone option precludes the ability for multithreading, but is preformance important?

## Architectural Reasoning and Analysis

While I considered writing this solution in C, a highly preformant, low-level language, the cost-benefit analysis did not lean in favor of this approach. 

Python is not as temporally or spacially efficient as a compiled language like C/C++/C# etc, but the requirements imposed no constraints on execution speed, algorithmic time complexity, memory use, etc, so I instead prioritized simplicity, readability, time-to-MVP, and bonus features.

Though I have used C daily for several years, using C in this application would have easily doubled the time to MVP, making additional quality-of-life features like animations and command line arguments into a much longer stretch goal.

Given these considerations, Python is an appropriate choice for several key reasons:
- Pace of development: the core logic and test cases were written within 45 minutes and contained in a single file of 75 lines (⏰🟰💵)
- Ease in opening files, parsing strings, parsing command line arguments, etc
- Familiarity with OpenCV for simple animation, argparse for options, etc.

A final factor in my choice to use python is related to my lack of knowledge about the ultimate goal/third exercise. It is difficult to choose the optimal tool for a job if you do not know the requirements. Though I am sacrificing performance, the choice to use python helps ensure that the third exercise will go smoothly.

## Developmental timeline
1. Read instructions, consider options
2. implement core logic for Exercise 1 & 2 in parallel via ```sub.py```, test as standalone module
3. implement file parsing in ```sub.py```, first using the example solution (see ```example.txt```)
3. implement ```__main__.py``` to utilize common python design patterns, move file parsing into main application
4. implement  ```sys.argv``` command line options inside ```__main__.py``` for switching input file and exercise number 
5. implement ```animation.py```, test as standalone module
6. implement ```animation.py``` in ```__main__.py```
7. implement ```argparse``` in ```__main__.py``` to increase accessibility and simplify parsing of command line arguments
8. refinement, type hints, error catching, further documentation
9. easter egg 

## Future Improvements
- implement different exercises as subclasses rather than current approach
- change the submarine animation to be a rectangle so it can better show rotation/directionality
- show aim in the animation
- parallelization? use an additional thread for animation?

## BEWARE! 
If you hung around this long, then you deserve a kind warning. The seas are unpredictable, and you may get lost if you run this script a few times...

There is an easter egg which could be unpleasant to those suffering epileptic seizures.