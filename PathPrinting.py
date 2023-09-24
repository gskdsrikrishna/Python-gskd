import os
file="gskd.txt"
loc="C:/Users/GS.Devarayulu/OneDrive/Desktop/Bhuvana/"
path=os.path.join(loc,file)
print(path)
os.remove(path)