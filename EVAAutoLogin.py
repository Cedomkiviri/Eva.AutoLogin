# datos.txt : Guarda la matricula y contraseña del usuario
# geckodriver.exe : Necesario para abrir Firefox a travez de selenium
import time
import selenium
from selenium import webdriver
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import os

# Esta funcion devuelve una un lista [usuario,contrasena] del archivo datos.txt
def ObtenerDatos():
     f=open("datos.txt")
     l =f.read()
     f.close()
     return l.split(":")

# Esta funcion comprueba si el archivo datos.txt esta vacío 
def NoHayDatos():
    return os.stat('datos.txt').st_size == 0

# Este es el script que usando la libreria Selenium se conecta con Firefox a traves de geckodriver.exe 
def scriptCompleto(usuario,contrasena):
    driver = webdriver.Firefox(executable_path="geckodriver.exe")
    driver.get('https://eva.unapec.edu.do/moodle/login/index.php')
    loginuno = driver.find_element_by_class_name('btn-login')
    loginuno.click()
    time.sleep(1)
    campoLogin = driver.find_element_by_id('i0116')
    campoLogin.send_keys(usuario+"@unapec.edu.do") 
    userlogin = driver.find_element_by_id('idSIButton9')
    userlogin.click()
    time.sleep(1)
    campoLogin = driver.find_element_by_id('i0118')
    campoLogin.send_keys(contrasena) 
    contrasenalogin = driver.find_element_by_id('idSIButton9')
    contrasenalogin.click()
    time.sleep(1)
    botonFinal = driver.find_element_by_id('idBtn_Back')
    botonFinal.click()

# Esta función ejecuta una nueva pestaña para el registro
def Registro():
    #Habra que cambiar esto para añadir un frame y adaptar el diseño
    registrov = Toplevel(mainv)
    registrov.update()
    registrov.title("Registro")
    registrov.geometry('700x200')
    registrov.resizable(width=False, height=False)
    registrov.configure(bg="white")

    # Esta función verifica si los campos fueron llenados,
    # si estos campos son validos crea los datos en
    # el archivo datos.txt
    def RegistrarUsuario(a,b):
        if(NoHayDatos()):
            if(a== "" or b== ""):
                messagebox.showinfo("Error", "Nombre y/o contraseña faltante")
                registrov.lift()
            else:
                f=open("datos.txt","w")
                f.write(a+":"+b)
                f.close()
                registrov.destroy()
                registrov.update()
                mainv.lift()
                boton['state'] =NORMAL
        else:
            messagebox.showinfo("Error", "Ya tiene un usuario registrado")  
            
    load = Image.open("0.png")
    render = ImageTk.PhotoImage(load)
    img = Label(registrov, image=render)
    img.image = render
    img.place(x=0, y=0)

    Label(registrov, text = "Matricula:",font=("Helvetica", 22)).pack()
    correo = Entry(registrov)
    correo.pack()

    Label(registrov, text = "Contraseña:",font=("Helvetica", 22)).pack()
    contra = Entry(registrov, show = "*")
    contra.pack()
    
    Button(registrov,text = "Login",font=("Helvetica", 22),command= lambda: RegistrarUsuario(correo.get(),contra.get())).pack()    
#Si datos.txt esta vacío, ejecuta la vista de registro
#Sino, cambia el estado del boton

def NecesitaRegistro():   
    if(NoHayDatos()):
        Registro() 
    else:
        boton['state'] =NORMAL        

                                        #Aqui se genera la pestaña principal


mainv = Tk()
mainv.title("Eva AutoLogin")
mainv.geometry('700x200')
mainv.resizable(width=False, height=False)
mainv.configure(bg="white")

load = Image.open("0.png")
render = ImageTk.PhotoImage(load)
img = Label(mainv, image=render)
img.image = render
img.place(x=0, y=0)

#Aqui se crea el boton que envia los datos registrados del usuarios a la funcion del Script
boton = Button(mainv,text = "Abrir Eva",state=DISABLED,font=("Helvetica", 22),command= lambda : scriptCompleto(ObtenerDatos()[0],ObtenerDatos()[1]))

boton.pack()

#Se llama a esta funcion para verificar si hace falta registrar usuario
NecesitaRegistro()

mainv.mainloop()
