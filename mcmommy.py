qitemd={}
with open("qitemd.txt", "r+") as qitem:
        while True:
            try:
                ab=qitem.readline()
                abc=(ab.len()-1)
                abcd,cd=qitem.read(abc).split("-")
                qitemd[key]=qitemd[key]-qty
            except EOFError:
                break
            
