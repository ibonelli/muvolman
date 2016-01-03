import string_format as stringFormat

class guiFixedList(object):
  top = 0; pos = 0
  botitem = 0; botscreen = 0 
  limith = 0; limitw = 0
  items = []
  itemscnt = 0
  view = []

  def __init__(self,items,limits):
    self.items = items
    self.itemscnt = len(items)
    self.limith,self.limitw = limits
    self.top = 0
    self.botscreen = self.limitw-1
    self.botitem = self.itemscnt-1
    self.fill_view()

  def fill_view(self):
    if(self.itemscnt<self.limitw):
      # fill with empty to comple the screen view
      view.append(begin_y+i, begin_x, stringFormat.getfstr(self.winwidth-2,""), self.color["basic"])
    else:
      i = 0
      while i < limitw
        
        view[i]=items[top+i]

  def get_view(self,pos):
    if(pos>=0 && pos<limitw):
      # Todavia dentro de la ventana
      
    elif(pos == -1):
      # Superamos el limite superior
      if(top == 0):
        self.pos = pos = 0
      else:
        top -= 1
        bot -= 1
        pos = 0
        self.pos -= 1 

    elif(pos==limitw):
      # Superamos el limite inferior
      if(bot==itemscnt):
        pos = self.limitw-1
        self.pos = itemscnt
      else:
        top += 1
        bot += 1
        pos = self.limitw-1
        self.pos += 1

    else:
      print("Error de limites")
      sys.exit()

    i = top
    while i < bot: 
      

    return view,pos
