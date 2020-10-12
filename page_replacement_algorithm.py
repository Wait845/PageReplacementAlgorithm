import random
# FIFO algorithm
def fifo(data):
    memory = []
    fault = 0
    oldestAddr = 0
    for page in data:
        if oldestAddr >= numOfFrames:
            oldestAddr -= numOfFrames

        if page not in memory:
            if len(memory) < numOfFrames:
                memory.append(page)
            else:
                memory.pop(oldestAddr)
                memory.insert(oldestAddr, page)
                fault += 1
                oldestAddr += 1
        print(memory, "numbers of fault:", fault)


# LRU algorithm
def lru(data):
    memory = []
    fault = 0
    last_reference = {}
    for page in data:
        for node in last_reference:
            last_reference[node] += 1
        last_reference[page] = 0
        
        
        
        if memory.count(page) == 0:     # This page is not exists in the list
            if len(memory) < numOfFrames:
                memory.append(page)
            else:
                fault += 1

                recently = None
                for node in last_reference:
                    
                    if recently == None:
                        recently = node
                        continue
                    elif last_reference[node] > last_reference[recently]:
                        recently = node

                memory[memory.index(recently)] = page
                last_reference.pop(recently)
        else:
            last_reference[page] = 0
        # print(memory, page)
        # print(last_reference)

        print(memory, "numbers of fault:", fault)

        
# OPTIMAL algorithm
def optimal(data):
    memory = []
    fault = 0
    for index, page in enumerate(data):
        if len(memory) < numOfFrames:
            if memory.count(page) == 0:     # current page is not existing
                memory.append(page)

        elif memory.count(page) == 0:
            fault += 1
            # pick one to replace
            next_use = {}
            pick = None
            # check if use furture
            for temp in memory:
                if temp not in data[index:]:      # doesnt use furture
                    pick = temp
                    break
                else:   # use in furture
                    distance = data[index:].index(temp)
                    next_use[temp] = distance
            else:   # every node is use in furture
                # calculate farest node
                for node in next_use:
                    if pick == None:
                        pick = node
                    else:
                        if next_use[node] > next_use[pick]:
                            pick = node
            
            memory[memory.index(pick)] = page
        print(memory, page)
    print(memory, "numbers of fault:", fault)
    

# 生成数据的方法
def generate(nums):
    data = []
    for _ in range(nums):
        data.append(random.randint(0, 9))
    return data

# 程序开始
type = input("Type numbers(1), Random generate(2):")
if type == "1":     # read from the path
    temp = input("INPUT:")
    data = []
    for i in temp.split(" "):
        data.append(i)
    
elif type == "2":       # random nums
    nums = int(input("How many numbers?:"))
    data = generate(nums)
    print("The numbers are ", data)
else:   # other
    exit()

numOfFrames = int(input("How many frames?:"))
mode = input("Select an algorithm:FIFO(1), LRU(2), OPTIMAL(3):")
if mode == "1":
    fifo(data)
elif mode == "2":
    lru(data)
elif mode == "3":
    optimal(data)
    


