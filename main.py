from io import open
import os
import time
import platform
#from colorama import Fore # solo es para dar color a los mensajes por terminal   


#########################################################################
#########################################################################
####     script creado solo para gestionar archivos, sencillo        ####
####     funcion abrir,crear,editar,sobrescribir                     ####
####     funcion abrir,crear,editar,sobrescribir                     ####
####     @autor victor jx                                            ####
####     nota :                                                      ####
####           Al crear el archivo solo poner el nombre              ####
####           la extension se agrega sola                           ####         
#########################################################################
#########################################################################



class main():
    def __init__(self):
        #self.ruta =  "/home/victorjx/Documents/Codigo/testfichero/ficheros/"
        self.ruta = os.getcwd()+ "/testfichero/ficheros/"   
        self.principal()
        

    def show(self):
        print("""                             
            Welcome creator Victorjx
            1) crear un archivo
            2) abrir un archivo
            3) agregar contenido a un archivo
            4) sobrescribir un archivo
            5) listar archivos creados
            6) salir 
        """)
        time.sleep(1)
        
    def principal(self):
        print("archivos existentes :V")
        self.listar_ruta()
        self.show()
        
        while True:
            elec = input("ingrese la opcion que desee realizar \n>")
            if elec == "1":
                self.newfile()
            elif elec == "2":
                self.openfile()
            elif elec == "3":
                self.addfile()
            elif elec == "4":
                self.overwrite()
            elif elec == "5":
                self.listar_ruta()
            elif elec == "6":
                break

            time.sleep(1)
            self.show()



    def newfile(self):
        nombre = input("ingrese nombre \n>")
        try:
            fichero = open("{}{}.txt".format(self.ruta,nombre),"x")
            fichero.close()
        except FileExistsError as a:
            print("El fichero ya existe ")
        else:
            print("archivo creado")
    


    def openfile(self):
        self.listar_ruta()
        nombre = input("ingrese nombre del archivo \n>")
        try:
            fichero = open("{}{}.txt".format(self.ruta,nombre),"r")
            print(fichero.read())
            fichero.close()
        except Exception as a:
            print("ingrese el nombre de un archivo existente")
        time.sleep(20)
        

    def overwrite(self):
        nombre = input("ingrese nombre del archivo \n>")
        conten = input("sobrescribe contenido \n>")
        try:
            fichero = open("{}{}.txt".format(self.ruta,nombre),"w")
            fichero.write(conten)
            fichero.close()            
        except Exception as a:
            print("el archivo no existe")

    def addfile(self):
        nombre = input("ingrese nombre del archivo \n>")
        conten = input("agrege contenido \n>")
        try:
            fichero = open("{}{}.txt".format(self.ruta,nombre),"a")
            fichero.write("\n"+conten)
            fichero.close()            
        except Exception as a:
            print("seleccionar un archivo existente")

    def listar_ruta(self):
        lista_de_archivos = os.listdir(self.ruta)
        for a in lista_de_archivos:
            print ("\t "+a)




main()
