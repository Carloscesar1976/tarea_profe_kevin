class Curso:
    def __init__(self, titulo, descripcion, objetivos, programa, costo, duracion_en_meses, foto, estado, fecha_de_comienzo):
        self._titulo = titulo
        self._descripcion = descripcion
        self._objetivos = objetivos
        self._programa = programa
        self._costo = costo
        self._duracion_en_meses = duracion_en_meses
        self._foto = foto
        self._estado = estado
        self._fecha_de_comienzo = fecha_de_comienzo

    
    def get_titulo(self):
        return self._titulo

    def get_descripcion(self):
        return self._descripcion

    def get_objetivos(self):
        return self._objetivos

    def get_programa(self):
        return self._programa

    def get_costo(self):
        return self._costo

    def get_duracion_en_meses(self):
        return self._duracion_en_meses

    def get_foto(self):
        return self._foto

    def get_estado(self):
        return self._estado

    def get_fecha_de_comienzo(self):
        return self._fecha_de_comienzo

    def set_titulo(self, titulo):
        self._titulo = titulo

    def set_descripcion(self, descripcion):
        self._descripcion = descripcion

    def set_objetivos(self, objetivos):
        self._objetivos = objetivos

    def set_programa(self, programa):
        self._programa = programa

    def set_costo(self, costo):
        self._costo = costo

    def set_duracion_en_meses(self, duracion_en_meses):
        self._duracion_en_meses = duracion_en_meses

    def set_foto(self, foto):
        self._foto = foto

    def set_estado(self, estado):
        self._estado = estado

    def set_fecha_de_comienzo(self, fecha_de_comienzo):
        self._fecha_de_comienzo = fecha_de_comienzo


curso1 = Curso("Programacion inicial", "introducciom a Python", 
               "Aprender los conceptos básicos de Python", "Temario detallado",
                 3000, "2 meses", "imagen.png", "Activo", "2023-09-10")


print(curso1.get_titulo())  
curso1.set_costo(3000) 
print(curso1.get_costo())  







class Categoria:
    def __init__(self,inicial,intermedio,avanzado):
        self._inicial = inicial
        self._intermedio = intermedio
        self._avanzado = avanzado

    def get_inicial(self):
        return self._inicial

    def set_inicial(self, valor):
        self._inicial = valor

    def get_intermedio(self):
        return self._intermedio

    def set_intermedio(self, valor):
        self._intermedio = valor

    def get_avanzado(self):
        return self._avanzado

    def set_avanzado(self, valor):
        self._avanzado = valor

mi_categoria = Categoria(inicial=1,intermedio=2,avanzado=3)

mi_categoria.set_inicial("Dos meses ")
mi_categoria.set_intermedio("Cuatro meses")
mi_categoria.set_avanzado("Ocho meses")


print("Nivel Inicial:", mi_categoria.get_inicial())
print("Nivel Intermedio:", mi_categoria.get_intermedio())
print("Nivel Avanzado:", mi_categoria.get_avanzado())






class Clase:
    def __init__(self, fecha, titulo, contenido, url_drive):
        self._fecha = fecha
        self._titulo = titulo
        self._contenido = contenido
        self._url_drive = url_drive

    def get_fecha(self):
        return self._fecha

    def set_fecha(self, nueva_fecha):
        self._fecha = nueva_fecha

    def get_titulo(self):
        return self._titulo

    def set_titulo(self, nuevo_titulo):
        self._titulo = nuevo_titulo

    def get_contenido(self):
        return self._contenido

    def set_contenido(self, nuevo_contenido):
        self._contenido = nuevo_contenido

    def get_url_drive(self):
        return self._url_drive

    def set_url_drive(self, nueva_url_drive):
        self._url_drive = nueva_url_drive

mi_clase = Clase("2023-09-03", "clases", 
                 "Contenido de ejemplo", "https://drive.google.com/000000")
print(mi_clase.get_titulo())  
mi_clase.set_titulo("Materias")  
print(mi_clase.get_titulo())  
print(mi_clase.get_url_drive())






class Docente:
    def __init__(self, apellido, nombre, dni, fecha_de_nac, direccion, localidad, cod_postal, provincia, celular, email, clave_de_acceso, confirmar_clave, confirmar_email):
        self._apellido = apellido
        self._nombre = nombre
        self._dni = dni
        self._fecha_de_nac = fecha_de_nac
        self._direccion = direccion
        self._localidad = localidad
        self._cod_postal = cod_postal
        self._provincia = provincia
        self._celular = celular
        self._email = email
        self._clave_de_acceso = clave_de_acceso
        self._confirmar_clave = confirmar_clave
        self._confirmar_email = confirmar_email

    
    def get_apellido(self):
        return self._apellido

    def set_apellido(self, nuevo_apellido):
        self._apellido = nuevo_apellido

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    def get_dni(self):
        return self._dni

    def set_dni(self, nuevo_dni):
        self._dni = nuevo_dni

    def get_fecha_de_nac(self):
        return self._fecha_de_nac

    def set_fecha_de_nac(self, nueva_fecha_de_nac):
        self._fecha_de_nac = nueva_fecha_de_nac

    def get_direccion(self):
        return self._direccion

    def set_direccion(self, nueva_direccion):
        self._direccion = nueva_direccion

    def get_localidad(self):
        return self._localidad

    def set_localidad(self, nueva_localidad):
        self._localidad = nueva_localidad

    def get_cod_postal(self):
        return self._cod_postal

    def set_cod_postal(self, nuevo_cod_postal):
        self._cod_postal = nuevo_cod_postal

    def get_provincia(self):
        return self._provincia

    def set_provincia(self, nueva_provincia):
        self._provincia = nueva_provincia

    def get_celular(self):
        return self._celular

    def set_celular(self, nuevo_celular):
        self._celular = nuevo_celular

    def get_email(self):
        return self._email

    def set_email(self, nuevo_email):
        self._email = nuevo_email

    def get_clave_de_acceso(self):
        return self._clave_de_acceso

    def set_clave_de_acceso(self, nueva_clave_de_acceso):
        self._clave_de_acceso = nueva_clave_de_acceso

    def get_confirmar_clave(self):
        return self._confirmar_clave

    def set_confirmar_clave(self, nueva_confirmar_clave):
        self._confirmar_clave = nueva_confirmar_clave

    def get_confirmar_email(self):
        return self._confirmar_email

    def set_confirmar_email(self, nueva_confirmar_email):
        self._confirmar_email = nueva_confirmar_email


docente = Docente("Perez", "Juan", "12345678", "1990-01-15", "Calle 123", 
                  "Ciudad", "12345", "Provincia", "123-456-7890",
                    "juan@example.com", "password123", "password123", "juan@example.com")
print(docente.get_nombre())  
docente.set_nombre("Pedro")  
print(docente.get_nombre())  






class Usuario:
    def __init__(self, administrador=False, docente=False, activo=False, inactivo=False):
        self._administrador = administrador
        self._docente = docente
        self._activo = activo
        self._inactivo = inactivo

    def es_administrador(self):
        return self._administrador

    def set_administrador(self, estado):
        self._administrador = estado

    def es_docente(self):
        return self._docente

    def set_docente(self, estado):
        self._docente = estado

    def esta_activo(self):
        return self._activo

    def set_activo(self, estado):
        self._activo = estado

    def esta_inactivo(self):
        return self._inactivo

    def set_inactivo(self, estado):
        self._inactivo = estado

usuario = Usuario(administrador=True, activo=True)
print(usuario.es_administrador())  
print(usuario.esta_activo())  

usuario.set_docente(True)
usuario.set_inactivo(True)

print(usuario.es_docente())  
print(usuario.esta_inactivo())  







class CarritoDeCompra:
    def __init__(self, foto=None, titulo_del_curso=None, duracion=0, costo=0.0):
        self._foto = foto
        self._titulo_del_curso = titulo_del_curso
        self._duracion = duracion
        self._costo = costo

    
    def obtener_foto(self):
        return self._foto

    def establecer_foto(self, foto):
        self._foto = foto

    def obtener_titulo_del_curso(self):
        return self._titulo_del_curso

    def establecer_titulo_del_curso(self, titulo):
        self._titulo_del_curso = titulo

    def obtener_duracion(self):
        return self._duracion

    def establecer_duracion(self, duracion):
        self._duracion = duracion

    def obtener_costo(self):
        return self._costo

    def establecer_costo(self, costo):
        self._costo = costo

carrito = CarritoDeCompra()
carrito.establecer_foto("imagen_curso.jpg")
carrito.establecer_titulo_del_curso("Curso de Python")
carrito.establecer_duracion(30)
carrito.establecer_costo(3000)

print("Foto:", carrito.obtener_foto())
print("Título del curso:", carrito.obtener_titulo_del_curso())
print("Duración:", carrito.obtener_duracion(), "días")
print("Costo:", carrito.obtener_costo(), "$")







class MediosDePago:
    def __init__(self, tarjeta_de_debito, tarjeta_de_credito, transferencia):
        self._tarjeta_de_debito = tarjeta_de_debito
        self._tarjeta_de_credito = tarjeta_de_credito
        self._transferencia = transferencia

    def get_tarjeta_de_debito(self):
        return self._tarjeta_de_debito

    def set_tarjeta_de_debito(self, estado):
        self._tarjeta_de_debito = estado

    def get_tarjeta_de_credito(self):
        return self._tarjeta_de_credito

    def set_tarjeta_de_credito(self, estado):
        self._tarjeta_de_credito = estado

    def get_transferencia(self):
        return self._transferencia

    def set_transferencia(self, estado):
        self._transferencia = estado







class DatosMediosDePago:
    def __init__(self, nombre_del_banco="", numero_de_tarjeta="", 
                 monto_a_pagar=0.0, nombre_del_titular="", fecha_vencimiento_tarjeta=""):
        self._nombre_del_banco = nombre_del_banco
        self._numero_de_tarjeta = numero_de_tarjeta
        self._monto_a_pagar = monto_a_pagar
        self._nombre_del_titular = nombre_del_titular
        self._fecha_vencimiento_tarjeta = fecha_vencimiento_tarjeta

    
    def get_nombre_del_banco(self):
        return self._nombre_del_banco

    def establecer_nombre_del_banco(self, nombre):
        self._nombre_del_banco = nombre

    def get_numero_de_tarjeta(self):
        return self._numero_de_tarjeta

    def establecer_numero_de_tarjeta(self, numero):
        self._numero_de_tarjeta = numero

    def get_monto_a_pagar(self):
        return self._monto_a_pagar

    def establecer_monto_a_pagar(self, monto):
        self._monto_a_pagar = monto

    def get_nombre_del_titular(self):
        return self._nombre_del_titular

    def establecer_nombre_del_titular(self, nombre):
        self._nombre_del_titular = nombre

    def get_fecha_vencimiento_tarjeta(self):
        return self._fecha_vencimiento_tarjeta

    def establecer_fecha_vencimiento_tarjeta(self, fecha):
        self._fecha_vencimiento_tarjeta = fecha

datos_pago = DatosMediosDePago()
datos_pago.establecer_nombre_del_banco("Banco Galicia")
datos_pago.establecer_numero_de_tarjeta("1234 5678 9012 3456")
datos_pago.establecer_monto_a_pagar(3000)
datos_pago.establecer_nombre_del_titular("Juan Pérez")
datos_pago.establecer_fecha_vencimiento_tarjeta("12/25")

print("Nombre del banco:", datos_pago.get_nombre_del_banco())
print("Número de tarjeta:", datos_pago.get_numero_de_tarjeta())
print("Monto a pagar:", datos_pago.get_monto_a_pagar())
print("Nombre del titular:", datos_pago.get_nombre_del_titular())
print("Fecha de vencimiento de la tarjeta:", datos_pago.get_fecha_vencimiento_tarjeta())






class ConfirmarCompra:
    def __init__(self, fecha_de_compra="", nombre_de_titular="", monto_total=0.0):
        self._fecha_de_compra = fecha_de_compra
        self._nombre_de_titular = nombre_de_titular
        self._monto_total = monto_total

    def get_fecha_de_compra(self):
        return self._fecha_de_compra

    def set_fecha_de_compra(self, fecha):
        self._fecha_de_compra = fecha

    def get_nombre_de_titular(self):
        return self._nombre_de_titular

    def set_nombre_de_titular(self, nombre):
        self._nombre_de_titular = nombre

    def get_monto_total(self):
        return self._monto_total

    def set_monto_total(self, monto):
        self._monto_total = monto

confirmacion_compra = ConfirmarCompra()
confirmacion_compra.set_fecha_de_compra("2023-09-03")
confirmacion_compra.set_nombre_de_titular("Juan Pérez")
confirmacion_compra.set_monto_total(3000)

print("Fecha de compra:", confirmacion_compra.get_fecha_de_compra())
print("Nombre del titular:", confirmacion_compra.get_nombre_de_titular())
print("Monto total:", confirmacion_compra.get_monto_total())
















