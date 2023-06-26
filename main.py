from LinkedList import simplyList



def test():
    ObjSimplyList = simplyList.SimplyList()

    ObjSimplyList.insert(10)
    ObjSimplyList.insert(2)
    ObjSimplyList.insert(4)
    ObjSimplyList.printValues()
    ObjSimplyList.sort()
    ObjSimplyList.printValues()



test()