from LinkedList.simplyList import SimplyList
from Punto1 import Combinar
from Punto3 import PilaConColas
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

def cola1():
    pila = PilaConColas.PilaConColas()
    print("-----------------------------------------")
    print("PILA CON COLAS 1")
    print("La pila se encuentra vacia? " + str(pila.estaVaciaPilaConColas()))
    print("Se insertan los valores 1, 2, 3, 4, 5, 6, 7 y 8 a la pila con colas")
    pila.pushPilaConColas(1)
    pila.pushPilaConColas(2)
    pila.pushPilaConColas(3)
    pila.pushPilaConColas(4)
    pila.pushPilaConColas(5)
    pila.pushPilaConColas(6)
    pila.pushPilaConColas(7)
    pila.pushPilaConColas(8)

    print("La pila se encuentra vacia? " + str(pila.estaVaciaPilaConColas()))

    print("Se ejecuta Pop en pila con colas. El valor a realizarle la función Pop es: "+ str(pila.popPilaConColas()))
    print("###")
    pila.mostrarPilaConColas()
    print("###")
    print("Se ejecuta Pop en pila con colas. El valor a realizarle la función Pop es: "+ str(pila.popPilaConColas()))
    print("###")
    pila.mostrarPilaConColas()
    print("###")
    print("-----------------------------------------")


def cola2():
    pila = PilaConColas.PilaConColas()
    print("-----------------------------------------")
    print("PILA CON COLAS 2")
    print("La pila se encuentra vacia? " + str(pila.estaVaciaPilaConColas()))
    print("Se insertan los valores 10, 20 y 30 a la pila con colas")
    pila.pushPilaConColas(10)
    pila.pushPilaConColas(20)
    pila.pushPilaConColas(30)

    print("La pila se encuentra vacia? " + str(pila.estaVaciaPilaConColas()))

    print("Se ejecuta Pop en pila con colas. El valor a realizarle la función Pop es: "+ str(pila.popPilaConColas()))
    print("###")
    pila.mostrarPilaConColas()
    print("###")

    print("Se ejecuta Pop en pila con colas. El valor a realizarle la función Pop es: " + str(pila.popPilaConColas()))
    print("###")
    pila.mostrarPilaConColas()
    print("###")

    print("Se ejecuta Pop en pila con colas. El valor a realizarle la función Pop es: "+ str(pila.popPilaConColas()))
    print("###")
    pila.mostrarPilaConColas()
    print("###")
    print("-----------------------------------------")


def cola3():
    pila = PilaConColas.PilaConColas()
    print("-----------------------------------------")
    print("PILA CON COLAS 3")
    print("La pila se encuentra vacia? " + str(pila.estaVaciaPilaConColas()))
    print("Se insertan los valores 500000, 1000000 y 2000000 a la pila con colas")
    pila.pushPilaConColas(500000)
    pila.pushPilaConColas(1000000)
    pila.pushPilaConColas(2000000)

    print("La pila se encuentra vacia? "+ str(pila.estaVaciaPilaConColas()))

    print("Se ejecuta Pop en pila con colas. El valor a realizarle la función Pop es: "+ str(pila.popPilaConColas()))

    print("###")
    pila.mostrarPilaConColas()
    print("###")

    print("Se insertan los valores 3000000, 4000000 y 5000000 a la pila con colas")
    pila.pushPilaConColas(3000000)
    pila.pushPilaConColas(4000000)
    pila.pushPilaConColas(5000000)

    print("Se ejecuta Pop en pila con colas. El valor a realizarle la función Pop es: " + str(pila.popPilaConColas()))

    print("###")
    pila.mostrarPilaConColas()
    print("###")

    print("-----------------------------------------")


test()
cola1()
cola2()
cola3()