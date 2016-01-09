import curses, os
from dirtree import CurDir
from gui_fixedlist import guiFixedList

class guiVolumes(object):
  pos = 0
  winheight = 20
  winwidth = 60
  color = {}
  entries = []
  entriescnt = 0
  curdir = None
  view = None

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
    # init path
    self.curdir = os.getcwd()
    self.fillentries()
    self.view = guiFixedList(self.entries,(winheight-2,winwidth-2))

  def draw_win(self):
    begin_x = 1; begin_y = 1
    height = self.winheight; width = self.winwidth
    w1v = self.screen.subwin(height, width, begin_y, begin_x)
    w1v.bkgdset(' ',self.color["basic"])
    w1v.border()
    self.pos = self.view.get_view(self.pos)
    i=0
    for v in self.view:
      if self.pos==i:
        w1v.addstr(begin_y+i, begin_x, self.view[i], self.color["highlighted"])
      else:
        w1v.addstr(begin_y+i, begin_x, self.view[i], self.color["basic"])
      i+=1
    self.screen.addstr(begin_y+self.winheight, begin_x, "Para seleccionar presione \"S\"", self.color["normal"])

  def fillentries(self):
    self.entriescnt = 0
    mycurdir = CurDir(self.curdir)
    for d,ref in mycurdir.dirs:
      self.entries.append(stringFormat.getfstr(self.winwidth-2,d,"dir"))
      self.entriescnt+=1
    for f,size in mycurdir.files:
      self.entries.append(stringFormat.getfstr(self.winwidth-2,(f,size),"file"))
      self.entriescnt+=1

  def show(self):
    self.screen.keypad(1)
    stay = True
    self.draw_win()
    while stay:
      c = self.screen.getch() # Gets user input
      if(c==curses.KEY_UP):
        self.pos-=1
        self.draw_win()
      elif(c==curses.KEY_DOWN):
        self.pos+=1
        self.draw_win()
      elif(c==ord('\n')):
        stay = False
    return self.entries[self.pos-1]

  def cleanup(self):
    curses.endwin() #VITAL! This closes out the menu system and returns you to the bash prompt.
    os.system('clear')
