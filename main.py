from LinkedList.simplyList import SimplyList
from Punto1 import Combinar
from Punto3 import PilaConColas
from Punto2 import Obra
import random


def punto1():
    print("===PUNTO 1===")
    # Instancia de objetos y ejemplos
    l1 = SimplyList()
    l2 = SimplyList()
    l4 = SimplyList()
    l5 = SimplyList()
    l6 = SimplyList()

    # Lista1
    l1.insert(9)
    l1.insert(7)
    l1.insert(3)
    # Lista 2
    l2.insert(1)
    l2.insert(3)
    l2.insert(8)

    # Lleno las listas 3 y 4 de manera aleatoria
    for i in range(1, 5):
        l4.insert(i * random.randint(1, 9))
        l5.insert(i * random.randint(8, 20))
        l6.insert(i * random.randint(7, 15))

    # Crear una instancia de la clase Combinar
    comb = Combinar.Combinar()
    # Realizo los ejemplos
    print("Ejemplo 1")
    l4 = comb.combinar(l1, l2)
    l4.printvalues()
    print("Ejemplo 2")
    l6 = comb.combinar(l4, l5)
    l6.printvalues()
    print("Ejemplo 3")
    l5 = comb.combinar(l5, l6)
    l5.printvalues()
    print("Ejemplo 4")
    # Nota: Los resultados de combinar se pueden ver directamente sin la necesidad de asignarle una variable.
    comb.combinar(l6, l1).printvalues()  # Esto sucede porque la clase combinar retorna una lista nueva ya combinada.


def punto2():
    print("===PUNTO 2===")

    # Intancia de la clase Obra y 3 ejemplos
    obra = Obra.Obra("Monalisa", 5)

    obra.agregarReplica("Monalisa")
    obra.agregarReplica("Monalisa")
    obra.venderReplica("Monalisa")  # ---> Quedaria 6 replicas de la monalisa (La Gioconda)

    obra.agregarReplica("Noche Estrellada")
    obra.agregarReplica("Noche Estrellada")
    obra.venderReplica("Noche Estrellada")  # ----> Quedaria 1 replica de una Noche estrellada

    obra.agregarReplica("La joven de la perla")
    obra.agregarReplica("La joven de la perla")
    obra.agregarReplica("La joven de la perla")
    obra.venderReplica("La joven de la perla")  # --> Quedaria 2 replicas de La joven de perla

    obra.listarReplicas()


def cola1():
    print("\n===PUNTO 3===")
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

    print("Se ejecuta Pop en pila con colas. El valor a realizarle la función Pop es: " + str(pila.popPilaConColas()))
    print("###")
    pila.mostrarPilaConColas()
    print("###")
    print("Se ejecuta Pop en pila con colas. El valor a realizarle la función Pop es: " + str(pila.popPilaConColas()))
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

    print("Se ejecuta Pop en pila con colas. El valor a realizarle la función Pop es: " + str(pila.popPilaConColas()))
    print("###")
    pila.mostrarPilaConColas()
    print("###")

    print("Se ejecuta Pop en pila con colas. El valor a realizarle la función Pop es: " + str(pila.popPilaConColas()))
    print("###")
    pila.mostrarPilaConColas()
    print("###")

    print("Se ejecuta Pop en pila con colas. El valor a realizarle la función Pop es: " + str(pila.popPilaConColas()))
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

    print("La pila se encuentra vacia? " + str(pila.estaVaciaPilaConColas()))

    print("Se ejecuta Pop en pila con colas. El valor a realizarle la función Pop es: " + str(pila.popPilaConColas()))

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


# === Punto 1 ===
punto1()
# === Punto 2 ===
punto2()
# === Punto 3 ===
cola1()
cola2()
cola3()
