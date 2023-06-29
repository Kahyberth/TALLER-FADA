class PilaConColas:
    def __init__(self):
        self.cola1 = []
        self.cola2 = []

    def estaVaciaPilaConColas(self):
        return len(self.cola1) == 0

    def pushPilaConColas(self, cola):

        while len(self.cola1) > 0:
            self.cola2.append(self.cola1.pop(0))


        self.cola1.append(cola)


        while len(self.cola2) > 0:
            self.cola1.append(self.cola2.pop(0))

    def popPilaConColas(self):
        if self.estaVaciaPilaConColas():
            return None


        return self.cola1.pop(0)

    def mostrarPilaConColas(self):
        if self.estaVaciaPilaConColas():
            print("La pila con colas está vacía")
        else:
            print("Elementos de la pila con colas:")
            for cola in self.cola1:
                print(cola)
