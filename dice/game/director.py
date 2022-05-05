from game.die import Die
 
class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        dice (List[Die]): A list of Die instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.dice = []
        self.is_playing = True
        self.score = 0
        self.total_score = 0
        self.num_rolls = 0

        for i in range(5):
            # Set the terminal X coordinate for the die to be displayed
            # (1, 11, 21...)
            x_coord = (i * 10)+1
            die = Die(x_coord, 0)
            self.dice.append(die)

    def show_title(self):
        """Shows a title screen and displays the rules of the game.
        
        Args:
            self (Director): an instance of Director.
        """
        print("\33[2J\33[H")    # Clear/Home Screen
        print("DICE\n")
        print("The rules are simple. Roll the dice. Count the 1s and 5s. Each 1 is worth")
        print("100 points, each 5 is worth 50 points. As long as you roll at least a 1")
        print("or a 5 you can keep playing and add to your score.\n")
        print("If you do not roll any 1s or 5s, the game is over.\n")


    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        self.show_title()

        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

        self.end_game()


    def end_game(self):
        """Provides a clean exit to the game by printing the final score and saying goodbye.
        
        Args:
            self (Director): an instance of Director.
        """
        print()
        if self.num_rolls == 0: # What? Quitting without even trying?!
            print("Making no attempt keeps you safe from failure... It also keeps you safe from success.\n")
            return
        elif self.num_rolls == 1 and self.score == 0: # Zero on the first roll? Darn it.
            print("No score on the first roll. Well, isn't that rotten luck?")
        elif self.score == 0:  # Otherwise, player did not roll a 1 or a 5... 
            print("Well, shoot... You didn't roll a 1 or a 5. Your streak is over.")
        else:   # Or the player must have chosen to quit.
            print("You know there's no risk to keep rolling, right? Oh well...")

        rolls = "roll" if self.num_rolls == 1 else "rolls"

        print(f"You achieved a final score of {self.total_score} in {self.num_rolls} {rolls}.\n")
        print("Thank you for playing! Goodbye!\n")


    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        valid_input = False
        while not valid_input:
            roll_dice = input("Roll dice? [y/n]: ").lower()
            valid_input = roll_dice in ['y','n']
            if not valid_input:
                print("I'm sorry, please confine your response to 'y' or 'n'.\n")
        self.is_playing = (roll_dice == "y")

       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        # Bugfix: Round score needs to be reset before rolling the dice again.
        self.score = 0

        for i in range(len(self.dice)):
            die = self.dice[i]
            die.roll()
            self.score += die.points 
        self.total_score += self.score
        # Increase the number of rolls made.
        self.num_rolls += 1


    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        values = ""
        for i in range(len(self.dice)):
            die = self.dice[i]
            values += f"{die.value} "

        print(chr(27)+"[2J"+chr(27)+"[H",end="")
        for i in range(len(self.dice)):
            self.dice[i].display()
        print("\n")
        print(f"Score this round:\t{self.score}".expandtabs(25))
        print(f"Your total score is:\t{self.total_score}\n".expandtabs(25))
        self.is_playing = (self.score > 0)