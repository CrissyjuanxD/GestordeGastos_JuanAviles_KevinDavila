
class GestoGastos:
    def __init__(self):
        #Creamos la lista que contendrá los gastos
        self.gastos = []
    #Creamos el método que servirá para agregar los gastos
    def agregar_gastos(self, categoria, nombre, monto, fecha):
        self.gastos.append({"categoria": categoria, "nombre": nombre, "monto": monto, "fecha": fecha})
        return self.gastos

    #Creamos el método que servirá para visualizar los gastos
    def visualizar_gastos(self):
        if len(self.gastos) > 0:
            sumaCategorias = {}
            for categorias in self.gastos:
                categoria = categorias['categoria']
                cantidad = categorias['monto']
                #Verifica si la categoria existe en el diccionario
                if categoria in sumaCategorias:
                    sumaCategorias[categoria] += cantidad
                else:
                    #Si la categoria existe en el diccionario, suma la cantidad
                    sumaCategorias[categoria] = cantidad
            #Devuelve el diccionario con las categorias y la suma de los gastos
            return sumaCategorias
        else:
            #Si la lista de gastos no contiene elementos, devuelve un diccionario vacio
            return {}

    def visualizar_resumen_mensual(self, mes):
        VerificarGastos = False
        if len(self.gastos) > 0:
            mes_anio = mes
            resumen_mensual = {'Servicios': 0,
                               'Alimentos': 0,
                               'Educacion': 0,
                               'Transporte': 0,
                               'Trabajo': 0,
                               'Salud': 0,
                               'Otro Pago': 0}
            for gasto in self.gastos:
                fecha_gasto = gasto['fecha']
                if fecha_gasto.startswith(mes_anio):
                    VerificarGastos=True
                    categoria = gasto['categoria']
                    cantidad = gasto['monto']
                    if categoria in resumen_mensual:
                        resumen_mensual[categoria] += cantidad
            if VerificarGastos:
                return resumen_mensual
            else:
                return {}
        else:
            return {}