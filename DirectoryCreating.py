import os
directory = "Indu"
parent_dir = "C:/Users/GS.Devarayulu/OneDrive/Desktop"
mode = 0o666
path = os.path.join(parent_dir, directory)
os.makedirs(path, mode)
print("Directory '% s' created" % directory)