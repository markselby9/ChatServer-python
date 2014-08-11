#Implement the replace command. This command will replace one string with another in the list of files provided.
__author__ = 'fengchaoyi'
import os, sys

if __name__=='__main__':
    argvArray = sys.argv
    if len(argvArray) < 4:
        print 'usage: python byte...and.py oldstr newstr file1 (file2...)'
        sys.exit()
    oldstr = argvArray[1]
    newstr = argvArray[2]
    filelist = argvArray[3:]
    for filename in filelist:
        try:
            # reader and writer should be seperate here
            reader = open(filename).read()
            # no need to replace line by line
            reader = reader.replace(oldstr, newstr)
            writer = open(filename, 'w')
            writer.write(reader)
            writer.close()
        except IOError, e:
            print 'file: ' + filename + ' replace error: ', e
        else:
            print 'file: ' + filename + ' replace complete.'
