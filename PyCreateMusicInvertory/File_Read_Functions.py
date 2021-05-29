'''
Created on May 27, 2021

@author: rduvalwa2
'''
import sys, platform

class file_Read_Functions():
    def __init__(self, f,mode):
        '''
        open() returns a file object, and is most commonly used with two arguments: open(filename, mode).
        second argument string describing the way the file will be used
         'r' read
         'w' writing (an existing file with the same name will be erased)
         'a' opens the file for appending any data written to the file is automatically added to the end
         'r+' opens the file for both reading and writing
         mode argument is optional; 'r' will be assumed if it’s omitted.
        '''
        try:
            self.filObj = open(f,mode)
        except Exception as e:
            print(e)
    
    def read_file(self):
        print("function read_file")
        print(self.filObj.read())
        
    def read_file_line(self):
        print("function read_file_line")
        print(self.filObj.readline())
    
    def read_file_lines(self,numberOfLines):
        print("function read_file_lines")
        n = 0
        for line in self.filObj:
            if n < numberOfLines:
                print(n, line)
                n = n + 1

    def close_file(self):
        self.filObj.close()
        if self.filObj.closed:
            print("File ",self.filObj.name," is closed")
        else:
            print("File ", self.filObj.name," is NOT closed")
             
class file_attributes():
    def __init__(self, filee, mode):
        try:
            self.myfile = open(filee,mode)
        except FileNotFoundError as e:
            print(e)
            return None
        except ValueError as e:
            print(e)
            return None
        
    def get_file_mode(self):  # get file mode 
        try:
            return self.myfile.mode
        except Exception as e:
            return e

    def get_file_encoding(self):
        try:
            return 'This system ' + platform.system()  + " system encoding is " + sys.getfilesystemencoding()
        except Exception as e:
            print(e)
    
    def close_file(self):
        try:
            result = self.myfile.close()
            print("Close Result is ", result)
            
        except Exception as e:
            print(e)
          
    def get_close(self):
        try:
            return self.myfile.closed
        except Exception as e:
            print( e)
    
    def get_file_name(self):
        try:
            return self.myfile.name
        except Exception as e:
            return e
    
    def get_file_newline_type(self):
        '''
        newlines
        If Python was built with the --with-universal-newlines option to configure (the default) this read-only 
        attribute exists, and for files opened in universal newline read mode it keeps track of the types of newlines 
        encountered while reading the file. The values it can take are '\r', '\n', '\r\n', None (unknown, no newlines read yet)
         or a tuple containing all the newline types seen, to indicate that multiple newline conventions were encountered. For 
         files not opened in universal newline read mode the value of this attribute will be None.
        '''
        try:
            return self.myfile.newlines
        except Exception as e:
            return e
        
    def get_file_softspace(self):
        '''
        softspace
        Boolean that indicates whether a space character needs to be printed before another value when using the 
        print statement. Classes that are trying to simulate a file object should also have a writable softspace attribute, 
        which should be initialized to zero. This will be automatic for most classes implemented in Python (care may be needed 
        for objects that override attribute access); types implemented in C will have to provide a writable softspace attribute.
        Note: This attribute is not used to control the print statement, but to allow the implementation of print to keep track 
        of its internal state.
        '''
        try:
            return self.myfile.softspace()
        except Exception as e:
            return e
        
    
if __name__ == '__main__':
    f = './testFile.txt'
    fx = './testFile2.txt'
    ff = file_Read_Functions(fx,'r')
    fa = file_attributes(f,'w+')
    NoFile = file_attributes('noExist.txt','r')
    BadMode = file_attributes(fx,'X')
    ff.read_file()
    ff.close_file()
    ff2 = file_Read_Functions(fx,'r')
    ff2.read_file_line()
    ff2.close_file()
    ff3 = file_Read_Functions(fx,'r')
    ff3.read_file_lines(2)
    ff3.close_file()
    
    print(fa.get_file_mode())
    print(fa.get_file_name())
    print(fa.get_file_encoding())
    print(fa.get_file_newline_type())
    print(fa.get_file_softspace())
    print(fa.get_close())
    fa.close_file()
    print(fa.get_close())    
    
    

    