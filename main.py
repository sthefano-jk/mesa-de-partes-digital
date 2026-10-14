"""Mesa de partes digital - versión básica (avance hasta la semana 10).
Ejecutar con: python main.py
"""

# Arreglos paralelos: la posición i de cada lista describe el MISMO documento.
codigos = []
nombres = []
dnis = []
tipos = []
asuntos = []
fechas = []


def registrar_documento():
    print("\n--- Registrar documento ---")

    nombre = input("Nombre y apellidos: ").strip()
    while nombre == "":
        nombre = input("El nombre es obligatorio. Nombre y apellidos: ").strip()

    dni = input("DNI (8 dígitos): ").strip()
    while len(dni) != 8 or not dni.isdigit():
        dni = input("DNI inválido. DNI (8 dígitos): ").strip()

    print("Tipo de trámite:")
    print(" - Matrícula o traslado")
    print(" - Solicitud de certificados o constancias")
    print(" - Solicitud de documentos académicos")
    print(" - Reclamo o sugerencia")
    tipo = input("Escriba el tipo: ").strip()
    asunto = input("Asunto: ").strip()
    fecha = input("Fecha (DD/MM/AAAA): ").strip()

    # El código es el número de orden: el primer documento es el 1, el segundo el 2...
    codigo = str(len(codigos) + 1)

    codigos.append(codigo)
    nombres.append(nombre)
    dnis.append(dni)
    tipos.append(tipo)
    asuntos.append(asunto)
    fechas.append(fecha)

    print("\n===== CARGO DE RECEPCIÓN =====")
    print("Código : " + codigo)
    print("Nombre : " + nombre)
    print("Fecha  : " + fecha)
    print("Conserve este código para consultar su trámite")
    print("==============================")


def buscar_documento():
    print("\n--- Buscar por código ---")
    buscado = input("Código a buscar: ").strip()

    posicion = -1
    for i in range(len(codigos)):
        if codigos[i] == buscado:
            posicion = i

    if posicion == -1:
        print("No existe ese código")
    else:
        print("Código : " + codigos[posicion])
        print("Nombre : " + nombres[posicion])
        print("DNI    : " + dnis[posicion])
        print("Trámite: " + tipos[posicion])
        print("Asunto : " + asuntos[posicion])
        print("Fecha  : " + fechas[posicion])


def main():
    opcion = ""
    while opcion != "3":
        print("\nMESA DE PARTES DIGITAL")
        print("1) Registrar documento")
        print("2) Buscar por código")
        print("3) Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            registrar_documento()
        elif opcion == "2":
            buscar_documento()
        elif opcion == "3":
            print("Hasta luego")
        else:
            print("Opción no válida")


main()