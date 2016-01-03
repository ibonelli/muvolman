# string to human bytes conversion

def convertbh(size):
  # bytes
  if(size<1024):
    return str(size)
  # Kbytes
  elif(size<1024*1024):
    return dformat(size/1024)+"K"
  # Mbytes
  elif(size<1024*1024*1024):
    return dformat(size/(1024*1024))+"M"
  # Gbytes
  else:
    return dformat(size/(1024*1024*1024))+"G"

def dformat(x):
  return ('%.2f' % x).rstrip('0').rstrip('.')

# string format for fixed size

def getfstr(maxsize,string,mode=None):
  if(mode==None):
    return(fillstr(maxsize,string))
  if(mode=="dir"):
    return(filldstr(maxsize,string))
  if(mode=="file"):
    return(fillfstr(maxsize,string))

def fillstr(maxsize,string):
  mystr = string
  if(len(string) < maxsize):
    strfill = maxsize - len(string)
    while strfill > 0:
      mystr += ' '
      strfill -= 1
  else:
    mystr = string[0:maxsize]
  return mystr

def filldstr(maxsize,string):
  mystr = string
  if(len(mystr) < maxsize-2):
    strfill = maxsize-2 - len(mystr)
    while strfill > 0:
      mystr += ' '
      strfill -= 1
  else:
    mystr = string[0:maxsize-2]
  return "["+mystr+"]"

def fillfstr(maxsize,string):
  mystr1,size = string
  mystr2 = convertbh(size)
  if(len(mystr1)+len(mystr2) < maxsize-3):
    strfill = maxsize-3 - len(mystr1)- len(mystr2)
    while strfill > 0:
      mystr1 += ' '
      strfill -= 1
  else:
    mystr1 = mystr1[0:maxsize-3]
  return mystr1+" ("+mystr2+")"
