import os
import sys
import pickle
from dirtree import DirTree

if(__name__ == '__main__'):
  if(len(sys.argv) < 2):
    print('Malos datos de entrada')
    exit(-1)
  else:
    root = DirTree(sys.argv[1])
    root.calc_sizes()
    print('Saving...')
    mylist = root.get_tree()
    output = open('data.pkl', 'wb')
    pickle.dump(mylist, output)
    output.close()
    print('Loading...')
    pkl_file = open('data.pkl', 'rb')
    list_dirs = pickle.load(pkl_file)
    print('---tree1---')
    list_dirs[0].show_tree()
    print('---tree2---')
    for curdir in list_dirs:
      curdir.print_self()
    #print('---listing---')
    #list_dirs[0].print_self()
    #list_dirs[0].print_files()
    #list_dirs[0].print_subdirs()
