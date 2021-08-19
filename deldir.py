import os
import shutil
def delete():
    listdir=os.listdir()
    cwd=os.getcwd()
    


    for i in list(listdir):
        path=os.path.join(cwd,i)
        try:
            if i=="deldir.py":
                pass
            else:
                os.remove(path)
        except:
            shutil.rmtree(path)

delete()
