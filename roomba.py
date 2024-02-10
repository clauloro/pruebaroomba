import tkinter as tk

def calcular_area():
    # Obtener las medidas de la habitación
    largo_habitacion = float(entry_largo_habitacion.get())
    ancho_habitacion = float(entry_ancho_habitacion.get())
    
    # Obtener las medidas del objeto
    largo_objeto = float(entry_largo_objeto.get())
    ancho_objeto = float(entry_ancho_objeto.get())
    
    # Obtener las coordenadas del objeto
    posicion_x = float(entry_posicion_x.get())
    posicion_y = float(entry_posicion_y.get())
    
    # Calcular áreas
    area_habitacion = largo_habitacion * ancho_habitacion
    area_objeto = largo_objeto * ancho_objeto
    
    # Calcular área de limpieza de la aspiradora
    area_limpiar = area_habitacion - area_objeto
    
    # Mostrar resultados
    resultado_area_habitacion.config(text=f"Área de la habitación: {area_habitacion} metros cuadrados")
    resultado_area_objeto.config(text=f"Área del objeto: {area_objeto} metros cuadrados")
    resultado_area_limpiar.config(text=f"Área para limpiar: {area_limpiar} metros cuadrados")
    
    # Dibujar habitación y objeto en el lienzo
    lienzo.delete("all")  # Limpiar el lienzo
    
    # Escala mayor
    escala = 20
    
    # Dimensiones del lienzo
    lienzo_width = 400
    lienzo_height = 300
    
    # Coordenadas para centrar el lienzo
    centro_x = lienzo_width / 2
    centro_y = lienzo_height / 2
    
    # Dibujar habitación
    x1, y1 = centro_x - largo_habitacion * escala / 2, centro_y - ancho_habitacion * escala / 2
    x2, y2 = x1 + largo_habitacion * escala, y1 + ancho_habitacion * escala
    lienzo.create_rectangle(x1, y1, x2, y2, outline="black", fill="white")
    
    # Dibujar objeto
    x1_objeto, y1_objeto = centro_x - largo_habitacion * escala / 2 + posicion_x * escala, centro_y - ancho_habitacion * escala / 2 + posicion_y * escala
    x2_objeto, y2_objeto = x1_objeto + largo_objeto * escala, y1_objeto + ancho_objeto * escala
    lienzo.create_rectangle(x1_objeto, y1_objeto, x2_objeto, y2_objeto, outline="red")

# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora de Área de Limpieza")

# Crear marco para los controles
marco_controles = tk.Frame(ventana)
marco_controles.grid(row=0, column=0, padx=10, pady=10)

# Crear títulos para los campos de entrada
titulo_habitacion = tk.Label(marco_controles, text="Dimensión Habitación", font=("Helvetica", 14, "bold"))
titulo_habitacion.grid(row=0, column=0, columnspan=2, pady=(0,5))

titulo_largo_habitacion = tk.Label(marco_controles, text="Largo (m):")
titulo_largo_habitacion.grid(row=1, column=0)
entry_largo_habitacion = tk.Entry(marco_controles)
entry_largo_habitacion.grid(row=1, column=1)

titulo_ancho_habitacion = tk.Label(marco_controles, text="Ancho (m):")
titulo_ancho_habitacion.grid(row=2, column=0)
entry_ancho_habitacion = tk.Entry(marco_controles)
entry_ancho_habitacion.grid(row=2, column=1)

titulo_objeto = tk.Label(marco_controles, text="Dimensión Objeto", font=("Helvetica", 14, "bold"))
titulo_objeto.grid(row=3, column=0, columnspan=2, pady=(10,5))

titulo_largo_objeto = tk.Label(marco_controles, text="Largo (m):")
titulo_largo_objeto.grid(row=4, column=0)
entry_largo_objeto = tk.Entry(marco_controles)
entry_largo_objeto.grid(row=4, column=1)

titulo_ancho_objeto = tk.Label(marco_controles, text="Ancho (m):")
titulo_ancho_objeto.grid(row=5, column=0)
entry_ancho_objeto = tk.Entry(marco_controles)
entry_ancho_objeto.grid(row=5, column=1)

titulo_posicion = tk.Label(marco_controles, text="Posición Objeto", font=("Helvetica", 14, "bold"))
titulo_posicion.grid(row=6, column=0, columnspan=2, pady=(10,5))

titulo_posicion_x = tk.Label(marco_controles, text="X (m):")
titulo_posicion_x.grid(row=7, column=0)
entry_posicion_x = tk.Entry(marco_controles)
entry_posicion_x.grid(row=7, column=1)

titulo_posicion_y = tk.Label(marco_controles, text="Y (m):")
titulo_posicion_y.grid(row=8, column=0)
entry_posicion_y = tk.Entry(marco_controles)
entry_posicion_y.grid(row=8, column=1)

# Botón para calcular el área
boton_calcular = tk.Button(marco_controles, text="Calcular Área", command=calcular_area)
boton_calcular.grid(row=9, column=0, columnspan=2, pady=10)

# Crear marco para mostrar los resultados
marco_resultados = tk.Frame(ventana)
marco_resultados.grid(row=0, column=1, padx=10, pady=10)

# Etiquetas para mostrar los resultados
resultado_area_habitacion = tk.Label(marco_resultados, text="")
resultado_area_habitacion.grid(row=0, column=0, sticky="w", padx=5, pady=2)

resultado_area_objeto = tk.Label(marco_resultados, text="")
resultado_area_objeto.grid(row=1, column=0, sticky="w", padx=5, pady=2)

resultado_area_limpiar = tk.Label(marco_resultados, text="")
resultado_area_limpiar.grid(row=2, column=0, sticky="w", padx=5, pady=2)

# Crear lienzo para visualizar habitación y objeto
lienzo_frame = tk.Frame(ventana, bg="white", bd=2, relief="groove")
lienzo_frame.grid(row=0, column=2, padx=10, pady=10)

lienzo = tk.Canvas(lienzo_frame, width=400, height=300, bg="white")
lienzo.pack()

ventana.mainloop()































