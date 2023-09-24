import os
try:
    filename = 'C:/Users/GS.Devarayulu/OneDrive/Desktop/gskd.txt'
    f = open(filename, 'r')
    text = f.read()
    print(text)
    f.close()
except IOError:
    print('Problem reading: ' + filename)