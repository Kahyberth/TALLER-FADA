from LinkedList import simplyList


class Combinar:

    @staticmethod
    def combinar(l1: simplyList.SimplyList, l2: simplyList.SimplyList):

        l3 = simplyList.SimplyList()
        for i in range(l1.length):
            l3.insert(l1.getindex(i))
        for j in range(l2.length):
            l3.insert(l2.getindex(j))
        return l3
