from LinkedList.simplyList import SimplyList
from Punto1 import Combinar
from Punto2 import Obra

def test():


    # Instancia de objetos
    l1 = SimplyList()
    l2 = SimplyList()
    l4 = SimplyList()

    l1.insert(9)
    l1.insert(7)
    l1.insert(3)
    # Lista 2
    l2.insert(1)
    l2.insert(3)
    l2.insert(8)

    # Crear una instancia de la clase Combinar
    comb = Combinar

    # Llamar al método Combinar pasando l1 como argumento
    comb.Combinar().combinar(l1, l2).printvalues()

    print("===PUNTO 2===")

    #Intancia de la clase Obra
    obra = Obra.Obra("Monalisa",5)
    obra.agregarReplica("Monalisa")
    obra.agregarReplica("Monalisa")
    obra.venderReplica("Monalisa")
    obra.agregarReplica("Noche Estrellada")
    obra.agregarReplica("Noche Estrellada")
    obra.venderReplica("Noche Estrellada")
    obra.listarReplicas()

test()
