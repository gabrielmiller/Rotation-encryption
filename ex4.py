TheData=raw_input("Enter your data > ")
TheData=str(TheData[:])
lendiff=len(TheData)%8
if lendiff>0:
  TheData=TheData+((8-lendiff)*'0')
 
DataList = list(TheData)
DataListBinary = []
atemp=[]
DataListBinaryOutput = [[],[],[],[],[],[],[],[]]
indexer = [0,0]
for sublst in DataListBinaryOutput:
  sublst=[[],[],[],[],[],[],[],[]]
 
for a in DataList:
  for b in bin(ord(a)):
    atemp.append(b)
  DataListBinary.append(atemp)
  atemp=[]
 
for c in DataListBinary:
  offset=c.index('b')
  c[:offset+1]=offset*['0']
  if len(c)<8:
    c=((8-len(c))*['0'])+c
  for d in c:
    DataListBinaryOutput[indexer[1]].insert(indexer[0],d)
    indexer[1]=indexer[1]+1
  indexer[0]=indexer[0]+1
  indexer[1]=0
 
indexer = [0,0]
joiner=['','','','','','','','']
for e in DataListBinaryOutput:
  for f in e:
    joiner[indexer[0]]=joiner[indexer[0]][:]+f
    indexer[1]=indexer[1]+1
  indexer[1]=0
  indexer[0]=indexer[0]+1
 
finalResult=''
for g in joiner:
  finalResult=finalResult[:]+chr(int(g, 2))
print finalResult
