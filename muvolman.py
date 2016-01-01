import os
import sys

class DirTree(object):
  lastdid=0
  def __init__(self,dirpath,parent=None):
    self.did = DirTree.lastdid
    DirTree.lastdid+=1
    self.dirpath = dirpath
    self.parent = parent
    if(parent==None):
      self.pdid = None
      print('d,'+str(self.did)+',None,'+self.dirpath)
    else:
      self.pdid = self.parent.did
      print('d,'+str(self.did)+','+str(self.pdid)+','+os.path.basename(self.dirpath))
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
  def print_self(self):
    print('--self--')
    print('d,'+str(self.did)+','+str(self.pdid)+','+os.path.basename(self.dirpath))
  def print_dirs(self):
    print('--dirs--')
    for d in self.dirs:
      print('d,'+str(d.did)+','+str(d.pdid)+','+os.path.basename(d.dirpath))
  def print_subdirs(self):
    print('--subdirs--')
    for d in self.dirs:
      d.print_self()
      d.print_dirs()
      d.print_files()
      d.print_subdirs()
  def print_files(self):
    print('--files--')
    for f,size in self.files:
      print('f,'+str(self.did)+','+f+','+str(size))

if(__name__ == '__main__'):
  if(len(sys.argv) < 2):
    print('Malos datos de entrada')
    exit(-1)
  else:
    root = DirTree(sys.argv[1])
    print('----main.print()----')
    root.print_self()
    root.print_dirs()
    root.print_files()
    root.print_subdirs()

# COMO LISTO SUBDIRS?
# Se estan creando los subdirs?
# Necesito averiguar sobre childs...
