from LinkedList import simplyList

class Combinar:

    def combinar(self, l1: simplyList.SimplyList, l2: simplyList.SimplyList):
        l3 = simplyList.SimplyList()
        for i in range( l1.length() ):
            l3.insert( l1.getIndex(i) )
        for j in range( l2.length() ):
            l3.insert( l2.getIndex(j) )
        return l3