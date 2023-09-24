#53.Copying Files
import os
import shutil
origin="C:/Users/GS.Devarayulu/OneDrive/Desktop/Gskd/"
target="C:/Users/GS.Devarayulu/OneDrive/Desktop/Bhuvana/"
files=os.listdir(origin)
print(files)
for file_name in files:
    shutil.copy(origin+file_name,target+file_name)
print("Files are copied")