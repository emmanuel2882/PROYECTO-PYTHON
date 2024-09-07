def solicitar_datos():
    departamento = input("Ingrese el departamento: ")
    municipio = input("Ingrese el municipio: ")
    cultivo = input("Ingrese el tipo de cultivo: ")
    limit = int(input("Ingrese el número de registros a consultar: "))
    return departamento, municipio, cultivo, limit

