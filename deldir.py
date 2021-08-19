import os
def delete():
    listdir=os.listdir()
    cwd=os.getcwd()
    # path=os.path.join(cwd,i)


    for i in list(listdir):
        path=os.path.join(cwd,i)
        try:
            os.remove(path)
        except:
            os.rmdir(path)

delete()