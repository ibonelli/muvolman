import os
import sys

class CurDir(object):
  def __init__(self,dirpath,dirtreeref=None):
    self.dirpath = dirpath
    self.dirtreeref = dirtreeref
    self.dirs = []
    self.files = []
    if(dirtreeref==None):
      for f in os.listdir(dirpath):
        if(os.path.isfile(os.path.join(dirpath,f))):
          self.files.append((f,os.stat(dirpath).st_size()))
        if(os.path.isdir(os.path.join(startpath,f))):
          self.dirs.append((f,None))
    else:
      self.dirs = dirtreeref.get_dirs()
      self.files = dirtreeref.get_files()

class DirTree(object):
  lastdid=0
  def __init__(self,dirpath,parent=None):
    self.did = DirTree.lastdid
    DirTree.lastdid+=1
    self.dirpath = dirpath
    self.parent = parent
    if(parent==None):
      self.pdid = None
    else:
      self.pdid = self.parent.did
    self.dirs = []
    self.files = []
    self.size = None
    self.du = None
    self.walk_self(self.dirpath)
  def append_child_dirs(self,mydir,parent=None):
    self.dirs.append(DirTree(mydir,parent))
  def append_child_files(self,myfile,size=None,du=None):
    self.files.append((myfile,size,du))
  def walk_self(self,startpath):
    for f in os.listdir(startpath):
      filefullpath = os.path.join(startpath,f)
      if(os.path.isfile(filefullpath)):
        fst = os.stat(filefullpath)
        self.append_child_files(f,fst.st_size,fst.st_blocks*512)
      if(os.path.isdir(filefullpath)):
        self.append_child_dirs(filefullpath,self)
  def get_name(self):
    return os.path.basename(self.dirpath)
  def print_self(self):
    #print('--self--')
    print(self.serialize_self())
  def print_dirs(self):
    #print('--dirs--')
    dirlist = self.serialize_dirs()
    for dstr in self.dirlist:
      print(dstr)
  def print_subdirs(self):
    #print('--subdirs--')
    for d in self.dirs:
      d.print_self()
      d.print_files()
      d.print_subdirs()
  def print_files(self):
    #print('--files--')
    filelist = self.serialize_files()
    for fstr in filelist:
      print(fstr)
  def calc_sizes(self):
    for d in self.dirs:
      d.calc_sizes()
    total = 0
    totaldu = 0
    for f in self.files:
      total+=f[1]
      totaldu+=f[2]
    for d in self.dirs:
      total+=d.size
      totaldu+=d.du
    self.size=total
    self.du=totaldu
  def show_tree(self):
    print self.dirpath
    for d in self.dirs:
      d.show_tree()
  def get_tree(self):
    dirlist = []
    dirlist.append(self)
    for d in self.dirs:
      dirlist.append(d)
    return dirlist
  def get_dirs(self):
    dirlist = []
    for d in self.dirs:
      dirlist.append((os.path.basename(d.dirpath),self))
    return dirlist
  def get_files(self):
    filelist = []
    for f,size,du in self.files:
      filelist.append((f,size))
    return filelist
  def serialize_self(self):
    if(self.parent==None):
      return ('d,'+str(self.did)+','+self.dirpath+',root,'+str(self.size)+','+str(self.du))
    else:
      return ('d,'+str(self.did)+','+self.dirpath+','+str(self.pdid)+','+str(self.size)+','+str(self.du))
  def serialize_dirs(self):
    dirlist = []
    for d in self.dirs:
      dirlist.append('d,'+str(d.did)+','+str(d.pdid)+','+os.path.basename(d.dirpath))
    return dirlist
  def serialize_files(self):
    filelist = []
    for f,size,du in self.files:
      filelist.append('f,'+str(self.did)+','+f+','+str(size)+','+str(du))
    return filelist
