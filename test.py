# resources.txt : Guarda la matricula y contraseña del usuario
# geckodriver.exe : Necesario para abrir Firefox a travez de selenium
import time
import selenium
from selenium import webdriver
from tkinter import * 
from PIL import Image, ImageTk
from tkinter import messagebox
import os

# Esta funcion devuelve un string
# el contenido del archivo
# resources.txt
def getResources():
     f=open("resources.txt")
     l =f.read()
     f.close()
     return l.split(":")

# Esta funcion comprueba si el archivo
# resources.txt esta vacío 
# retorna booleano
def isResourcesEmpty():
    return os.stat('resources.txt').st_size == 0

# Este es el script que usando la libreria 
# Selenium se conecta con Firefox a traves
# de geckodriver.exe 
def scriptCompleto(usuario,password):
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
    campoLogin.send_keys(password) 
    passwordlogin = driver.find_element_by_id('idSIButton9')
    passwordlogin.click()
    time.sleep(1)
    botonFinal = driver.find_element_by_id('idBtn_Back')
    botonFinal.click()


# Esta función ejecuta una nueva pestaña
# para  el registro
def Registro():
    #Habra que cambiar esto para añadir un frame y adaptar el diseño
    window = Toplevel(mainv)
    window.update()
    window.title("Registro")
    window.geometry('700x200')
    window.resizable(width=False, height=False)
    window.configure(bg="white")

    # Esta función verifica si los campos fueron llenados,
    # si estos campos son validos crea los datos en
    # el archivo resources.txt
    def RegistrarUsuario(a,b):
        if(isResourcesEmpty()):
            if(a== "" or b== ""):
                messagebox.showinfo("Error", "Nombre y/o contraseña faltante")
                window.lift()
            else:
                f=open("resources.txt","w")
                f.write(a+":"+b)
                f.close()
                window.destroy()
                window.update()
                mainv.lift()
                boton['state'] =NORMAL
        else:
            messagebox.showinfo("Error", "Ya tiene un usuario registrado")  
            
    load = Image.open("0.png")
    render = ImageTk.PhotoImage(load)
    img = Label(window, image=render)
    img.image = render
    img.place(x=0, y=0)

    Label(window, text = "Matricula:",font=("Helvetica", 22)).pack()
    correo = Entry(window)
    correo.pack()

    Label(window, text = "Contraseña:",font=("Helvetica", 22)).pack()
    contra = Entry(window, show = "*")
    contra.pack()
    
    Button(window,text = "Login",font=("Helvetica", 22),command= lambda: RegistrarUsuario(correo.get(),contra.get())).pack()    
          

#Aqui se genera la pestaña principal

#Habra que cambiar esto para añadir un frame y adaptar el diseño
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
boton = Button(mainv,text = "Abrir Eva",state=DISABLED,font=("Helvetica", 22),command= lambda : scriptCompleto(getResources()[0],getResources()[1]))
boton.pack()

if(isResourcesEmpty()):
    Registro() 
else:
    boton['state'] =NORMAL

mainv.mainloop()
