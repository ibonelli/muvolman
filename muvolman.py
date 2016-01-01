import os
import sys

class DirTree(object):
  def __init__(self,dirpath,parent=None):
    self.dirpath = dirpath
    self.parent = parent
    self.dirs = []
    self.files = []
    self.size = None
    self.walk_self(self.dirpath)
  def append_child_dirs(self,mydir,parent=None):
    self.dirs.append(DirTree(mydir,parent))
  def append_child_files(self,myfile,size=None):
    self.files.append((myfile,size))
  def walk_self(self,startpath):
    for f in os.listdir(startpath):
      filefullpath = os.path.join(startpath,f)
      if(os.path.isfile(filefullpath)):
        self.append_child_files(f,os.stat(filefullpath).st_size)
      if(os.path.isdir(filefullpath)):
        self.append_child_dirs(filefullpath,self)
  def list_dirs(self):
    return self.dirs
  def list_files(self):
    return self.files
  def get_name(self):
    return os.path.basename(self.dirpath)

if(__name__ == '__main__'):
  if(len(sys.argv) < 2):
    print('Malos datos de entrada')
    exit(-1)
  else:
    root = DirTree(sys.argv[1])
    print('dirs:')
    for mydir in root.list_dirs():
      print(mydir.get_name())
    print('files:')
    for f,size in root.list_files():
      print(f+','+str(size))

# COMO LISTO SUBDIRS?
# Se estan creando los subdirs?
# Necesito averiguar sobre childs...
