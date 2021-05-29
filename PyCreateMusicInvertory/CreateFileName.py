'''
Created on May 28, 2021

@author: rduvalwa2
'''
import platform, time
from test.test_logging import secs

class createFileName():
    def __init__(self):
        print("*************** Node Name is ", platform.uname().node)
        self.hostname = platform.uname().node
        
    
    def getTime(self):
        print("Local: ", time.localtime())
        print("GMT:", time.gmtime())
        print("Time: ",time.time())
        self.localTime = time.localtime()
        self.gmtTime = time.gmtime()
        self.myTime = time.time_ns()
        
    def createName(self):
        self.localFilename = self.hostname + str(self.myTime) + ".txt"
#        self.gmtFilename = self.hostname + self.gmtTime() + ".txt"
        print(self.localFilename)
#        print( self.gmtFilename)
        return(self.localFilename)
        
if __name__ == '__main__':
    myFilename = createFileName()
 #   myFilename.createName()
    myFilename.getTime()
    print("Returned ",myFilename.createName())