class Block:
    def __init__(self):
        self.data = [None]*800 #each element will be either 0 or 1
        self.id = 0

class DiskA:
    def __init__(self):
        self.disk = [Block() for i in range(200)]
        self.unallocated = 200

class DiskB:
    def __init__(self):
        self.disk = [Block() for i in range(300)]
        self.unallocated = 300

class Disk:
    def __init__(self , ID , NUM_BLOCKS):
        self.id = ID
        self.num_blocks = NUM_BLOCKS
        self.list_of_blocks =[]



def API_for_write(block_No, data):
    # print "writing in block number "+str(block_No)
    if(block_No <= 200):
        #read and write from diska
        diska.disk[block_No-1].data = data
        # print diska.disk[block_No-1].data
        # print diska
    else:
        #read and write from diskb
        diskb.disk[block_No-201].data = data
        # print diskb.disk[block_No-201].data

def API_for_read(block_No):
    if(block_No <= 200):
        #read and write from diska
        return diska.disk[block_No-1].data
    else:
        #read and write from diskb
        return diskb.disk[block_No-201].data


def CreateDisk(ID, No_of_blocks):
    temp_size = No_of_blocks
    if temp_size <= diska.unallocated + diskb.unallocated:
        new_disk = Disk(ID,No_of_blocks)
        start = -1
        end = -1
        for i in range(1,500):
            if temp_size == 0:
                break
            if (i<=200):
                if diska.disk[i-1].id == 0:
                    if ( start == -1):
                        start = i-1
                    if (end == -1 or end == i-2):
                        end =i-1
                    else:
                        new_disk.list_of_blocks.append((start, end))
                        start = i-1
                        end = i-1
                    diska.disk[i-1].id = ID
                    diska.unallocated = diska.unallocated-1
                    temp_size = temp_size-1
            else:
                if diskb.disk[i-201].id == 0:
                    if ( start == -1):
                        start = i-1
                    if (end == -1 or end == i-2):
                        end =i-1
                    else:
                        new_disk.list_of_blocks.append((start, end))
                        start = i-1
                        end = i-1
                    diskb.disk[i-201].id = ID
                    diskb.unallocated = diskb.unallocated-1
                    temp_size = temp_size-1
        new_disk.list_of_blocks.append((start, end))
        print "for disk ID " + str(ID)
        print new_disk.list_of_blocks
        new_dict[ID] = new_disk
        return new_disk
    else:
        print "ERROR: Insufficient memory to create Disk " + str(ID)
        return None

def disk_print():
    for i in range(1,500):
        if i <= 200:
            print diska.disk[i-1].id
        else:
            print diskb.disk[i-201].id


def DeleteDisk(ID):
	if ID in new_dict:
		for i in range(1,500):
			if i <= 200:
				if diska.disk[i-1].id == ID:
					diska.disk[i-1].id = 0
					diska.disk[i-1].data = [None]*800
					diska.unallocated = diska.unallocated + 1

			else:
				if diskb.disk[i-201].id == ID:
					diskb.disk[i-201].id = 0
					diskb.disk[i-201].data = [None]*800
					diskb.unallocated = diskb.unallocated + 1
		del new_dict[ID]
	else:
		 print "ERROR: Disk " + str(ID) + " not found"


def API_for_write_disk(disk_id, block_no , block_data):
	if disk_id in new_dict:
		disk = new_dict[disk_id]
		if(disk.num_blocks < block_no):
			print "ERROR: Block number out of bounds exception"
		else:
			l = disk.list_of_blocks
			temp_block_number = block_no
			i = 0
			while (i <= len(l)):
				start , end = l[i]
				if (end - start  > temp_block_number):
					API_for_write(start + temp_block_number , block_data)
					break
				else:
					i = i + 1
					temp_block_number = temp_block_number - (end - start)
	else:
		 print "ERROR: Disk " + str(disk_id) + " not found"

def API_for_read_disk(disk_id, block_no):
	if disk_id in new_dict:
		disk = new_dict[disk_id]
		var = None
		if(disk.num_blocks < block_no):
			print "ERROR: Block number out of bounds exception"
		else:
			l = disk.list_of_blocks
			temp_block_number = block_no
			i = 0
			while (i <= len(l)):
				start , end = l[i]
				if (end - start  > temp_block_number):
					var = API_for_read(start + temp_block_number)
					break
				else:
					i = i + 1
					temp_block_number = temp_block_number - (end - start)
		return var
	else:
		 print "ERROR: Disk " + str(disk_id) + " not found"
		 return None

diska = DiskA()
diskb = DiskB()
new_dict = {}


def test_part1():
    API_for_write(1 , "Written text 1")
    API_for_write(200, "Written text 2")
    print API_for_read(1)
    disk1 = CreateDisk(1,100)
    disk2 = CreateDisk(2,50)
    disk3 = CreateDisk(3,150)
    DeleteDisk(2)
    disk4 = CreateDisk(4,100 )
    print "Range of each disk"
    print disk1.list_of_blocks
    print disk3.list_of_blocks
    print disk4.list_of_blocks
    print new_dict
    API_for_write_disk(4,60,"Written text 3")
    print  API_for_read_disk(4,60)
# print diska.disk

test_part1()


# s = stru()
# s.a = 10
