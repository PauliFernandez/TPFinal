from datetime import date
from guardar_cliente import Guardar_Cliente
from guardar_trabajo import Guardar_trabajo
import sys
class Menu:
    # Mostrar un menú y responder a las opciones
     def __init__(self):
        self.lista_clientes = Guardar_Cliente()
        self.lista_trabajo = Guardar_trabajo()
        self.opciones = {
            "1": self.mostrar_clientes,
            "2": self.nuevo_cliente,
            "3": self.modificar_cliente_particular,
            "4": self.modificar_cliente_corporativo,
            "5": self.buscar_cliente,
            "6": self.agregar_trabajo,
            "7": self.mostrar_trabajo,
            "8": self.modificar_trabajo,
            "9": self.trabajo_terminado,
            "10": self.trabajo_retirado,
            "11": self.buscar_trabajo,
            "12": self.informe
        }
     def mostrar_menu(self):
        print(
            """Menú del anotador:
        1. Mostrar clientes
        2. Nuevo cliente
        3. Modificar cliente particular
        4. Modificar cliente corporativo
        5. Buscar cliente
        6. Agregar trabajo
        7. Mostrar trabajo
        8. Modificar trabajo
        9. Terminar un trabajo
        10. Irabajo retirado
        11. Buscar trabajo
        12. Informe
        : """)

     def ejecutar(self):
        # Mostrar el menu y responder a las opciones.
        while True:
            self.mostrar_menu()
            opcion = input("Ingresar una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print("{0} no es una opción válida".format(opcion))

     def mostrar_clientes(self, lista=None):
        if lista == None:
            lista = self.lista_clientes.lista
        for cliente in lista:
            print(cliente)

     def nuevo_cliente(self):
        tipo = "A"
        while tipo not in ("C", "c", "P", "p"):
            tipo = input("Ingrese el tipo de cliente: C:Corporativo / P: Particular")
        nombre = input("Ingrese el nombre: ")
        if tipo in ("C", "c"):
             contacto = input("Ingrese el nombre del contacto: ")
             tc = input("Ingrese el teléfono del contacto: ")
        else:
                apellido = input("Ingrese el apellido: ")
        tel = input("Ingrese el teléfono: ")
        mail = input("Ingrese el correo electrónico: ")
        if tipo in ("C", "c"):
             c = self.lista_clientes.nuevo_cliente_corporativo(nombre, contacto, tc, tel, mail)
        else:
            c = self.lista_clientes.nuevo_cliente_particular(nombre, apellido, tel, mail)
        if c is None:
            print(" Error al cargar el cliente")
        else:
            print(c)
            print(" Cliente cargado correctamente")


     def modificar_cliente_particular(self):
         listas = self.lista_clientes.lista
         for clientec in listas:
             print(clientec)
         id_cliente = int(input("Ingrese el id del cliente que desea modificar"))
         if clientec.id_cliente == id_cliente:
                    opc = int(input(""""Elija una opción para modificar o eliminar un trabajo:
                                     1. Nombre
                                     2. Apellido
                                     3. Teléfono
                                     4. Mail
                                     5. Eliminar cliente
                                     0. Salir
                                     """))
                    if opc == 1:
                        nombre = input("Ingrese el nuevo nombre: ")
                        c = self.lista_clientes.modificar_nombre(nombre, id_cliente)
                        if c == None:
                            print("ERROR AL MODIFICAR CLIENTE")
                        else:
                            print("MODIFICADO CORRECTAMENTE")
                    if opc == 2:
                        apellido = input("Ingrese el nuevo apellido: ")
                        c = self.lista_clientes.modificar_apellido(apellido, id_cliente)
                        if c == None:
                            print("ERROR AL MODIFICAR CLIENTE")
                        else:
                            print("MODIFICADO CORRECTAMENTE")

                    if opc == 3:
                        telefono = input("Ingrese el nuevo telefono: ")
                        c = self.lista_clientes.modificar_telefono(telefono, id_cliente)
                        if c == None:
                            print("ERROR AL MODIFICAR CLIENTE")
                        else:
                            print("MODIFICADO CORRECTAMENTE")

                    if opc == 4:
                        mail = input("Ingrese el nuevo mail: ")
                        c = self.lista_clientes.modificar_mail(mail, id_cliente)
                        if c == None:
                            print("ERROR AL MODIFICAR CLIENTE")
                        else:
                            print("MODIFICADO CORRECTAMENTE")

                    if opc == 5:
                        c = self.lista_clientes.eliminar_cliente(id_cliente)
                        if c == None:
                            print("ERROR AL BORRAR CLIENTE")
                        else:
                            print("BORRADO CORRECTAMENTE")
         else:
                    print("El id no existe")

     def modificar_cliente_corporativo(self):
         listas = self.lista_clientes.lista
         for clientec in listas:
             print(clientec)
         id_cliente = int(input("Ingrese el id del cliente que desea modificar"))
         if clientec.id_cliente == id_cliente:
                 opc = int(input(""""Elija una opción para modificar o eliminar un trabajo:
                    1. Nombre empresa
                    2. Nombre contacto
                    3. Teléfono contacto
                    4. Teléfono
                    5. Mail
                    6. Eliminar cliente
                    0. Salir
                        """))
                 if opc == 1:
                  nombre_empresa = input("Ingrese el nuevo nombre de la empresa: ")
                  c = self.lista_clientes.modificar_nombre_empresa(nombre_empresa, id_cliente)
                  if c is None:
                            print("ERROR AL MODIFICAR CLIENTE")
                  else:
                             print("MODIFICADO CORRECTAMENTE")
                 if opc == 2:
                  nombre_contacto = input("Ingrese el nuevo nombre del contacto: ")
                  c = self.lista_clientes.modificar_nombre_empresa(nombre_contacto, id_cliente)
                  if c is None:
                            print("ERROR AL MODIFICAR CLIENTE")
                  else:
                            print("MODIFICADO CORRECTAMENTE")
                 if opc == 3:
                  telefono_contacto = input("Ingrese el nuevo teléfono del contacto: ")
                  c = self.lista_clientes.modificar_nombre_empresa(telefono_contacto, id_cliente)
                  if c is None:
                            print("ERROR AL MODIFICAR CLIENTE")
                  else:
                            print("MODIFICADO CORRECTAMENTE")
                 if opc == 4:
                  telefono = input("Ingrese el nuevo telefono: ")
                  c = self.lista_clientes.modificar_telefono(telefono, id_cliente)
                  if c is None:
                            print("ERROR AL MODIFICAR CLIENTE")
                  else:
                            print("MODIFICADO CORRECTAMENTE")

                 if opc == 5:
                  mail = input("Ingrese el nuevo mail: ")
                  c = self.lista_clientes.modificar_mail(mail, id_cliente)
                  if c is None:
                            print("ERROR AL MODIFICAR CLIENTE")
                  else:
                            print("MODIFICADO CORRECTAMENTE")
                 if opc == 6:
                  c = self.lista_clientes.eliminar_cliente(id_cliente)
                  if c is None:
                            print("ERROR AL BORRAR CLIENTE")
                  else:
                            print("BORRADO CORRECTAMENTE")
         else:
             print("El id no existe")

     def buscar_cliente(self):
         listas = self.lista_clientes.lista
         for clientec in listas:
             print(clientec)
         id_cliente = int(input("Ingrese el id del cliente que desea modificar"))
         if clientec.id_cliente == id_cliente:
            opc = int(input(""""Elija una opción para buscar un trabajo:
                                     1. Id cliente
                                     2. Teléfono
                                     3. Mail
                                     0. Salir """))
            if opc == 1:
                filtro = int(input("Buscar : "))
                for i in listas:
                    if i.id_cliente == filtro:
                        print(i)
                    else:
                        print("El id escrito no existe")
            if opc == 2:
                filtro = input("Buscar : ")
                for i in listas:
                    if i.telefono == filtro:
                        print(i)
                    else:
                        print("El id escrito no existe")
            if opc == 3:
                filtro = input("Buscar : ")
                for i in listas:
                    if i.mail == filtro:
                        print(i)
                    else:
                        print("El id escrito no existe")
         else:
             print("El id no existe")


     def agregar_trabajo(self):
        listatrabajo = self.lista_clientes.lista
        for clientet in listatrabajo:
            print(clientet)
        filtro = int(input("Buscar id: "))
        if clientet.id_cliente == filtro:
                cliente = clientet
                fecha_ingreso = date.today()
                print("Fecha de entrega propuesta")
                anio = int(input("Ingrese el año : "))
                mes = int(input("Ingrese el mes: "))
                dia = int(input("Ingrese el dia: "))
                fecha_entrega_propuesta = date(anio, mes, dia)
                descripcion = input("Ingrese una descirpción de trabajo: ")
                t = self.lista_trabajo.NuevoTrabajo(cliente, fecha_ingreso, fecha_entrega_propuesta, descripcion)
                if t is None:
                    print(" Error al cargar trabajo")
                else:

                    print(" Trabajo cargado correctamente")
        else:
            print("El id no existe")


     def buscar_trabajo(self):
         listatrabajo = self.lista_clientes.lista
         for clientet in listatrabajo:
             print(clientet)
         filtro = int(input("Buscar id: "))
         if clientet.id_cliente == filtro:
            opc = int(input(""""Elija una opción para buscar un trabajo:
                             1. Descripción
                             2. Fecha de ingreso
                             3. Eliminar trabajo
                             0. Salir """))

            if opc == 1:
                filtro = input("Buscar : ")
                for i in clientet:
                    if i.descripcion == filtro:
                        print(i)
            if opc == 2:
                filtro = int(input("Buscar : "))
                for i in clientet:
                    if i.id_trabajo == filtro:
                        print(i)
            if opc == 3:
                filtro = input("Buscar : ")
                for i in clientet:
                    if i.retirado == filtro:
                        print(i)
         else:
             print("El id no existe")

     def mostrar_trabajo(self, listatrabajo=None):
        if listatrabajo == None:
            listatrabajo = self.lista_trabajo.listatrabajo
        for trabajo in listatrabajo:
          print(trabajo)


     def modificar_trabajo(self):
         lista = self.lista_trabajo.listatrabajo
         for tr in lista:
             print(tr)
         id_trabajo = int(input("Ingrese el id del trabajo que desea modificar"))
         for i in lista:
            if i.id_trabajo == id_trabajo:
             opc = int(input(""""Elija una opción para modificar o eliminar un trabajo:
                     1. Descripción
                     2. Fecha de ingreso
                     3. Eliminar trabajo
                     0. Salir """))
             if opc == 1:
                    descrpicion = input("Ingrese la nueva descripción: ")
                    t = self.lista_trabajo.modificar_descripcion(descrpicion, id_trabajo)
                    if t == None:
                        print("ERROR AL MODIFICAR TRABAJO")
                    else:
                        print("MODIFICADO CORRECTAMENTE")
             if opc == 2:
                    anio = int(input("Ingrese el año : "))
                    mes = int(input("Ingrese el mes: "))
                    dia = int(input("Ingrese el dia: "))
                    t = self.lista_trabajo.modificar_fecha_ingreso(date(anio, mes, dia), id_trabajo)
                    if t == None:
                        print("ERROR AL MODIFICAR TRABAJO")
                    else:
                        print("MODIFICADO CORRECTAMENTE")
             if opc ==3:
                    t = self.lista_trabajo.eliminar_trabajo(id_trabajo)
                    if t == None:
                        print("ERROR AL BORRAR CLIENTE")
                    else:
                        print("BORRADO CORRECTAMENTE")


     def trabajo_terminado(self):
        print("Indicar un trabajo que fue terminado")
        lista = self.lista_trabajo.listatrabajo
        for tr in lista:
            print(tr)
        id_trabajo = int(input("Ingrese el id del trabajo"))
        for i in lista:
            if i.id_cliente == id_trabajo:
                fecha_entrega_real = date.today()
                t = self.lista_trabajo.trabajo_terminado(fecha_entrega_real, id_trabajo)
                if t == None:
                            print("ERROR AL TERMINAR TRABAJO")
                else:
                            print("TRABAJO TERMINADO CORRECTAMENTE")

     def trabajo_retirado(self):
         print("Indicar si el trabajo fue retirado")
         lista = self.lista_trabajo.listatrabajo
         for tr in lista:
             print(tr)
         id_trabajo = int(input("Ingrese el id del trabajo que desea modificar"))
         for i in lista:
             if i.id_cliente == id_trabajo:
                 t = self.lista_trabajo.trabajo_entregado(True, id_trabajo)
                 if t == None:
                        print("ERROR AL TERMINAR TRABAJO")
                 else:
                        print("TRABAJO TERMINADO CORRECTAMENTE")

     def informe(self):
         for listaS in self.lista_clientes.lista:
          print(listaS)
         listat = self.lista_trabajo.listatrabajo
         id = int(input("Ingrese el id del cliente: "))
         for i in listat:
            if i.cliente.id_cliente == id:
                    print("ID trabajo: ", i.id_trabajo)
                    print("Descripción", i.descripcion)
                    print("Fecha de ingreso", i.fecha_ingreso)
                    print ("fecha de entrega propuesta", i.fecha_entrega_propuesta)
                    print("fecha de entrega real", i.fecha_entrega_real)
                    print("retirado", i.retirado)




     def salir(self):
        print("Gracias por utilizar el sistema.")
        sys.exit(0)

if __name__ == "__main__":
    m= Menu()
    m.ejecutar()










