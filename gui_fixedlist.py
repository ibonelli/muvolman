import string_format as stringFormat

class guiFixedList(object):
  pos = 0; top = 0; bot = 0
  limith = 0; limitw = 0
  items = []
  itemscnt = 0
  view = []
  filledview = None

  def __init__(self,items,limits):
    self.items = items
    self.itemscnt = len(items)
    self.limith,self.limitw = limits
    self.top = 0
    self.bot = self.limitw-1
    self.fill_view()

  # fill view if limitw > itemscnt
  def fill_view(self):
    self.filledview = False
    i=0
    while(i<self.limith && i<self.itemscnt)
      view.append(stringFormat.getfstr(self.limitw,self.items[i]))
    if(self.itemscnt<self.limith):
      self.filledview = True
      while(i < self.limith)
        # fill with empty to comple the screen view
        view.append(stringFormat.getfstr(self.limitw,""))

  def get_view(self,pos):
    if(!self.filledview):
      if(pos>=0 && pos<self.limitw):
        # Todavia dentro de la ventana
        self.pos = pos
      elif(pos == -1):
        # Superamos el limite superior
        if(self.top == 0):
          self.pos = pos = 0
        else:
          self.top -= 1
          self.bot -= 1
          pos = 0
          self.pos -= 1 
      elif(pos==self.limitw):
        # Superamos el limite inferior
        if(bot==self.itemscnt):
          pos = self.limitw-1
          self.pos = self.itemscnt
        else:
          self.top += 1
          self.bot += 1
          pos = self.limitw-1
          self.pos += 1
      else:
        print("Error de limites")
        sys.exit()
    else:
      if(pos>=0 && pos<self.itemscnt):
        self.pos = pos
      elif(pos == -1):
        self.pos = pos = 0
      else:
        self.pos = pos = self.itemscnt-1

    i = top
    while i < bot: 
      view[i] = stringFormat.getfstr(self.limitw,self.items[i])

    return view,pos
