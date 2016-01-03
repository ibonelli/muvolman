import curses, os

class cMenu(object):
  color = {}
  menu = []
  pos = 1
  begin_x = 1
  begin_y = 1
  screen = None
  def __init__(self):
    self.screen = curses.initscr() #initializes a new window for capturing key presses
    curses.noecho() # Disables automatic echoing of key presses (prevents program from input each key twice)
    curses.cbreak() # Disables line buffering (runs each key as it is pressed rather than waiting for the return key to pressed)
    curses.start_color() # Lets you use colors when highlighting selected menu option
    # Setting up colors to us
    self.color["normal"] = curses.A_NORMAL
    self.color["bold"] = curses.A_BOLD
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    self.color["highlighted"] = curses.color_pair(1)
  def add_menu_entry(self,option,cmd):
    self.menu.append((option,cmd))
  def show(self):
    self.screen.keypad(1)
    stay = True
    while stay:
      self.drawmenu()
      c = self.screen.getch() # Gets user input
      if(c==curses.KEY_UP):
        self.upKey()
      elif(c==curses.KEY_DOWN):
        self.downKey()
      elif(c==ord('\n')):
        stay = False
    return self.menu[self.pos-1][1]
  def drawmenu(self):
    i=0
    self.screen.bkgdset(' ',self.color["normal"])
    self.screen.addstr(i+1, 1, "menu:", self.color["bold"])
    i+=1
    for opt,cmd in self.menu:
      if self.pos==i:
        usecolor = self.color["highlighted"]
      else:
        usecolor = self.color["normal"]
      self.screen.addstr(i+1, 4, opt, usecolor)
      i+=1
  def upKey(self):
      if self.pos > 1:
          self.pos -= 1
      else:
          self.pos = len(self.menu)
  def downKey(self):
      if self.pos < len(self.menu):
          self.pos += 1
      else:
          self.pos = 1
  def cleanup(self):
    curses.endwin() #VITAL! This closes out the menu system and returns you to the bash prompt.
    os.system('clear')
