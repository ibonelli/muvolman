import os
import sys
import pickle

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
    if(self.parent==None):
      print('d,'+str(self.did)+',root,'+self.dirpath+','+str(self.size)+','+str(self.du))
    else:
      print('d,'+str(self.did)+','+str(self.pdid)+','+os.path.basename(self.dirpath)+','+str(self.size)+','+str(self.du))
  def print_dirs(self):
    #print('--dirs--')
    for d in self.dirs:
      print('d,'+str(d.did)+','+str(d.pdid)+','+os.path.basename(d.dirpath))
  def print_subdirs(self):
    #print('--subdirs--')
    for d in self.dirs:
      d.print_self()
      d.print_files()
      d.print_subdirs()
  def print_files(self):
    #print('--files--')
    for f,size,du in self.files:
      print('f,'+str(self.did)+','+f+','+str(size)+','+str(du))
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
  def serialize_self(self):
    return ('d,'+str(self.did)+','+self.dirpath+','+str(self.pdid)+','+str(self.size)+','+str(self.du))
  def serialize_file(self):
    filelist = []
    for f,size,du in self.files:
      filelist.append('f,'+str(self.did)+','+f+','+str(size)+','+str(du))
    return filelist

if(__name__ == '__main__'):
  if(len(sys.argv) < 2):
    print('Malos datos de entrada')
    exit(-1)
  else:
    root = DirTree(sys.argv[1])
    root.calc_sizes()
    print('---Saving---')
    mylist = root.get_tree()
    for l in mylist:
      print(l.serialize_self())
    output = open('data.pkl', 'wb')
    pickle.dump(mylist, output)
    output.close()
    print('---Loading---')
    pkl_file = open('data.pkl', 'rb')
    list_dirs = pickle.load(pkl_file)
    # Works
    #for l in list_dirs:
    #  print(l.serialize_self())
    # Trying
    list_dirs[0].show_tree()
    #print('---tree---')
    #root.show_tree()
    #print('---listing---')
    #root.print_self()
    #root.print_files()
    #root.print_subdirs()
