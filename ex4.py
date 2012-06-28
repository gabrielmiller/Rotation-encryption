import copy #Import copy because deepcopy is used
 
class dataChunk():
    def __init__(self, chunk):
        self.chunk = chunk
    def breakToList(self):  #Breaks strings into lists of strings, and lists of strings into lists of lists of strings
        try:
            for num in range(len(self.chunk)):
                self.chunk[num]=list(self.chunk[num])
        except:
            self.chunk=list(self.chunk)
    def stringToBinary(self):   #Converts each character into binary and replaces its "0b" with "00" if applicable
        for num in range(len(self.chunk)):
            self.chunk[num]='0'*(8-ord(self.chunk[num]).bit_length())+bin(ord(self.chunk[num])).lstrip('0b')
    def flipData(self): #Interprets data from a shifted 90 degree perspective
        self.temp = copy.deepcopy(self.chunk)
        for num in range(len(self.chunk)):
            for innum in range(len(self.chunk[num])):
                self.temp[num][innum]=self.chunk[innum][num]
        self.chunk=self.temp
    def unbreakList(self):  #Joins lists of lists of strings into lists of strings, and lists of strings into strings
        try:
            self.chunk=''.join(self.chunk)
        except:
            for num in range(len(self.chunk)):
                self.chunk[num]=''.join(self.chunk[num])
    def binaryToString(self):   #Converts binary strings into single character strings
        for num in range(len(self.chunk)):
            self.chunk[num]=chr(int(self.chunk[num],2))
    def createOutput(self): #Returns output to the user
        return self.chunk
 
def main():
    enteredData = raw_input("Enter your data > ")
    modDiff = len(enteredData)%8        #Makes sure our chunks are each 8 characters.
    eData = enteredData[:]              #If they aren't then the difference in 0s is appended to the string.
    if modDiff>0:
        eData = enteredData[:]+(8-modDiff)*'0'
    chunkDict = {}
    counter = 0
    while len(eData)>0:                  #Create a dict of 8 character chunks and instance their values.
        chunkDict[counter]=dataChunk(eData[:8])
        eData = eData[8:]
        counter+=1
    output=''
    for item in chunkDict:              #For every 8 character chunk, iterate through the methods and concatenate output
        chunkDict[item].breakToList()
        chunkDict[item].stringToBinary()
        chunkDict[item].breakToList()
        chunkDict[item].flipData()
        chunkDict[item].unbreakList()
        chunkDict[item].binaryToString()
        chunkDict[item].unbreakList()
        output=output[:]+chunkDict[item].createOutput()
    print "Your output is \'%s\'" % output
 
if __name__ == "__main__":
    main()
