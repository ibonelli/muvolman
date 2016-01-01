import os
import sys

class Directorio(object)
  def __init__(self,name,dirpath,parent):
    self.dirpath = dirpath
    self.parent = parent
    self.dirs = []
    self.files = []
    self.size = None
  def append_child_dirs(self,mydir):
    self.dirs.append(Directorio(mydir,os.path.join(self.dirpath,mydir)))
  def append_child_files(self,myfile,size=None):
    self.children.files.append((myfile,size))
  def list_dirs(self):
    print self.children.dirs
  def list_files(self):
    print self.children.files

if(__name__ == '__main__'):
  if(len(sys.argv) < 2):
    print('Malos datos de entrada')
    exit(-1)
  else:
    mypath = sys.argv[1]
    for root, dirs, files in os.walk(mypath, topdown=True):
      if(mypath == root):
        mydir = Directorio(mypath,root,None)
      else
        mydir = Directorio(os.path.basename(root),root,None)

      for name in files:
        mydir.append_child_files(name,None)
      for name in dirs:
        mydir.append_child_dirs(name)
