import os
directory = "Bhuvana"
parent_dir = "C:/Users/GS.Devarayulu/OneDrive/Desktop"
path = os.path.join(parent_dir, directory)
os.mkdir(path)
print("Directory '% s' created" % directory)