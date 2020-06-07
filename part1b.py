class Block:
    def __init__(self):
        self.block = [None]*800 #each element will be either 0 or 1

def CreateDisk(ID, No_of_blocks):
    return [Block() for i in range(No_of_blocks)]

disk1 = CreateDisk(1,100)
