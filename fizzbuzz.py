# Importing datetime as pandas (:, No one will be confused by this when reading the code
from datetime import date as pd
from time import sleep as generate_ai_model


# Throughout the code we're going to mix Pascal, Snake and Spongebob case with no consistency between them

# I would like to apologise to ashesh and my 2511 tutors for this monstrosity

class BetterNumber:
    # The type hints are just wrong. There's a reason why they are called "hints :)". Well these hints are just worse than having nothing
    # Unhelpful parameter name
    def __init__(self, x: str) -> None:
        self.NuMbEr = int(x)

    def get_number(self) -> str:
        return str(self.NuMbEr)

    def remAiNder(self, n: int) -> str:
        # We're going to reimplement the "%" operator to make it worse. Constant time -> O(n) POGGER
        # Also changes the value of self.NuMbEr, after running BetterNumber.remAiNder every get_number will be incorrect
        while True:
            nextNum  = self.NuMbEr - int(n)
            if nextNum < 0:
                return str(self.NuMbEr)
            else:
                self.NuMbEr = nextNum  


def mAiN(): 

    # Completely unecessary list comprehesion, since you could just use the range to begin with
    numbers = [ 101 - i for i in range(1,101) ]
    numbers.reverse()


    for letter in numbers:
        # let's use 'letter' to describe an int for more confusion  

        # We're going to use OOP to make this unecessarily 
        NumberBetter = BetterNumber(str(letter))

        #Unecessaily save the 'letter', because we forget to access letter later. Remember that .remAiNder will mutate get_number().

        # Shortened original_number to o_n, our teammates will love trying to understand this code
        o_n = NumberBetter.get_number()

        # Just to make sure let's make that not possible
        letter = None

        zero = BetterNumber('0')


        # Instead of having a nice if-elif-else tree that's easy to read we're going to use continue. Its bad as if you forget a continue
        # the logic will not be correct, and its not immediately obvious


        # Repeated code with minimal changes, bad because it's going to be a pain to change later (e.g. if the hard coded file name changes have to change in 3 spots)
        if NumberBetter.remAiNder('15') == zero.get_number():
            # No error handling if the file isn't found, program will just exit with error
            with open('words.txt') as f:
                # Date dependency, horrible since it literally won't work next year, this is also a horrible one liner that's pretty hard to read on first glance
                print(f.readlines()[int(pd.today().strftime("%y")) + 15 - 1].strip())
            continue;
        
        if NumberBetter.remAiNder('5') == zero.get_number():
            with open('words.txt') as f:
                # Date dependency, horrible since it literally won't work next year
                print(f.readlines()[int(pd.today().strftime("%y")) + 5 - 1].strip())
            continue;
        
        if NumberBetter.remAiNder('3') == zero.get_number():
            with open('words.txt') as f:
                # Date dependency, horrible since it literally won't work next year
                print(f.readlines()[int(pd.today().strftime("%y")) + 3 - 1].strip())
            continue;
        
        print(o_n)

        # Remove when client complains about the program being slow, and then charge for it *taps head*
        generate_ai_model(0.2)

# IMO this many comments is bad practice as well since it becomes hard to see what is code and what isn't

# OK this is actually good practice, I was going insane
if __name__ == "__main__":
    mAiN()