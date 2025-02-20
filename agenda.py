import tkinter as tk
from tkinter import messagebox
import sqlite3
from plyer import notification
from datetime import datetime

# Crear base de datos
conn = sqlite3.connect("agenda.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS notas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT,
        contenido TEXT,
        fecha TEXT
    )
""")
conn.commit()

# Función para agregar nota
def agregar_nota():
    titulo = entry_titulo.get()
    contenido = text_contenido.get("1.0", tk.END).strip()
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if titulo and contenido:
        cursor.execute("INSERT INTO notas (titulo, contenido, fecha) VALUES (?, ?, ?)", (titulo, contenido, fecha))
        conn.commit()
        notification.notify(title="Nota guardada", message=f"{titulo} ha sido guardado", timeout=5)
        messagebox.showinfo("Éxito", "Nota guardada correctamente")
        entry_titulo.delete(0, tk.END)
        text_contenido.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Error", "Título y contenido no pueden estar vacíos")

# Configurar ventana principal
root = tk.Tk()
root.title(" Notas")
root.geometry("700x500")

# Widgets
tk.Label(root, text="Título:").pack()
entry_titulo = tk.Entry(root, width=70)
entry_titulo.pack()

tk.Label(root, text="Contenido:").pack()
text_contenido = tk.Text(root, height=5, width=70)
text_contenido.pack()

tk.Button(root, text="Guardar Nota", command=agregar_nota).pack()

root.mainloop()

# Cerrar base de datos al salir
conn.close()
