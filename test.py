class Block:
    def __init__(self):
        self.block = [None]*800 #each element will be either 0 or 1


class DiskA:
    def __init__(self):
        self.disk = [Block() for i in range(200)]

class DiskB:
    def __init__(self):
        self.disk = [Block() for i in range(300)]



def API_for_write(block_No, data):
    if(block_No <= 200):
        #read and write from diska
        diska.disk[block_No-1] = data
        print diska.disk[block_No-1]
        # print diska
    else:
        #read and write from diskb
        diskb.disk[block_No-201] = data
        print diskb.disk[block_No-201]

def API_for_read(block_No):
    if(block_No <= 200):
        #read and write from diska
        return diska.disk[block_No-1]
        # print diska
    else:
        #read and write from diskb
        return diskb.disk[block_No-201]





diska = DiskA()
diskb = DiskB()

API_for_write(1 , "mamm")
API_for_write(200, "ww")
print API_for_read(88)



# print diska.disk




# s = stru()
# s.a = 10
