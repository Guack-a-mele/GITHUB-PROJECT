qitemd={}

with open("qitemd.txt", "r+") as qitem:
        while True:
            try:
                for i, line in enumerate(qitem, start=1):
                    if "-" in line:
                        ab=qitem.readline()
                        abc=(len(ab)-1)
                        abcd,cd=line.split("-")
                        qitemd[cd]=qitemd[cd]-qty
            except EOFError:
                break