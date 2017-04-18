# EXAM: Programming Basics

### Getting Started
 - Fork this repository under your own account
 - Clone the forked repository to your computer
 - Create a `.gitignore` file so generated files won't be committed
 - Commit your progress frequently and with descriptive commit messages
 - All your answers and solutions should go in this repository

### What can I use?
- You can use any resource online, but **please work individually**
- **Don't just copy-paste** your answers and solutions, use your own words instead.
- **Don't push your work** to GitHub until your mentor announces that the time is up


# Tasks
## 1-3. Complete the following tasks: (~90 mins)
- [Odd Average](oddavg/odd_avg.py)
- [Copy](copy/copy.py)
- [BlackJack](blackjack/black_jack.py)

### Acceptance criteria
The application is accepted if:
- The solution works according to specification [1p each]
- The solution follows [styleguide](https://google.github.io/styleguide/pyguide.html) [1p]
- Has proper error handling where the specification says it [1p each]
- Has the correct loops, methods, filters [1p each]
- The code is clean, without unnecessary repetition, and with descriptive names [1p each]
- You commit frequently with descriptive commit messages [1p]

## 4. Question time! (~10 mins) [4p]

### Name each building block of a method! [2p]

![anatomy](anatomy/anatomy_py.png)

#### Your answer:
[add your answer here]   
1:   calls the function
2:   name of the function
3:   argument, in his case it will be used in the 'for loop' as the second parameter of the range
4:   actual function that works and counts the total in this case
5:   variable, now it is set to zero
6:   end of the function, it stops the function and returns the total value
7:   new total variable, it has the value after the counting

### What is the constructor? When it is used? [2p]
#### Your answer:
class ClassName(object):
    def __(init)__(self):               <-- constructor
        self.variable = "some value"
        self.function()

The __init__ method is the constructor of the ClassName object and it instantly sets up its base values and/or class different methods, when it is instantiated later.
In this case the __init__ method sets up the self.variable to "some value" and calls the self.function() method.
