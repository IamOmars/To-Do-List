class Menu:
    cedulas = []
    usuarios = []
    contrasenas = []
    taskes = []

    print("Escoge una de las opciones: ")
    print("1. Registrar un usuario.")
    print("2. Iniciar sesion.")
    print("3. Crear una tarea.")
    print("4. Obtener todas las tareas.")
    print("5. Actualizar una tarea.")
    print("6. Eliminar una tarea.")

    abc = True

    opc = int(input())
    while abc == True:
        if opc == 1:
            print("Ingrese el ID, username y password del nuevo usuario: ")
            id = int(input())
            username = str(input())
            password = str(input())
            cedulas.append(id)
            usuarios.append(username)
            contrasenas.append(password)
        elif opc == 2:
            print("Ingrese el ID del usuario que desee buscar: ")
            search = input(" ")
            cedulas.index(search)
            print(cedulas.index(search))
        elif opc == 3:
            print("Ingrese el numero identificador de la tarea que quiere crear.")
            idTask = int(input())
            print("Ingresa el titulo de la tarea.")
            titleTask = str(input())
            print("Ingrese la descripcion de la tarea.")
            descTask = str(input())
            print("La tarea ya ha sido completada?")
            isCompleted = str(input())
            if isCompleted == ("Si"):
                completed = True
            else:
                completed = False
            print("Para que fecha se vence la tarea?: ")
            DueDate = str(input())
        elif opc == 4:
            print("Ingrese el ID de la tarea que desea buscar: ")
            searchTask = int(input())
            taskes.index(searchTask)
        elif opc == 5:
            print("Ingrese el ID de la tarea que desee modificar: ")
            searchID = int(input())
            if taskes.index(searchID):
                print("Ingresa el titulo de la tarea.")
                titleTask = str(input())
                print("Ingrese la descripcion de la tarea.")
                descTask = str(input())
                print("La tarea ya ha sido completada?")
                isCompleted = str(input())
                if isCompleted == ("Si"):
                    completed = True
                else:
                    completed = False
                print("Para que fecha se vence la tarea?: ")
                DueDate = str(input())
                taskes.append[titleTask, descTask, completed, DueDate]
            else:
                print("El ID de la tarea no existe.")
        elif opc == 6:
            print("Ingrese el ID de la tarea que desee eliminar: ")
            searchID = int(input())
            if taskes.index(searchID):
                taskes.remove(taskes)