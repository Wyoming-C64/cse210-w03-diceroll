import random
from time import sleep

# 1) Add the class declaration. Use the following class comment.
class Die:
    """A small cube with a different number of spots on each of its six sides.

    The responsibility of Die is to keep track of the side facing up and calculate the points for 
    it.
   
    Attributes:
        value (int): The number of spots on the side facing up.
        points (int): The number of points the die is worth.
        x, y (int): The screen X and Y coordinates where the die will display.
    """

# 2) Create the class constructor. Use the following method comment.
    def __init__(self, param_x = 0, param_y = 0):
        """Constructs a new instance of Die with a value and points attribute. 
        Sets x,y to passed value, or 0,0 if none set.

        Args:
            self (Die): An instance of Die.
        """
        self.value = 0
        self.points = 0
        self.x = param_x
        self.y = param_y

# 3) Create the roll(self) method. Use the following method comment.
    def roll(self):
        """Generates a new random value and calculates the points.
        
        Args:
            self (Die): An instance of Die.
        """
        self.value = random.randint(1,6)
        if self.value == 1:
            self.points = 100
        elif self.value == 5:
            self.points = 50
        else:
            self.points = 0


    def display(self):
        SCREEN_HOME = chr(27) + "[H"
        FACE_LINE_HOME = chr(27) + "[7D"
        DOWN = chr(27) + "[1B"

        RVS_YELLOW = chr(27)+"[48;5;226m"+chr(27)+"[38;5;0m"
        
        NORMAL = chr(27)+"[38;5;248m"+chr(27)+"[48;5;0m"
        RVS_NORMAL = chr(27)+"[48;5;245m"+chr(27)+"[38;5;0m"
        
        RVS_WHITE = chr(27)+"[48;5;255m"+chr(27)+"[38;5;0m"

        face = [ '',
            # 1
            RVS_YELLOW +
            '       ' + FACE_LINE_HOME + DOWN +
            '   ■   ' + FACE_LINE_HOME + DOWN +
            '       ' + FACE_LINE_HOME + DOWN + NORMAL,
            # 2
            RVS_NORMAL +
            ' ■     ' + FACE_LINE_HOME + DOWN +
            '       ' + FACE_LINE_HOME + DOWN +
            '     ■ ' + FACE_LINE_HOME + DOWN + NORMAL,
            # 3
            RVS_NORMAL +
            ' ■     ' + FACE_LINE_HOME + DOWN +
            '   ■   ' + FACE_LINE_HOME + DOWN +
            '     ■ ' + FACE_LINE_HOME + DOWN + NORMAL,
            # 4
            RVS_NORMAL +
            ' ■   ■ ' + FACE_LINE_HOME + DOWN +
            '       ' + FACE_LINE_HOME + DOWN +
            ' ■   ■ ' + FACE_LINE_HOME + DOWN + NORMAL,
            # 5
            RVS_WHITE +
            ' ■   ■ ' + FACE_LINE_HOME + DOWN +
            '   ■   ' + FACE_LINE_HOME + DOWN +
            ' ■   ■ ' + FACE_LINE_HOME + DOWN + NORMAL,
            # 6
            RVS_NORMAL +
            ' ■   ■ ' + FACE_LINE_HOME + DOWN +
            ' ■   ■ ' + FACE_LINE_HOME + DOWN +
            ' ■   ■ ' + FACE_LINE_HOME + DOWN + NORMAL,
            ]
        
        print(chr(27)+f"[{self.y};{self.x}H",end='')
        print(face[self.value],end='')
        print(chr(27)+"[0;37m")
        return


