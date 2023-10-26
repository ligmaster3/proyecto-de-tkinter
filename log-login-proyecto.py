import mysql.connector
import tkinter as tk
from tkinter import messagebox, ttk, Scrollbar
from customtkinter import CTkButton, CTkFrame, CTkTextbox

class Registro:
    def __init__(self, ventana):
        # Crear la ventana principal
        self.wind = ventana
        self.wind.title("Formulario de Registro con tkinter y Python")
        self.wind.geometry("650x750")
        self.wind.resizable(0,0)
        
        # Crear un contenedor
        marco = CTkFrame(ventana,corner_radius=10,width=80,fg_color="#E5E7E9")
        titulo = tk.Label(ventana, text="REGISTRO DE USUARIO", bg="#6c757d", fg="white", width="94", height=2)
        titulo.pack()
        marco.pack(side="top")

        self.titulo = tk.Label(marco, text="LOGIN",bg="#E5E7E9",width=40)
        self.titulo.pack(side="top")
        # Caja de texto para ingresar el nombre
        self.name_label = tk.Label(marco, text="Nombre",bg="#E5E7E9")
        self.name_label.pack(padx=10, pady=10)
        self.name_entry = tk.Entry(marco)
        self.name_entry.pack(padx=5, pady=5)

        # Caja de texto para ingresar el apellido
        self.appe_label = tk.Label(marco, text="Apellido",bg="#E5E7E9")
        self.appe_label.pack(padx=10, pady=10)
        self.appe_entry = tk.Entry(marco)
        self.appe_entry.pack(padx=5, pady=5)

        # Caja de texto para ingresar la edad
        self.eda_label = tk.Label(marco, text="Edad",bg="#E5E7E9")
        self.eda_label.pack(padx=10, pady=10)
        self.eda_entry = tk.Entry(marco)
        self.eda_entry.pack(padx=5, pady=5)

        # Caja de texto para ingresar el modelo
        self.mod_label = tk.Label(marco, text="Modelo",bg="#E5E7E9")
        self.mod_label.pack(padx=10, pady=10)
        self.mod_entry = tk.Entry(marco)
        self.mod_entry.pack(padx=5, pady=5)

        # Caja de texto para ingresar el producto
        self.prob_label = tk.Label(marco, text="Producto",bg="#E5E7E9")
        self.prob_label.pack(padx=10, pady=10)
        self.prob_entry = tk.Entry(marco)
        self.prob_entry.pack(padx=5, pady=5)

        # Caja de texto para ingresar la cantidad
        self.cant_label = tk.Label(marco, text="Cantidad",bg="#E5E7E9")
        self.cant_label.pack(padx=10, pady=10)
        self.cant_entry = tk.Entry(marco)
        self.cant_entry.pack(padx=5, pady=5)

        # Caja de texto para ingresar el precio
        self.preb_label = tk.Label(marco, text="Precio",bg="#E5E7E9")
        self.preb_label.pack(padx=10, pady=10)
        self.preb_entry = tk.Entry(marco)
        self.preb_entry.pack(padx=5, pady=5)

        # Botón para registrar
        self.reg_button = CTkButton(marco, text="REGISTRAR", command=self.registrar,height=20,width=10,fg_color="green",corner_radius=10)
        self.reg_button.pack(padx=5, pady=5)

        # Botón para mostrar registros
        self.boton_limpiar=CTkButton(marco, text="MOSTRAR",command=self.mostrar,height=20,width=10,fg_color="green",corner_radius=10)
        self.boton_limpiar.pack(padx=5, pady=5)

        # Botón para cerrar
        self.boton_cancelar=CTkButton(marco, text="CERRAR",command=self.cerrar,height=20,width=10,fg_color="green",corner_radius=10)
        self.boton_cancelar.pack(padx=5,pady=5)
        
        

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

    def mostrar(self):
        try:
            conn = self.conexion()
            cursor = conn.cursor()
            query = "SELECT * FROM clientes"
            cursor.execute(query)
            result = cursor.fetchall()

            if result:
                for row in result:
                    print(f"ID: {row[0]}, Nombre: {row[1]}, Apellido: {row[2]}, Edad: {row[3]}, Modelo: {row[4]}, Producto: {row[5]}, Cantidad: {row[6]}, Precio: {row[7]}")
            else:
                print("No hay registros en la base de datos")
        except mysql.connector.Error as err:
            print(f"Error al conectar a la base de datos: {err}")
        finally:
            if conn:
                conn.close()

    def cerrar(self):
        self.wind.destroy()


if __name__ == "__main__":
    ventana = tk.Tk()
    mi_app = Registro(ventana)
    ventana.mainloop()