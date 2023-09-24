#48.Writing Text File
import os
fd = "C:/Users/GS.Devarayulu/OneDrive/Desktop/gskd.txt"
file = open(fd, 'w')
file.write("Hello")
file.close()
file = open(fd, 'r')
text = file.read()
print(text)
file = os.popen(fd, 'w')
file.write("Hello")