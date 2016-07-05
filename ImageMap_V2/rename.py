import os


def rename():
    count = 0
    
    for filename in os.listdir("."):
        if filename.endswith(".jpg"):
            newName = 'file'+str(count)+'.jpg'
            os.rename(filename, newName)
        count = count + 1

rename()
