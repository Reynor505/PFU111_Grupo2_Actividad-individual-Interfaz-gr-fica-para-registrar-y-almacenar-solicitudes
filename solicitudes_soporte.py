import os
import csv
import tkinter as tk
from tkinter import ttk

ARCHIVO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "solicitudes.csv")
TIPOS = ["equipo", "software", "conectividad"]
PRIORIDADES = ["bajo", "medio", "alto"]


def mostrar(texto):
    # Muestra un mensaje en el área de resultados
    salida.delete("1.0", "end")
    salida.insert("end", texto)


def limpiar():
    entry_nombre.delete(0, "end")
    entry_codigo.delete(0, "end")
    combo_tipo.set("")
    texto_desc.delete("1.0", "end")
    var_prioridad.set("")
    mostrar("")


def registrar():
    nombre = entry_nombre.get().strip()
    codigo = entry_codigo.get().strip()
    tipo = combo_tipo.get()
    descripcion = texto_desc.get("1.0", "end").strip().replace("\n", " ")
    prioridad = var_prioridad.get()

    # Validaciones
    errores = []
    if nombre == "":
        errores.append("- El nombre no puede estar vacío.")
    if codigo == "":
        errores.append("- El código de estudiante no puede estar vacío.")
    if tipo not in TIPOS:
        errores.append("- Seleccione un tipo de solicitud válido.")
    if descripcion == "":
        errores.append("- La descripción no puede estar vacía.")
    if prioridad not in PRIORIDADES:
        errores.append("- Seleccione una prioridad válida.")

    if len(errores) > 0:
        mostrar("No se guardó. Corrija lo siguiente:\n" + "\n".join(errores))
        return

    # Guardar en el archivo
    try:
        archivo_nuevo = not os.path.exists(ARCHIVO)
        with open(ARCHIVO, "a", newline="", encoding="utf-8") as f:
            escritor = csv.writer(f)
            if archivo_nuevo:
                escritor.writerow(["nombre", "codigo", "tipo", "descripcion", "prioridad"])
            escritor.writerow([nombre, codigo, tipo, descripcion, prioridad])
        limpiar()
        mostrar("Solicitud registrada correctamente.")
    except OSError:
        mostrar("Error: no se pudo escribir en el archivo.")


def consultar():
    if not os.path.exists(ARCHIVO):
        mostrar("Todavía no hay solicitudes guardadas (el archivo no existe).")
        return
    try:
        with open(ARCHIVO, "r", newline="", encoding="utf-8") as f:
            filas = list(csv.reader(f))
        texto = ""
        for fila in filas[1:]:  # filas[0] es el encabezado
            texto += f"{fila[0]} | {fila[1]} | {fila[2]} | {fila[4]}\n   {fila[3]}\n"
        mostrar(texto if texto != "" else "El archivo no tiene solicitudes.")
    except (OSError, IndexError):
        mostrar("Error: no se pudo leer el archivo.")


# ---------- Ventana ----------
ventana = tk.Tk()
ventana.title("Solicitudes de soporte técnico")

ttk.Label(ventana, text="Nombre del solicitante:").grid(row=0, column=0, sticky="w", padx=8, pady=4)
entry_nombre = ttk.Entry(ventana, width=40)
entry_nombre.grid(row=0, column=1, padx=8)

ttk.Label(ventana, text="Código de estudiante:").grid(row=1, column=0, sticky="w", padx=8, pady=4)
entry_codigo = ttk.Entry(ventana, width=40)
entry_codigo.grid(row=1, column=1, padx=8)

ttk.Label(ventana, text="Tipo de solicitud:").grid(row=2, column=0, sticky="w", padx=8, pady=4)
combo_tipo = ttk.Combobox(ventana, values=TIPOS, state="readonly", width=37)
combo_tipo.grid(row=2, column=1, padx=8)

ttk.Label(ventana, text="Descripción del problema:").grid(row=3, column=0, sticky="nw", padx=8, pady=4)
texto_desc = tk.Text(ventana, width=30, height=4)
texto_desc.grid(row=3, column=1, padx=8)

ttk.Label(ventana, text="Prioridad:").grid(row=4, column=0, sticky="w", padx=8, pady=4)
var_prioridad = tk.StringVar()
marco = ttk.Frame(ventana)
marco.grid(row=4, column=1, sticky="w", padx=8)
for p in PRIORIDADES:
    ttk.Radiobutton(marco, text=p, value=p, variable=var_prioridad).pack(side="left", padx=5)

marco_botones = ttk.Frame(ventana)
marco_botones.grid(row=5, column=0, columnspan=2, pady=10)
ttk.Button(marco_botones, text="Registrar solicitud", command=registrar).pack(side="left", padx=5)
ttk.Button(marco_botones, text="Consultar solicitudes", command=consultar).pack(side="left", padx=5)
ttk.Button(marco_botones, text="Limpiar formulario", command=limpiar).pack(side="left", padx=5)

salida = tk.Text(ventana, width=60, height=10)
salida.grid(row=6, column=0, columnspan=2, padx=8, pady=8)

ventana.mainloop()