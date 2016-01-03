import curses, os

class guiMc(object):
  pos = 0
  winvheight = 3
  winvwidth = 0
  winlheight = 0
  winlwidth = 0
  maxy = None
  maxx = None
  color = {}
  screen = None

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
    # init screen size
    self.maxy,self.maxx = self.screen.getmaxyx()
    self.winlheight = self.maxy - self.winvheight
    self.winlwidth = self.winvwidth = self.maxx/2

  def win1v(self):
    begin_x = 0; begin_y = 0
    height = self.winvheight; width = self.winvwidth
    w1v = self.screen.subwin(height, width, begin_y, begin_x)
    w1v.bkgdset(' ',self.color["basic"])
    w1v.border()

  def win1l(self):
    begin_x = 0; begin_y = self.winvheight
    height = self.winlheight; width = self.winlwidth
    w1l = self.screen.subwin(height, width, begin_y, begin_x)
    w1l.bkgdset(' ',self.color["basic"])
    w1l.border()

  def win2v(self):
    begin_x = self.maxx/2; begin_y = 0
    height = self.winvheight; width = self.winvwidth
    w2v = self.screen.subwin(height, width, begin_y, begin_x)
    w2v.bkgdset(' ',self.color["basic"])
    w2v.border()

  def win2l(self):
    begin_x = self.maxx/2; begin_y = self.winvheight
    height = self.winlheight; width = self.winlwidth
    w2l = self.screen.subwin(height, width, begin_y, begin_x)
    w2l.bkgdset(' ',self.color["basic"])
    w2l.border()

  def show(self):
    self.win1v()
    self.win1l()
    self.win2v()
    self.win2l()
    self.screen.keypad(1)
    x = self.screen.getch() # Gets user input

  def cleanup(self):
    curses.endwin() #VITAL! This closes out the menu system and returns you to the bash prompt.
    os.system('clear')
