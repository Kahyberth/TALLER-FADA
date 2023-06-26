from LinkedList.simplyList import SimplyList
from Punto1 import Combinar

def test():
    # Instancia de objetos
    l1 = SimplyList()
    l2 = SimplyList()

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
    comb.Combinar().combinar(l1, l2).printValues()

test()
