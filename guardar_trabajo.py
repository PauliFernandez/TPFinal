from datetime import date
import datetime
from trabajo import Trabajo
from repositorioTrabajos import RepositorioTrabajos
class Guardar_trabajo:
    def __init__(self):
        self.rt = RepositorioTrabajos()
        self.listatrabajo = self.rt.get_all()

    def NuevoTrabajo(self, cliente, fecha_ingreso, fecha_entrega_propuesta, descripcion):
        ''' Crea un nuevo trabajo, lo agrega a la lista y a la Base de Datos'''
        t = Trabajo(cliente, fecha_ingreso, fecha_entrega_propuesta, None, descripcion, None)
        t.id_trabajo = self.rt.store(t)
        if t.id_trabajo == 0:
            return None
        else:
            self.listatrabajo.append(t)
            return t

    def buscar_por_id(self, id_trabajo):
        '''Buscar al cliente con el id dado'''
        for buscar_id in self.listatrabajo:
            if buscar_id.id_trabajo == int(id_trabajo):
                return (buscar_id)
        return None

    def modificar_descripcion(self, descripcion, id_trabajo):
        t = self.buscar_por_id(id_trabajo)
        if t:
            t.descripcion = descripcion
            return self.rt.update(t)
        return False
