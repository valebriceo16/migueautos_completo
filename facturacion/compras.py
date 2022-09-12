from facturacion.models import *

class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, insumo):
        id = str(insumo.id)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "producto_id": insumo.id,
                "nombre": insumo.nombre,
                "acumulado": insumo.precio,
                "suma_tot": 1,
                "estado": True,
            }
        else:
            self.carrito[id]["suma_tot"] += 1
            self.carrito[id]["acumulado"] += insumo.precio
            self.carrito[id]["estado"] = False
        self.guardar_carrito()

    def guardar_carrito(self):
        factura_id = Generar.objects.create()
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, insumo):
        id = str(insumo.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, insumo):
        id = str(insumo.id)
        if id in self.carrito.keys():
            self.carrito[id]["suma_tot"] -= 1
            self.carrito[id]["acumulado"] -= insumo.precio
            if self.carrito[id]["suma_tot"] <= 0: self.eliminar(insumo)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True