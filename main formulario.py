import tkinter as tk
from tkinter import messagebox, Label, Entry, Tk, ttk
from customtkinter import CTkCheckBox, CTkButton, CTkFrame, CTkTextbox

import mysql.connector

class Registro:
    def __init__(self,ventana):
    
        # Crear la ventana principal
        self.wind = ventana
        self.wind.title("Formulario de Registro con tkinter y Python")
        self.wind.geometry("650x750")
        self.wind.resizable(0,0)
         # Crear un contenedor
        frame = CTkFrame(ventana,corner_radius=10)
        titulo = Label(ventana, text="REGISTRO DE USUARIO", bg="#6c757d", fg="white",font=("Comic Sans", 13, "bold"), width="70", height=2)
        titulo.pack()
        frame.pack(side="left")
        #crea variblees
        marco = ttk.LabelFrame(frame, text="LOGIN")
        marco.pack(padx=10, pady=10)
        self.name = tk.StringVar()
        self.appe = tk.StringVar()
        self.eda = tk.StringVar()
        self.mod = tk.StringVar()
        self.prob = tk.StringVar()
        self.cant = tk.StringVar()
        self.preb = tk.StringVar()
        
        # Añadir widgets
        nombre = Label(marco, text="Nombre",width=20)
        nombre.pack(padx=10, pady=10)
        self.name = Entry(marco)
        self.name.pack(padx=5,pady=5)

        apellido = Label(marco, text="Apellido")
        apellido.pack(padx=10, pady=10)
        self.appe = Entry(marco)
        self.appe.pack(padx=5, pady=5)

        edad = Label(marco, text="Edad")
        edad.pack(padx=10, pady=10)
        self.eda = Entry(marco)
        self.eda.pack(padx=5, pady=5)
        
        modelo = Label(marco, text="Modelo")
        modelo.pack(padx=10, pady=10)
        self.mod = Entry(marco)
        self.mod.pack(padx=5, pady=5)
        
        producto = Label(marco, text="Producto")
        producto.pack(padx=10, pady=10)
        self.prob = Entry(marco)
        self.prob.pack(padx=5, pady=5)
        
        cantidad = Label(marco, text="Cantidad")
        cantidad.pack(padx=10, pady=10)
        self.cant = Entry(marco)
        self.cant.pack(padx=5, pady=5)
        
        precio = Label(marco, text="Precio")
        precio.pack(padx=10, pady=10)
        self.preb = tk.Entry(marco)
        self.preb.pack(padx=5, pady=5)
        
        boton_registrar=CTkButton(marco, text="REGISTRAR",command=registrar,height=20,width=10,fg_color="green",font=("Comic Sans", 12,"bold"),corner_radius=20)
        boton_registrar.pack(padx=5,pady=10)
        
        boton_limpiar=CTkButton(marco, text="MOSTRAR",command=mostrar,height=20,width=10,fg_color="gray",font=("Comic Sans", 12,"bold"),corner_radius=20)
        boton_limpiar.pack(padx=5,pady=5)
        
        boton_cancelar=CTkButton(marco, text="CERRAR",command=cerrar,height=20,width=10,fg_color="red",font=("Comic Sans", 12,"bold"),corner_radius=20)
        boton_cancelar.pack(padx=5,pady=5)
        # Ejecutar la ventana principal
         
        visualizar=CTkFrame(ventana, fg_color="#F6DDCC",width=300,height=300)
        visualizar.pack(side="right")
        
 

        # Create and configure your GUI elements here

def conexion(self):
        # Establish a database connection
        config = {
            'host': 'localhost',
            'user': 'root',
            'password': '',
            'database': 'proyecto'
        }

        try:
            connection = mysql.connector.connect(**config)
            print("Conexión a la base de datos exitosa")
            return connection
        except mysql.connector.Error as err:
            print(f"Error al conectar a MySQL: {err}")
            return None

def registrar(self):
        conn = self.conexion()
        if conn:
            cursor = conn.cursor()
            query = "INSERT INTO clientes (nombre, apellido, edad, modelo, producto, cantidad, precio) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (self.name.get(), self.appe.get(), self.eda.get(), self.mod.get(), self.prob.get(), self.cant.get(), self.preb.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo("Info", "Registro guardado con éxito!")

def mostrar(self):
        conn = self.conexion()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT * FROM clientes")
                resultados = cursor.fetchall()
                for fila in resultados:
                    print(fila)
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error al mostrar datos: {err}")
            finally:
                conn.close()

def cerrar(self):
        ventana.destroy()
 
# Crear una instancia de la clase Registro
if __name__ == '__main__':
      ventana=tk.Tk()
      application=Registro(ventana)
      ventana.mainloop()
