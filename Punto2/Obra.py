from LinkedList import simplyList


class Obra:

    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad
        self.inventario = simplyList.SimplyList()
        self.inventario.insert(cantidad, nombre)

    def agregarReplica(self, nombre: str):
        if self.inventario.search_name(nombre):
            self.inventario.set_value_by_name(nombre, self.inventario.get_value_by_name(nombre) + 1)
        else:
            self.inventario.insert(1, nombre)

    def venderReplica(self, nombre: str):
        if self.inventario.search_name(nombre) and self.inventario.get_value_by_name(nombre) > 0:
            self.inventario.set_value_by_name(nombre, self.inventario.get_value_by_name(nombre) - 1)
            if self.inventario.get_value_by_name(nombre) == 0:
                self.inventario.delete(nombre)
        else:
            return 'No existe el producto'

    def listarReplicas(self):
        return self.inventario.printnames("Obra", "Cantidad disponible")
