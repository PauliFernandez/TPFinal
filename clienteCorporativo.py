#! /usr/bin/env python3
from cliente import Cliente

class ClienteCorporativo(Cliente):
    '''Representa un cliente particular'''
    def __init__(self, nombre_empresa, nombre_contacto, telefono_contacto,
            telefono, mail, id_cliente = None):
        self.nombre_empresa = nombre_empresa
        self.nombre_contacto = nombre_contacto
        self.telefono_contacto = telefono_contacto
        super().__init__(telefono, mail, id_cliente)

    def __str__(self):
        cadena = f"ID del cliente: {self.id_cliente} \nNombre empresa: {self.nombre_empresa}\nTipo de cliente: (Cliente corporativo)\n"
        cadena += f"Teléfono: {self.telefono}\n Mail: {self.mail}\n"
        cadena += f"Contacto:\n Nombre contacto: {self.nombre_contacto}\n Teléfono contacto: {self.telefono_contacto} \n"
        return cadena

