import mysql.connector
import tkinter as tk
from tkinter import messagebox, ttk, Scrollbar, PhotoImage
from PIL import ImageTk, Image
from customtkinter import CTkButton, CTkFrame, CTkTextbox

class Registro:
    def __init__(self, ventana):
        # Crear la ventana principal
        self.wind = ventana
        self.wind.title("Formulario de Registro con tkinter y Python")
        self.wind.geometry("1000x640+100+50")
        self.wind.resizable(0,0)
        self.wind.iconbitmap("imagen\icono-hotel.ico")
        
        #fondo++
        image = PhotoImage(file = "imagen\hoteles-dogs.png")
        fondo=tk.Label(self.wind,image=image).place(x=0,y=0,relwidth=1,relheight=1)
    
        # Crear un contenedor        
        marco = CTkFrame(ventana,corner_radius=10,width=100,height=2,fg_color="#E5E7E9")
        titulo = tk.Label(ventana, text="REGISTRO DE USUARIO", bg="#6c757d",font=('Arial',14), fg="white", width="94", height=2)
        titulo.pack(side="top")
        marco.pack(side="left",fill="both")

        self.titulo = tk.Label(marco, text="LOGIN",bg="#E5E7E9",width=35,height=3)
        self.titulo.pack(side="top")
        # Caja de texto para ingresar el nombre
        self.name_label = tk.Label(marco, text="Nombre",bg="#E5E7E9")
        self.name_label.pack(padx=6, pady=6)
        self.name_entry = tk.Entry(marco)
        self.name_entry.pack(padx=5, pady=5)

        # Caja de texto para ingresar el apellido
        self.appe_label = tk.Label(marco, text="Apellido",bg="#E5E7E9")
        self.appe_label.pack(padx=6, pady=6)
        self.appe_entry = tk.Entry(marco)
        self.appe_entry.pack(padx=5, pady=5)

        # Caja de texto para ingresar la edad
        self.eda_label = tk.Label(marco, text="Edad",bg="#E5E7E9")
        self.eda_label.pack(padx=6, pady=6)
        self.eda_entry = tk.Entry(marco)
        self.eda_entry.pack(padx=5, pady=5)

        # Caja de texto para ingresar el modelo
        self.mod_label = tk.Label(marco, text="Modelo",bg="#E5E7E9")
        self.mod_label.pack(padx=6, pady=6)
        self.mod_entry = tk.Entry(marco)
        self.mod_entry.pack(padx=5, pady=5)

        # Caja de texto para ingresar el producto
        self.prob_label = tk.Label(marco, text="Producto",bg="#E5E7E9")
        self.prob_label.pack(padx=6, pady=6)
        self.prob_entry = tk.Entry(marco)
        self.prob_entry.pack(padx=5, pady=5)

        # Caja de texto para ingresar la cantidad
        self.cant_label = tk.Label(marco, text="Cantidad",bg="#E5E7E9")
        self.cant_label.pack(padx=6, pady=6)
        self.cant_entry = tk.Entry(marco)
        self.cant_entry.pack(padx=5, pady=5)

        # Caja de texto para ingresar el precio
        self.preb_label = tk.Label(marco, text="Precio",bg="#E5E7E9")
        self.preb_label.pack(padx=6, pady=6)
        self.preb_entry = tk.Entry(marco)
        self.preb_entry.pack(padx=5, pady=5)
        
        # botón  de registrar los datos
        self.reg_button = CTkButton(marco, text="REGISTRAR", command=self.registrar,
                                    height=20,width=10,fg_color="green",corner_radius=10)
        self.reg_button.pack(padx=3, pady=3)

        # Botón para cerrar
        self.boton_cancelar=CTkButton(marco, text="CERRAR", command=self.cerrar,
                                      height=20,width=10,fg_color="green",corner_radius=10)
        self.boton_cancelar.pack(padx=3, pady=3)
        #boton invisble no tocar ni borrar
        btn = tk.Button(ventana)
        btn.grid(row=0,column=1)
        #---------------------------------
        

    def conexion(self):
        try:
            conn = mysql.connector.connect(
                host="localhost", 
                user="root", 
                password="",
                database="proyecto"
                )
            print("Conexion a la base de datos exitosa")
            return conn
        except mysql.connector.Error as err:
            print(f"Error al conectar a la base de datos: {err}")
            return None

    def registrar(self):
        name = self.name_entry.get()
        appe = self.appe_entry.get()
        eda = self.eda_entry.get()
        mod = self.mod_entry.get()
        prob = self.prob_entry.get()
        cant = self.cant_entry.get()
        preb = self.preb_entry.get()

        if not name or not appe or not eda or not mod or not prob or not cant or not preb:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        try:
            conn = self.conexion()
            cursor = conn.cursor()
            query = "INSERT INTO clientes (nombre, apellido, edad, modelo, producto, cantidad, precio) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (name, appe, eda, mod, prob, cant, preb))
            conn.commit()
            messagebox.showinfo("Exito", "Registro exitoso")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"No se pudo realizar el registro: {err}")
        finally:
            if conn:
                conn.close()

    def cerrar(self):
        self.wind.destroy()


if __name__ == "__main__":
    ventana = tk.Tk()
    mi_app = Registro(ventana)
    ventana.mainloop()
