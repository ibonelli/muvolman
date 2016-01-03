import curses, os

class guiVolumes(object):
  pos = 0
  winheight = 20
  winwidth = 60
  color = {}

  def __init__(self):
    # init ncurses
    self.screen = curses.initscr() #initializes a new window for capturing key presses
    curses.noecho() # Disables automatic echoing of key presses (prevents program from input each key twice)
    curses.cbreak() # Disables line buffering (runs each key as it is pressed rather than waiting for the return key to pressed)
    curses.start_color() # Lets you use colors when highlighting selected menu option
    # init color
    self.color["normal"] = curses.A_NORMAL #n is the coloring for a non highlighted menu option
    curses.init_pair(1,curses.COLOR_WHITE,curses.COLOR_BLUE) # Sets up color pair #1
    self.color["basic"] = curses.color_pair(1)
    curses.init_pair(2,curses.COLOR_BLACK,curses.COLOR_CYAN) # Sets up color pair #2
    self.color["highlighted"] = curses.color_pair(2)

  def win(self):
    begin_x = 1; begin_y = 1
    height = self.winheight; width = self.winwidth
    w1v = self.screen.subwin(height, width, begin_y, begin_x)
    w1v.bkgdset(' ',self.color["basic"])
    w1v.border()

  def show(self):
    self.win()
    self.screen.keypad(1)
    x = self.screen.getch() # Gets user input

  def cleanup(self):
    curses.endwin() #VITAL! This closes out the menu system and returns you to the bash prompt.
    os.system('clear')
