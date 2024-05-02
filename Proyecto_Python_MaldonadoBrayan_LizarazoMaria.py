#Proyecto para el filtro de Python

#Importación de librerias
import json
from os import system

#Definición de funciones
def abrirArchivo(): #Función que va a servir para abrir el archivo
    miJSON=[]
    with open('mainIndex.json','r',encoding='utf-8') as openfile:
        miJSON = json.load(openfile)
    return miJSON

def guardarArchivo(miData): #Función que va a servir para guardar los datos que se realicen al archivo
    with open("mainIndex.json","w",encoding='utf-8') as outfile:
        json.dump(miData,outfile)

#=============================== INICIO DEL PROGRAMA ======================================

#Entrada en la que el usuario va a ingresar el rol que tiene para así saber qué opciones mostrarle
boolUsuario = True
TipoUsuario = ""
while boolUsuario == True: #Se le va a preguntar el tipo de Rol hasta que ingrese un valor válido
    RolUsuario = int(input("¿Cuál es su rol dentro de CampusLands?\n 1. Camper\n 2. Trainer\n 3. Coordinador\n"))
   
    if RolUsuario == 1: #Dependiendo de la elección numerica, esta va a tomar un valor de texto
        TipoUsuario = "Camper"
        boolUsuario = False

    elif RolUsuario == 2: 
        TipoUsuario = "Trainer"
        boolUsuario = False

    elif RolUsuario == 3:
        TipoUsuario = "Coordinador"
        boolUsuario = False

    else:
        print("Este no es un número válido")
        input("Presione ENTER para continuar")
        system("cls")

print("Hola", TipoUsuario)
print("")






#=================================== MODULO DEL CAMPER ===========================================================
 
if RolUsuario == 1:
    system("cls")
    print("---CAMPER---")
    print("")
    print(""" 
MENÚ DEL CAMPER
1. Ver notas
2. Ver Ruta de Estudio.
3. Ver Horario y salon de clases.
4. Ver módulo en el que está registrado
5. Salir.
          """)
    





#=================================== MODULO DEL TRAINER ===========================================================
elif RolUsuario == 2:
    system("cls")
    boolTrainer = True
    while boolTrainer == True: 
        print("---TRAINER---")
        print("")
        print(""" 
MENÚ DEL TRAINER
1. Ver Grupos.
5.Salir.
          """)
        eleccionTrainer = int(input("¿Qué desea hacer: ?"))
        system("cls")

        #=========================== VER GRUPOS Y LOS ESTUDIANTES QUE HAY DENTRO ==================================
        if eleccionTrainer == 1:

            GeneralData = abrirArchivo()
            GrupoT1 = {}
            GrupoT2 = {}
            GrupoT3 = {}
            #Se guardan los estudiantes en el salon que correspondan
            for i in range (len(GeneralData[3]["Estudiantes"])):
                if GeneralData[3]["Estudiantes"][i]["Grupo"] == "T1":
                    GrupoT1 = (GeneralData[3]["Estudiantes"])

                elif GeneralData[3]["Estudiantes"][i]["Grupo"] == "T2":
                    GrupoT2 = (GeneralData[3]["Estudiantes"])
                
                elif GeneralData[3]["Estudiantes"][i]["Grupo"] == "T3":
                    GrupoT3 = (GeneralData[3]["Estudiantes"])
            GeneralData[6]["Grupos"][0]["GrupoT1"]= GrupoT1
            GeneralData[6]["Grupos"][1]["GrupoT2"]= GrupoT2
            GeneralData[6]["Grupos"][2]["GrupoT3"]= GrupoT3
            guardarArchivo(GeneralData)

            print ("GRUPOS"),print()
            GeneralData = abrirArchivo() #Mostrar los grupos
            print("GRUPO T1"),print("")
            contador = 0
            for i in GeneralData[6]["Grupos"][0]["GrupoT1"]:
                contador+=1
                print("Estudiante #",contador)
                print("Nombres:",i["Nombres"]),print("Apellidos:",i["Apellidos"]),print("Grupo:",i["Grupo"]),print("Salon:",i["Salon"]),print("Trainer:",i["Trainer"])
                print("================")
            
            print("GRUPO T2"),print("")
            contador = 0
            for i in GeneralData[6]["Grupos"][1]["GrupoT2"]:
                contador+=1
                print("Estudiante #",contador)
                print("Nombres:",i["Nombres"]),print("Apellidos:",i["Apellidos"]),print("Grupo:",i["Grupo"]),print("Salon:",i["Salon"]),print("Trainer:",i["Trainer"])
                print("================")

            print("GRUPO T3"),print("")
            contador = 0
            for i in GeneralData[6]["Grupos"][2]["GrupoT3"]:
                contador+=1
                print("Estudiante #",contador)
                print("Nombres:",i["Nombres"]),print("Apellidos:",i["Apellidos"]),print("Grupo:",i["Grupo"]),print("Salon:",i["Salon"]),print("Trainer:",i["Trainer"])
                print("================")

        elif eleccionTrainer == 5:
            print("Saliendo del módulo del trainer")
            input("Presione ENTER para continuar")
            boolTrainer = False





               
#=================================== MODULO DEL COORDINADOR ===========================================================
elif RolUsuario == 3:
    system("cls")
    boolCoordinador = True
    while boolCoordinador == True:
        print("---COORDINADOR---")
        print("")
        print(""" 
    MENÚ DEL TRAINER
    1. Registrar nuevo Camper.
    2. Ingresar Nota de la prueba inicial al Camper.
    3. Añadir Ruta de Estudio a los Campers, asignación de trainer, salon y definicion de horario.
    4. Salir del módulo de coordinador.
            """)
        eleccionCoordinador = int(input("¿Qué desea hacer?: "))
        system("cls")

        #=====Crear Nuevo Camper=====
        if eleccionCoordinador == 1:
            print("---REGISTRAR CAMPER A INSCRITOS---")
            GeneralData = abrirArchivo()
            GeneralData[2]["Estudiantes"].append ({
                    "Identificador" : len(GeneralData[2]["Estudiantes"])+1,
                    "Estado" : "Inscrito",
                    "Documento": (input("Ingrese su documento: ")),
                    "Nombres": (input("Ingrese los Nombres del Camper: ")),
                    "Apellidos": (input("Ingrese los apellidos del Camper: ")),
                    "Direccion": (input("Ingrese la dirección del Camper: ")),
                    "Acudiente": (input("Ingrese el nomnbre de el/la acudiente del Camper: ")),
                    "Celular": input("Ingrese el número de celular del Camper: "),
                    "Fijo": input("Ingrese el telefono fijo del Camper: "),
                    "NotaPrueba" : 0
                    })
            guardarArchivo(GeneralData)
            print("Camper Registrado!")
            print("")
            input("Presione ENTER para continuar")
            system("cls")
            break
    
        #INGRESAR NOTA DE LA PRUEBA INICIAL
        elif eleccionCoordinador == 2: 
            GeneralData = abrirArchivo()
            print("---INGRESAR LA NOTA DE LA PRUEBA INICIAL---")
            contador = 0 
            for i in GeneralData[2]["Estudiantes"]:
                contador+=1
                print("==========================")
                print("Idetinficador:",contador)
                print("Documento:",i["Documento"])
                print("Nombres",i["Nombres"])
                print("Apellidos",i["Apellidos"]) 
            print("==========================")
            CamperParaNota = int(input("Ingrese el identificador del Camper: "))
            PruebaTeorica = int(input("Ingrese la nota de la prueba teorica: "))
            PruebaPractica = int(input("Ingrese la nota de la prueba practica: ")) 
            NotaCamper = (PruebaPractica+PruebaTeorica)/2 #La nota de la prueba general del camper es el prom de las dos que realizó
            GeneralData[2]["Estudiantes"][CamperParaNota-1]["NotaPrueba"] = NotaCamper
            guardarArchivo(GeneralData)
            print("Nota Agregada!")
            input("Presione ENTER para continuar")
            system("cls")

            AprobadosInicial = {}
            ReprobadosInicial = {}
            SigueEnInscrito = {}

            GeneralData = abrirArchivo()
            for i in range (len(GeneralData[2]["Estudiantes"])-1):
                
                GeneralData = abrirArchivo()
                if GeneralData[2]["Estudiantes"][i]["NotaPrueba"]>=60:
                    ListarAprobados = GeneralData[2]["Estudiantes"]
                    AprobadosInicial = GeneralData[2]["Estudiantes"][i] #Dependiendo de la nota que se le dé al camper 
                    GeneralData[3]["Estudiantes"] = AprobadosInicial #Se va a añadir a la lista de "Cursando"
                    GeneralData[2]["Estudiantes"][i]["Estado"] = "Aprobado" # o a la de "Expulsados"
                    del GeneralData[2]["Estudiantes"][i]
                    guardarArchivo(GeneralData)

                    GeneralData = abrirArchivo()
                elif GeneralData[2]["Estudiantes"][i]["NotaPrueba"]<=59 and GeneralData[2]["Estudiantes"][i]["NotaPrueba"]!=0: #Primero se Guardan en un diccionario y posteriormente
                    ReprobadosInicial = GeneralData[2]["Estudiantes"][i] #se agregan al json
                    GeneralData[4]["Estudiantes"] = ReprobadosInicial
                    GeneralData[2]["Estudiantes"][i]["Estado"] = "Reprobado"
                    del GeneralData[2]["Estudiantes"][i]
                    guardarArchivo(GeneralData)
                
                    GeneralData = abrirArchivo()
                elif GeneralData[2]["Estudiantes"][i]["NotaPrueba"] == 0: 
                    SigueEnInscrito = GeneralData[2]["Estudiantes"] 
                    GeneralData[2]["Estudiantes"] = SigueEnInscrito
                    GeneralData[2]["Estudiantes"][i]["Estado"] = "Inscrito"
                    guardarArchivo(GeneralData)

                else:
                    print("")

            guardarArchivo(GeneralData)    
            print(AprobadosInicial)  
            print(ReprobadosInicial)     
            print(SigueEnInscrito)       

        #===DEFINIR RUTA DEL CAMPER, ASIGNACION DE TRAINER, SALON Y DEFINICION DE HORARIO===        
        elif eleccionCoordinador == 3:
            print("----REGISTRAR RUTA DE ESTUDIO, ASIGNACION DE TRAINER, SALON Y DEFINICION DE HORARIO----")
            GeneralData = abrirArchivo()
            for i in GeneralData[3]["Estudiantes"]:
                print("Idetinficador:",i["Identificador"])
                print("Documento:",i["Documento"])
                print("Nombres",i["Nombres"])
                print("Apellidos",i["Apellidos"])

            Camper = int(input("\nIngrese el identificador del Camper que desea escoger: "))
            print("\nPara la ruta de estudio elige entre:\n NoteCore \n Java \n NoteJS") 
            RutaElegida = str(input("\nIngrese el nombre de la Ruta que le desea definir: "))

            if RutaElegida == "NoteCore":
                GeneralData[3]["Estudiantes"][Camper-1]["Ruta"] = RutaElegida
                GeneralData[3]["Estudiantes"][Camper-1]["Trainer"] = "Jholver Garcia"
                GeneralData[3]["Estudiantes"][Camper-1]["Salon"] = "Apolo"
                GeneralData[3]["Estudiantes"][Camper-1]["FechaInicio"] = "00-00-00"
                GeneralData[3]["Estudiantes"][Camper-1]["FechaFinalizacion"] = "00-00-00"


            elif RutaElegida == "Java":
                GeneralData[3]["Estudiantes"][Camper-1]["Ruta"] = RutaElegida
                GeneralData[3]["Estudiantes"][Camper-1]["Trainer"] = "Miguel Sanchez"
                GeneralData[3]["Estudiantes"][Camper-1]["Salon"] = "Sputnik"
                GeneralData[3]["Estudiantes"][Camper-1]["FechaInicio"] = "00-00-00"
                GeneralData[3]["Estudiantes"][Camper-1]["FechaFinalizacion"] = "00-00-00"


            elif RutaElegida == "NoteJS":
                GeneralData[3]["Estudiantes"][Camper-1]["Ruta"] = RutaElegida
                GeneralData[3]["Estudiantes"][Camper-1]["Trainer"] = "Pedro Gomez"
                GeneralData[3]["Estudiantes"][Camper-1]["Salon"] = "Artemis"
                GeneralData[3]["Estudiantes"][Camper-1]["FechaInicio"] = "00-00-00"
                GeneralData[3]["Estudiantes"][Camper-1]["FechaFinalizacion"] = "00-00-00"


            #ASIGNAR HORARIO
            print("\nLos horarios son:\n 6am-10am\n 10am-2pm\n 2pm-6pm\n 6pm-10pm")
            HorarioAsignado = str(input("Ingrese el horario a asignar: "))
            GeneralData[3]["Estudiantes"][Camper-1]["Horario"] = HorarioAsignado
            guardarArchivo(GeneralData)

            print("Cambios Realizados!")
            input("Presione ENTER para continuar")
            system("cls")

        elif eleccionCoordinador == 4: 
            print("Saliendo del módulo del coordinador")
            input("Presione ENTER para continuar")
            system("cls")
            boolCoordinador = False





#==================================== MODULO DE REPORTES ==================================================
boolReportes = True
while boolReportes == True:
    print("""Modulo de reportes: 
    1. Listar los campers que se encuentren en estado de inscrito.
    2. Listar los campers que aprobaron el examen inicial.
    3. Listar los entrenadores que se encuentran trabajando con CampusLands.
    4. Listar los campers que cuentan con bajo rendimiento.
    5. Listar los Campers y Trainers que se encuentren asociados a una ruta de entrenamiento.
    6. Mostrar cuantos campers perdieron y aprobaron cada uno de los módulos teniendo en cuenta la ruta de entrenamiento y el entrenador encargado.
    7. Salir.
          """)
    eleccionReportes = int(input("¿Qué desea hacer?: "))
    system("cls")

    #=============================LISTAR CAMPERS EN ESTADO INSCRITO================================================
    if eleccionReportes == 1: 
        CampersInscritos = {}
        GeneralData = abrirArchivo()
        for i in range (len(GeneralData[2]["Estudiantes"])):
            if GeneralData[2]["Estudiantes"][i]["NotaPrueba"] == 0:
                CampersInscritos = GeneralData[2]["Estudiantes"]
            elif GeneralData[2]["Estudiantes"][i]["NotaPrueba"] != 0:
                continue
        print("Campers en estado inscrito")
        print("")
        
        if len(CampersInscritos)>=1:
            contador = 0
            for i in CampersInscritos:
                contador+=1
                print("Camper en Estado Inscrito #",contador),print("Nombres:",i["Nombres"]),print("Apellidos:",i["Apellidos"]),print("Nota:",i["NotaPrueba"])
                print("=================")
        else:
            print("No hay campers inscritos")

        input("Presione ENTER para continuar")
        system("cls")
    #===============================LISTAR CAMPERS QUE APROBARON LA PRUEBA INCIAL===================================
    elif eleccionReportes == 2:
        ListarAprobados = {}
        GeneralData = abrirArchivo()
        for i in range (len(GeneralData[2]["Estudiantes"])):
            if GeneralData[2]["Estudiantes"][i]["NotaPrueba"]>=60:
                ListarAprobados = GeneralData[2]["Estudiantes"]
        print("Campers que aprobaron el examen inicial")
        tamañolistaaprobados = len(ListarAprobados)
        if len(ListarAprobados)>=1:
            for i in ListarAprobados:
                print(i["Nombres"]),print("Apellidos:",i["Apellidos"]),print("Nota:",i["NotaPrueba"])
        else:
            print("Todavía no se ha ingresado notas de la prueba inicial a ningun Camper")
        input("Presione ENTER para continuar")
        system("cls")

    #============================== LISTAR TRAINERS DENTRO DE CAMPUSLANDS===========================================
    elif eleccionReportes == 3:
        print("Listar Trainers"),print("")
        GeneralData = abrirArchivo()
        contador = 0 
        for i in (GeneralData[0]["Trainers"]):
            contador+=1
            print("Trainer #",contador),print("Nombre:",i["Nombre"]),print("Ruta:",i["Ruta"]),print("Horario:",i["Horario"]),print("Grupo:",i["Grupo"])
            print("=================")
        
        input("Presione ENTER Para continuar")
        system("cls")


    elif eleccionReportes == 4:
        print("Listar Campers con rendimiento Bajo")


    elif eleccionReportes == 5:
        print("Listar Campers y Trainers asociados a una misma ruta de entrenamiento")

    elif eleccionReportes == 6:
        print("Listar Campers que perdieron y aprobaron cada uno de los modulos dependiendo la ruta de entrenamiento")
        
    elif eleccionReportes == 7:
        print("Saliendo del programa")
        boolReportes = False
    else:
        print("Esta no es una opción válida, intente de nuevo")
        input("Presione ENTER para continuar")
        system("cls")


      
#Desarrollado por Brayan Maldonado Y Maria Lizarazo - Campers