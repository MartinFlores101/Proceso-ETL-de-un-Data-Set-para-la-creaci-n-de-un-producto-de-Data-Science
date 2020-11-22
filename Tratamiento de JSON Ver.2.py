# Proyecto de Inteligencia de Negocios 2020 Ver. 4 <- 21-Nov-2020 ->

# --------------------------------- Librerias ---------------------------------

import json
import os
from pymongo import MongoClient

# --------------------------------- Variables Globales ---------------------------------
#nombre_del_archivo = 'baseDeDatos.txt'
nombre_del_archivo = '1576949597806.txt'

# --------------------------------- Funciones ---------------------------------
def imprimir_archivo():
    print (" _/ Imprimir archivo")
    archivo = open(nombre_del_archivo, 'r', encoding="utf8") # Encoding Common ones are Latin-1 and UTF-8
    contenido = archivo.read()
    print (contenido)
    archivo.close()

def limpiar_datos():
    print (" _/ Limpiar datos y Crear Json")
    print ("   _/ Limpiando datos...")

    lines = []
    sub_linea = []
    var_temp=""
    var_split =""

    archivo = open(nombre_del_archivo, 'r', encoding="utf8")
    for line in archivo:
        lines.append(line)       
    archivo.close()
    
    cont = 0
    sub_lineas_juntas=''
    while(cont <= len(lines)-1):
        sub_linea = lines[cont].split(',"')  #Seperamos en renglones

        cont2 = 0
        while(cont2 <= len(sub_linea)-1):
            if(cont2+2 <= len(sub_linea)-1):
                temp = sub_linea[cont2]
                temp2 = sub_linea[cont2+1]
                temp3 = sub_linea[cont2+2]
                if(temp.find('text":')!=-1):
                    if(temp2.find('<a href=')!=-1):
                        #sub_linea[cont2]='text":""'
                        var_split_temp=temp.split(':',1)
                        var_split=var_split_temp[1]
                        cont_text1=0
                        var_temp='text":"'
                        while(cont_text1 <= len(var_split)-1 ):
                            if(var_split[cont_text1]!= '"'):
                                var_temp=var_temp+var_split[cont_text1]
                            cont_text1=cont_text1+1
                        var_temp=var_temp+'"'
                        sub_linea[cont2]=var_temp
                        
                        #sub_linea[cont2+1]='source":""'
                        var_split_temp=temp.split(':',1)
                        var_split=var_split_temp[1]
                        cont_text1=0
                        var_temp2='source":"'
                        while(cont_text1 <= len(var_split)-1 ):
                            if(var_split[cont_text1]!= '"'):
                                var_temp2=var_temp2+var_split[cont_text1]
                            cont_text1=cont_text1+1
                        var_temp2=var_temp2+'"'
                        sub_linea[cont2+1]=var_temp2
                    if(temp3.find('<a href=')!=-1):
                        #sub_linea[cont2]='text":""'
                        var_split_temp=temp.split(':',1)
                        var_split=var_split_temp[1]
                        cont_text1=0
                        var_temp='text":"'
                        while(cont_text1 <= len(var_split)-1 ):
                            if(var_split[cont_text1]!= '"'):
                                var_temp=var_temp+var_split[cont_text1]
                            cont_text1=cont_text1+1
                        var_temp=var_temp+'"'
                        sub_linea[cont2]=var_temp

                        #sub_linea[cont2+2]='source":""'
                        var_split_temp=temp.split(':',1)
                        var_split=var_split_temp[1]
                        cont_text1=0
                        var_temp2='source":"'
                        while(cont_text1 <= len(var_split)-1 ):
                            if(var_split[cont_text1]!= '"'):
                                var_temp2=var_temp2+var_split[cont_text1]
                            cont_text1=cont_text1+1
                        var_temp2=var_temp2+'"'
                        sub_linea[cont2+2]=var_temp2
                
                if(temp.find('full_text":')!=-1):
                    if(temp2.find('display_text_range":')!=-1):
                        #sub_linea[cont2]='extended_tweet":{"full_text":""'
                        var_split_temp=temp.split(':',2)
                        var_split=var_split_temp[2]
                        cont_text1=0
                        var_temp='extended_tweet":{"full_text":"'
                        while(cont_text1 <= len(var_split)-1 ):
                            if(var_split[cont_text1]!= '"'):
                                var_temp=var_temp+var_split[cont_text1]
                            cont_text1=cont_text1+1
                        var_temp=var_temp+'"'
                        var_temp=var_temp+'"'
                        sub_linea[cont2]=var_temp

                    if(temp2.find('')!=-1):
                        #sub_linea[cont2]='extended_tweet":{"full_text":""'
                        var_split_temp=temp.split(':',2)
                        var_split=var_split_temp[2]
                        cont_text1=0
                        var_temp='extended_tweet":{"full_text":"'
                        while(cont_text1 <= len(var_split)-1 ):
                            if(var_split[cont_text1]!= '"'):
                                var_temp=var_temp+var_split[cont_text1]
                            cont_text1=cont_text1+1
                        var_temp=var_temp+'"'
                        sub_linea[cont2]=var_temp

                        if(temp3.find('display_text_range":')!=-1):
                            sub_linea[cont2+1]='' #<----------------------------------------AQUI Martin
                            
                
                if(temp.find('description":')!=-1):
                    if(temp2.find('translator_type":')!=-1):
                        #sub_linea[cont2]='description":""'
                        var_split_temp=temp.split(':',1)
                        var_split=var_split_temp[1]
                        cont_text1=0
                        var_temp='description":"'
                        while(cont_text1 <= len(var_split)-1 ):
                            if(var_split[cont_text1]!= '"'):
                                var_temp=var_temp+var_split[cont_text1]
                            cont_text1=cont_text1+1
                        var_temp=var_temp+'"'
                        sub_linea[cont2]=var_temp

                    if(temp2.find('')!=-1):
                        #sub_linea[cont2]='description":""'
                        var_split_temp=temp.split(':',1)
                        var_split=var_split_temp[1]
                        cont_text1=0
                        var_temp='description":"'
                        while(cont_text1 <= len(var_split)-1 ):
                            if(var_split[cont_text1]!= '"'):
                                var_temp=var_temp+var_split[cont_text1]
                            cont_text1=cont_text1+1
                        var_temp=var_temp+'"'
                        sub_linea[cont2]=var_temp

                        if(temp3.find('translator_type":')!=-1):
                            sub_linea[cont2+1]=''

                if(temp.find('name":')!=-1):
                    if(temp2.find('screen_name":')!=-1):
                        #sub_linea[cont2]='name":""'
                        var_split_temp=temp.split(':',1)
                        var_split=var_split_temp[1]
                        cont_text1=0
                        var_temp='name":"'
                        while(cont_text1 <= len(var_split)-1 ):
                            if(var_split[cont_text1]!= '"'):
                                var_temp=var_temp+var_split[cont_text1]
                            cont_text1=cont_text1+1
                        var_temp=var_temp+'"'
                        sub_linea[cont2]=var_temp

                    if(temp2.find('id":')!=-1):
                        #sub_linea[cont2]='name":""'   
                        var_split_temp=temp.split(':',1)
                        var_split=var_split_temp[1]
                        cont_text1=0
                        var_temp='name":"'
                        while(cont_text1 <= len(var_split)-1 ):
                            if(var_split[cont_text1]!= '"'):
                                var_temp=var_temp+var_split[cont_text1]
                            cont_text1=cont_text1+1
                        var_temp=var_temp+'"'
                        sub_linea[cont2]=var_temp
                        
                    if(temp3.find('screen_name":')!=-1):
                        #sub_linea[cont2]='name":""'   
                        var_split_temp=temp.split(':',1)
                        var_split=var_split_temp[1]
                        cont_text1=0
                        var_temp='name":"'
                        while(cont_text1 <= len(var_split)-1 ):
                            if(var_split[cont_text1]!= '"'):
                                var_temp=var_temp+var_split[cont_text1]
                            cont_text1=cont_text1+1
                        var_temp=var_temp+'"'
                        sub_linea[cont2]=var_temp

                if(temp.find('location":')!=-1):
                    if(temp2.find('url":')!=-1):
                        #sub_linea[cont2]='location":""'
                        var_split_temp=temp.split(':',1)
                        var_split=var_split_temp[1]
                        cont_text1=0
                        var_temp='location":"'
                        while(cont_text1 <= len(var_split)-1 ):
                            if(var_split[cont_text1]!= '"'):
                                var_temp=var_temp+var_split[cont_text1]
                            cont_text1=cont_text1+1
                        var_temp=var_temp+'"'
                        sub_linea[cont2]=var_temp
                                 
            if(cont2!=0):
                sub_linea[cont2] = ',"' + sub_linea[cont2]

            if(sub_linea[cont2]!=',"'):
                sub_lineas_juntas=sub_lineas_juntas + sub_linea[cont2]
            cont2 = cont2 + 1
        lines[cont]=sub_lineas_juntas
        sub_lineas_juntas=""
        cont = cont + 1
    
    print ("   _/ Creando Json...")
    cont=0
    file = open("base_de_datos_final.json", "w", encoding="utf8")
    file.write("[")
    while(cont <= len(lines)-1):
        if(lines[cont] != "\n"):
    
            if(cont != len(lines)-2):
                file.write(lines[cont]+ "," + os.linesep)
            else: 
                file.write(lines[cont] + "]")
    
        cont=cont+1
    file.close()
    
def importar():
    client = MongoClient("localhost", 27017)
    nombre = ""
    while nombre == "":
        print("¿Nombre del archivo .json?")
        nombre = input() + ".json"
        ruta = os.path.abspath(nombre)
        if os.path.isfile(ruta):
            print("Se encontro el archivo")
        else:
            print("no existe el archivo")
            nombre = ""

    print("¿Nombre de la Base de Datos de Mongo que desea crear?")
    base = input()
    print("¿Nombre de la Collecion de Mongo que desea crear?")
    collecion = input()
    try:
        print(client.list_database_names())

        db = client[base]
        collection = db[collecion]

        f = open(ruta, 'r', encoding="utf8")
        bdd = json.loads(f.read())

        for item in bdd:
            collection.insert_one(item)
        print("   _/ Base de datos creada")
    except NameError:
        print("Error")
    client.close()


def validar_menu():
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Elije una opcion: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero') 
    return num

# --------------------------------- Main ---------------------------------
salir = False
opcion = 0

print(" *-*-* Proyecto de Inteligencia de Negocios 2020 Ver. 1 *-*-* ")

while not salir:
    print ("\nMENU: ")
    print ("1. Imprimir archivo")
    print ("2. Limpiar datos y Crear Json")
    print ("3. Importar JSON ")
    print ("4. Salir")

    opcion = validar_menu()

    if opcion == 1:
        imprimir_archivo()
    elif opcion == 2:
        limpiar_datos()
    elif opcion == 3:
        importar()
    elif opcion == 4:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 4")
 
print ("Adios")

