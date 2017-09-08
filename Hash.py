import hashlib
from pathlib import Path
import pprint
BLOCKSIZE = 65536
pp = pprint.PrettyPrinter(indent=4)

def listFiles(p):
    return [listHash(f) for f in p.iterdir() if p.is_file()] 

def listHash(f):
    hasher = hashlib.md5()
    with open(f,'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf)>0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    print(f.name, str(f.parent), hasher.hexdigest())

    return((f.name, str(f.parent),hasher.hexdigest()))

def iterFiles(p):
    c = 0
    for i in p.iterdir():
        if i.is_dir():
            x = iterFiles(i)
            c = c + 1
            if c<0:
                break
        else:
            l.append(listHash(i))
    return l        

def checkDups():
    #f = open(r'C:\Users\McColgan\Pictures','r')
    for i in l:
        #pp.pprint(i)
        for j in l:
            if i[2] == j[2] and i != j:
                print('Duplicate')    
                pp.pprint(i)
                pp.pprint(j)
                #f.write(i[0], j[0], i[1],i[2])
    #f.close

p = Path(r'C:\Users\McColgan\Pictures')
print(p)         
#d = [listFiles(x) for x in p.iterdir() if x.is_dir()]
l = []
l = iterFiles(p)
with open(r'C:\Users\McColgan\Documents\files.txt','w') as f:
    pf = pprint.PrettyPrinter(indent=4,stream=f)
    pf.pprint(l)
    f.write("data")
    f.write(str(l))
    f.close
checkDups()



    
