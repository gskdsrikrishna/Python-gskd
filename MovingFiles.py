#53.Moving Files
import os
source="C:/Users/GS.Devarayulu/OneDrive/Desktop/Bhuvana"
destination="C:/Users/GS.Devarayulu/OneDrive/Desktop/Gskd"
allfiles=os.listdir(source)
for f in allfiles:
    src_path=os.path.join(source,f)
    dst_path=os.path.join(destination,f)
    os.rename(src_path,dst_path)