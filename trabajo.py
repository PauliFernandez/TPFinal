#! /usr/bin/python3
from guardar_trabajo import Guardar_trabajo
import datetime

class Trabajo:
    '''Representa un trabajo de reparación que realizará el taller'''
    def __init__(self, cliente, fecha_ingreso, fecha_entrega_propuesta,
        fecha_entrega_real, descripcion, retirado, id_trabajo = None):
        ''' Recibe un objeto cliente, una fecha de ingreso (objeto datetime),
        otros dos objetos datetime con la fecha de entrega propuesta y real, 
        una descripción, un valor "retirado" (True o False) y un id opcional'''
        self.cliente = cliente
        self.fecha_ingreso = fecha_ingreso
        self.fecha_entrega_propuesta = fecha_entrega_propuesta
        self.fecha_entrega_real = fecha_entrega_real
        self.descripcion = descripcion
        self.retirado = retirado
        self.id_trabajo = id_trabajo

    def _buscar_por_id(self, id_nota):
        '''Buscar la nota con el id dado'''
        for buscar_id in self.gurdar_trabajo:
            if buscar_id.id == int(id_trabajo):
                return buscar_id

        return None

    def modificar_descripcion(self, descripcion, id_trabajo):
        trabajo = self._buscar_por_id(id_trabajo)
        if trabajo:
            trabajo.descripcion = descripcion
            return True
        return False

    def modificar_descripcion(self, descripcion, id_trabajo):
        trabajo = self._buscar_por_id(id_trabajo)
        if trabajo:
            trabajo.descripcion = descripcion
            return True
        return False
    

