# An simplified ANSI screen code class to make the display of things... pretty.

class ANSI():
    """Responsibility: To provide quick access to ANSI screen control codes,
    and possibly provide some methods for navigating around the screen or
    changing colors. 
    
    Attributes:
        BLACK, WHITE, RED, YELLOW, GREEN, CYAN, BLUE, MAGENTA,
        BOLD, NORMAL, DIM, DEFAULT       : Color attribute codes.
        CLEAR, HOME  : Screen clearing and home cursor position.
        
    Behaviors:
        clear_home(self)                            :   Clears the screen and homes the cursor.
        pos_xy(self, x, y, execute)                 :   Sets cursor position to x and y.
        palette_color(self, fore_index, back_index) :   Sets the colors to predefined palette colors.   
        rgb_fore_color(self, r, g, b)               :   Sets the foreground color to a RGB-mixed color.
        rgb_back_color(self, r, g, b)               :   Sets the background color to a RGB-mixed color.
        up(self, value, execute)                    :   Move the cursor up [value] number of spaces.
        down(self, value, execute)                  :   Move the cursor down [value] number of spaces.
        right(self, value, execute)                 :   Move the cursor right [value] number of spaces.
        left(self, value, execute)                  :   Move the cursor left [value] number of spaces.

    """

    
    def __init__(self):
        """Initialize the class. This method will define the attributes described above."""
        self.BLACK      = chr(27)+"[30m"
        self.WHITE      = chr(27)+"[37m"
        self.RED        = chr(27)+"[31m"
        self.YELLOW     = chr(27)+"[33m"
        self.GREEN      = chr(27)+"[32m"
        self.CYAN       = chr(27)+"[36m"
        self.BLUE       = chr(27)+"[34m"
        self.MAGENTA    = chr(27)+"[35m"

        self.BK_BLACK   = chr(27)+"[40m"
        self.BK_WHITE   = chr(27)+"[47m"
        self.BK_RED     = chr(27)+"[41m"
        self.BK_YELLOW  = chr(27)+"[43m"
        self.BK_GREEN   = chr(27)+"[42m"
        self.BK_CYAN    = chr(27)+"[46m"
        self.BK_BLUE    = chr(27)+"[44m"
        self.BK_MAGENTA = chr(27)+"[45m"

        self.NORMAL     = chr(27)+"[0m"
        self.BOLD       = chr(27)+"[1m"
        self.DIM        = chr(27)+"[2m"
        self.ITALIC     = chr(27)+"[3m"
        self.UNDER      = chr(27)+"[4m"

        self.UP         = chr(27)+"[A"
        self.DOWN       = chr(27)+"[B"           
        self.RIGHT      = chr(27)+"[C" 
        self.LEFT       = chr(27)+"[D"

        self.DEFAULT    = chr(27)+"[39;49m"
        self.RESET      = chr(27)+"[0"
        self.CLEAR      = chr(27)+"[2J"
        self.HOME       = chr(27)+"[H"
        self.CLEARHOME  = self.CLEAR + self.HOME

    def palette_color(self, fore_index, back_index, execute = False):
        """Returns a sequence to set the color to one of 256 predefinded colors indexed 0 through 255.
        Parameters:
            self       : An instance of the ANSI class. (Implied, unused.)
            fore_index : The palette index number for the foreground color. (0-255)
            back_index : The palette index number for the background color. (0-255)
            execute    : True = Output commans directly to output device (terminal).
                         False (default) = Return a code string for use elsewhere.
        """
        val = f"\33[38;5;{fore_index}m" + f"\33[48;5;{back_index}m"
        if execute:
            print(val,end='')
            return
        else:
            return val


    def rgb_fore_color(self, r, g, b, execute = False):
        """Returns a sequence to set the foreground color to an RGB value specified by the user.
        Parameters:
            self    : An instance of the ANSI class. (Implied, unused.)
            r, g, b : The red, green, and blue values to mix the color. (0-255)
            execute : True = Output commans directly to output device (terminal).
                      False (default) = Return a code string for use elsewhere.
        """
        val = f"\33[38;2;{r};{g};{b}m"
        if execute:
            print(val,end='')
            return
        else:
            return val


    def rgb_back_color(self, r, g, b, execute = False):
        """Returns a sequence to set the background color to an RGB value specified by the user.
        Parameters:
            self    : An instance of the ANSI class. (Implied, unused.)
            r, g, b : The red, green, and blue values to mix the color. (0-255)
            execute : True = Output commans directly to output device (terminal).
                      False (default) = Return a code string for use elsewhere.
        """
        val = f"\33[38;2;{r};{g};{b}m"
        if execute:
            print(val,end='')
            return
        else:
            return val


    def clear_home(self):
        """Issues a CLEAR SCREEN and HOME command to the terminal.
        Parameters:
            self    : An instance of the ANSI class. (Implied)
        """
        print(self.CLEARHOME,end='')


    def pos_xy(self, x, y, execute = True):
        """Issues a cursor positioning command to the terminal, or returns and ANSI code for such.
        Parameters:
            self    : An instance of the ANSI class. (Implied, unused.)
            x, y    : The X and Y coordinates on the screen. 0,0 is top left.
            execute : True (default) = Output command directly to output (terminal).
                      False = Return a code string for use elsewhere.
        """
        val = f"\33[{y};{x}H"
        if execute:
            print(val,end='')
            return
        else:
            return val


    def up(self, value, execute = False):
        """Moves the cursor up [value] number of spaces, or returns an ANSI code for such.
        Parameters:
            self    : An instance of the ANSI class. (Implied, Unused)                    
            value   : The specified number of spaces to move.
            execute : True = Output command directly to output (terminal).
                      False (default) = Return a code string for use elsewhere.
        """
        out = f"\33[{value}A"
        if execute:
            print(out,end='')
            return
        else:
            return out


    def down(self, value, execute = False):
        """Moves the cursor down [value] number of spaces, or returns an ANSI code for such.
        Parameters:
            self    : An instance of the ANSI class. (Implied, Unused)
            value   : The specified number of spaces to move.
            execute : True = Output command directly to output (terminal).
                      False (default) = Return a code string for use elsewhere.
        """
        out = f"\33[{value}B"
        if execute:
            print(out,end='')
            return
        else:
            return out


    def right(self, value, execute = False):
        """Moves the cursor right [value] number of spaces, or returns an ANSI code for such.
        Parameters:
            self    : An instance of the ANSI class. (Implied, Unused)
            value   : The specified number of spaces to move.
            execute : True = Output command directly to output (terminal).
                      False (default) = Return a code string for use elsewhere.
        """
        out = f"\33[{value}C"
        if execute:
            print(out,end='')
            return
        else:
            return out


    def left(self, value, execute = False):
        """Moves the cursor left [value] number of spaces, or returns an ANSI code for such.
        Parameters:
            self    : An instance of the ANSI class. (Implied, Unused)
            value   : The specified number of spaces to move.
            execute : True = Output command directly to output (terminal).
                      False (default) = Return a code string for use elsewhere.
        """
        out = f"\33[{value}D"
        if execute:
            print(out,end='')
            return
        else:
            return out
    