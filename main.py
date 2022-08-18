
diccionario = {"codigo": ["001", "002", "003", "004", "005"],
          "nombre": ["Luis", "Javier", "Pedro", "Juan", "Carlos" ],
         "Curso": ["Comunicacion", "Matematica", " Historia", "Ciencia"," Ingles"]}
nota_ = []
resp = "s"
while resp == "s":
    codigo= input("Ingresar el codigo del alumno: ")
    curso = input("Ingresa el nombre del curso: ")
    nota1 = int(input("Ingrese la primera nota : "))
    nota2 = int(input("Ingrese la segunda nota: "))
    nota3 = int(input("Ingrese la tercera nota: "))
    nota4 = int(input("Ingrese la cuarta nota: "))
    x = 0
    for i in diccionario["codigo"]:
        if i == codigo:
            codigoTemp = i
            nombreTemp = diccionario["nombre"][x]
            promedio = (nota1 + nota2 + nota3 + nota4)/4
            registro = ["Codigo: " + str(codigoTemp) + " | " + "Nombre :" + str(nombreTemp) + " | " + "Curso :" + curso + " | " + "Promedio: " + str(promedio) + " | " +"Nota 1: " + str(nota1) + "| " + "Nota 2: " + str(nota2) + " | " + "Nota 3: " + str(nota3) + " | " + "Nota 4: " + str(nota4)]
            f = open("examen", "a")
            cadena = "".join(registro)
            f.write("\n" + cadena)
            f.close()
        x += 1

    f = open("examen")
    print(f.read())
    f.close()