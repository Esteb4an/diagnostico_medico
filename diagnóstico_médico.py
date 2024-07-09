# Archivo: sistema_experto_diagnostico_gui.py

import tkinter as tk
from tkinter import messagebox

# Definición de la base de conocimiento
BASE_CONOCIMIENTO = {
    'Gripe': {'fiebre', 'tos', 'dolor de cabeza', 'fatiga'},
    'Resfriado': {'estornudos', 'secreción nasal', 'dolor de garganta'},
    'COVID-19': {'fiebre', 'tos', 'dificultad para respirar', 'pérdida del gusto'},
    'Alergias': {'estornudos', 'picazón en los ojos', 'secreción nasal'},
    'Influenza': {'fiebre', 'tos', 'dolor muscular', 'fatiga'},
    'Bronquitis': {'tos', 'mucosidad', 'fatiga', 'dificultad para respirar'},
    'Neumonía': {'fiebre', 'escalofríos', 'tos', 'dificultad para respirar', 'dolor en el pecho'},
    'Sinusitis': {'dolor de cabeza', 'secreción nasal', 'dolor facial', 'congestión nasal'}
}

def diagnosticar(sintomas_seleccionados):
    diagnostico = []
    for enfermedad, sintomas_enfermedad in BASE_CONOCIMIENTO.items():
        if sintomas_enfermedad == sintomas_seleccionados:
            return [enfermedad]  # Devuelve solo esta enfermedad si todos sus síntomas están seleccionados
        elif sintomas_enfermedad & sintomas_seleccionados:
            if sintomas_enfermedad.issuperset(sintomas_seleccionados):
                diagnostico.append(enfermedad)  # Añade enfermedades que contienen todos los síntomas seleccionados

    return diagnostico

def mostrar_diagnostico():
    sintomas_seleccionados = {sintoma for sintoma, var in checkboxes.items() if var.get()}
    resultados = diagnosticar(sintomas_seleccionados)
    if resultados:
        mensaje = "Diagnóstico posible basado en los síntomas seleccionados:\n" + "\n".join(resultados)
    else:
        mensaje = "No se ha encontrado un diagnóstico claro con los síntomas seleccionados."
    messagebox.showinfo("Diagnóstico", mensaje)

# Crear la interfaz gráfica
ventana = tk.Tk()
ventana.title("Sistema Experto de Diagnóstico Médico")

tk.Label(ventana, text="Seleccione los síntomas:").pack(pady=10)

checkboxes = {}
for sintoma in {s for sintomas in BASE_CONOCIMIENTO.values() for s in sintomas}:
    var = tk.BooleanVar()
    checkbox = tk.Checkbutton(ventana, text=sintoma, variable=var)
    checkbox.pack(anchor='w')
    checkboxes[sintoma] = var

boton_diagnostico = tk.Button(ventana, text="Obtener Diagnóstico", command=mostrar_diagnostico)
boton_diagnostico.pack(pady=20)

ventana.mainloop()
