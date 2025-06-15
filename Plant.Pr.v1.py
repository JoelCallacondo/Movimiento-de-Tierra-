import tkinter as tk
from tkinter import ttk

# Funciones de cálculo
def calcular_respuesta1():
    try:
        largo_banco = float(Rescato1LB.get())
        ancho_banco = float(Rescato2AB.get())
        densidad = float(Rescato3DE.get())
        altura_banco = (largo_banco - 46.5) * (2/3)
        
        # Actualizar el campo de altura del banco
        altura_banco_var.set(f"{altura_banco:.2f}")
        
        resultado = altura_banco * ancho_banco * densidad * largo_banco
        RESPUESTA1_1.set(f"{resultado:.2f}")
    except ValueError:
        RESPUESTA1_1.set("Error en datos")

def calcular_respuesta2():
    try:
        densidad_explosivo = float(Rescato1DEX.get())
        diametro_pozo = float(Rescato2DIA.get())
        resultado = densidad_explosivo * (diametro_pozo ** 2) * 0.507
        RESPUESTA2_2.set(f"{resultado:.2f}")
    except ValueError:
        RESPUESTA2_2.set("Error en datos")

def calcular_respuesta3():
    try:
        altura = float(Rescato3AL.get())
        pasadura = float(Rescato1PAS.get())
        taco = float(Rescato2TAC.get())
        resultado = altura + pasadura - taco
        RESPUESTA3_3.set(f"{resultado:.2f}")
    except ValueError:
        RESPUESTA3_3.set("Error en datos")

def calcular_respuesta4():
    try:
        tonelaje = float(Rescato3TONE.get())
        altura_carga = float(Rescato3ALTU.get())
        resultado = tonelaje * altura_carga
        RESPUESTA4_4.set(f"{resultado:.2f}")
    except ValueError:
        RESPUESTA4_4.set("Error en datos")

# Configuración de la ventana principal
if __name__ == "__main__":
    root = tk.Tk()               
    root.title("Doc05 Ejercicio propuesto 8")
    root.geometry("600x800")
    root.config(bg="#E7F6F2")
    root.resizable(False, True)
    
    # Variables para los resultados
    RESPUESTA1_1 = tk.StringVar()
    RESPUESTA2_2 = tk.StringVar()
    RESPUESTA3_3 = tk.StringVar()
    RESPUESTA4_4 = tk.StringVar()
    altura_banco_var = tk.StringVar()

    # Frame para organizar mejor los elementos
    main_frame = ttk.Frame(root, padding="10")
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Encabezado - ORDEN CORREGIDO
    universidad = ttk.Label(main_frame, 
                          text="Universidad Nacional Jorge Basadre Grohmann - Facultad de Ingeniería - Escuela Profesional de Ingeniería de Minas",
                          font=("Bahnschrift", 8),
                          foreground="#2C3333")
    universidad.grid(row=0, column=0, columnspan=3, pady=(0, 5))

    titulo = ttk.Label(main_frame, 
                      text="Planteamiento del problema",
                      font=("Impact", 20),
                      foreground="#2C3333",
                      background="#A5C9CA")
    titulo.grid(row=1, column=0, columnspan=3, pady=(0, 5), sticky="ew")

    subtitulo = ttk.Label(main_frame, 
                         text="Creador: CALLACONDO HUARACHI JOEL FERNANDO",
                         font=("Bahnschrift", 10),
                         foreground="#2C3333")
    subtitulo.grid(row=2, column=0, columnspan=3, pady=(0, 20))

    # Sección 1 - Tonelaje a explotar
    seccion1_frame = ttk.LabelFrame(main_frame, text="N°01 - Tonelaje a explotar (Kg)", padding=10)
    seccion1_frame.grid(row=3, column=0, columnspan=3, sticky="ew", pady=(0, 20))

    # Campos para la sección 1
    ttk.Label(seccion1_frame, text="Ingresa el largo del banco (m):").grid(row=0, column=0, sticky="w")
    Rescato1LB = ttk.Entry(seccion1_frame)
    Rescato1LB.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(seccion1_frame, text="Altura del Banco (m):").grid(row=1, column=0, sticky="w")
    ttk.Label(seccion1_frame, textvariable=altura_banco_var).grid(row=1, column=1, sticky="w")

    ttk.Label(seccion1_frame, text="Ingresa el Ancho del banco (m):").grid(row=2, column=0, sticky="w")
    Rescato2AB = ttk.Entry(seccion1_frame)
    Rescato2AB.grid(row=2, column=1, padx=5, pady=5)

    ttk.Label(seccion1_frame, text="Ingresa la densidad (T/m3):").grid(row=3, column=0, sticky="w")
    Rescato3DE = ttk.Entry(seccion1_frame)
    Rescato3DE.grid(row=3, column=1, padx=5, pady=5)

    ttk.Button(seccion1_frame, 
              text="EJECUTAR N°01", 
              command=calcular_respuesta1).grid(row=4, column=0, columnspan=2, pady=10)

    ttk.Label(seccion1_frame, text="Resultado:").grid(row=5, column=0, sticky="w")
    ttk.Label(seccion1_frame, textvariable=RESPUESTA1_1).grid(row=5, column=1, sticky="w")

    # Sección 2 - Densidad de carga de explosivo
    seccion2_frame = ttk.LabelFrame(main_frame, text="N°02 - Densidad de carga de explosivo", padding=10)
    seccion2_frame.grid(row=4, column=0, columnspan=3, sticky="ew", pady=(0, 20))

    ttk.Label(seccion2_frame, text="Densidad del explosivo (gr/cc):").grid(row=0, column=0, sticky="w")
    Rescato1DEX = ttk.Entry(seccion2_frame)
    Rescato1DEX.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(seccion2_frame, text="Diámetro de un pozo de tronadura (in):").grid(row=1, column=0, sticky="w")
    Rescato2DIA = ttk.Entry(seccion2_frame)
    Rescato2DIA.grid(row=1, column=1, padx=5, pady=5)

    ttk.Button(seccion2_frame, 
              text="EJECUTAR N°02", 
              command=calcular_respuesta2).grid(row=2, column=0, columnspan=2, pady=10)

    ttk.Label(seccion2_frame, text="Resultado:").grid(row=3, column=0, sticky="w")
    ttk.Label(seccion2_frame, textvariable=RESPUESTA2_2).grid(row=3, column=1, sticky="w")

    # Sección 3 - Cálculos varios
    seccion3_frame = ttk.LabelFrame(main_frame, text="N°03 - Cálculos varios", padding=10)
    seccion3_frame.grid(row=5, column=0, sticky="ew", pady=(0, 20))

    ttk.Label(seccion3_frame, text="Pasadura (m):").grid(row=0, column=0, sticky="w")
    Rescato1PAS = ttk.Entry(seccion3_frame)
    Rescato1PAS.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(seccion3_frame, text="Taco (m):").grid(row=1, column=0, sticky="w")
    Rescato2TAC = ttk.Entry(seccion3_frame)
    Rescato2TAC.grid(row=1, column=1, padx=5, pady=5)

    ttk.Label(seccion3_frame, text="Altura de Banco (m):").grid(row=2, column=0, sticky="w")
    Rescato3AL = ttk.Entry(seccion3_frame)
    Rescato3AL.grid(row=2, column=1, padx=5, pady=5)

    ttk.Button(seccion3_frame, 
              text="EJECUTAR N°03", 
              command=calcular_respuesta3).grid(row=3, column=0, columnspan=2, pady=10)

    ttk.Label(seccion3_frame, text="Resultado:").grid(row=4, column=0, sticky="w")
    ttk.Label(seccion3_frame, textvariable=RESPUESTA3_3).grid(row=4, column=1, sticky="w")

    # Sección 4 - Consumo de explosivo
    seccion4_frame = ttk.LabelFrame(main_frame, text="N°04 - Consumo de explosivo (Kg)", padding=10)
    seccion4_frame.grid(row=5, column=1, sticky="ew", pady=(0, 20), padx=(10, 0))

    ttk.Label(seccion4_frame, text="Tonelaje a explotar (kg/m):").grid(row=0, column=0, sticky="w")
    Rescato3TONE = ttk.Entry(seccion4_frame)
    Rescato3TONE.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(seccion4_frame, text="Altura de carga (m):").grid(row=1, column=0, sticky="w")
    Rescato3ALTU = ttk.Entry(seccion4_frame)
    Rescato3ALTU.grid(row=1, column=1, padx=5, pady=5)

    ttk.Button(seccion4_frame, 
              text="EJECUTAR N°04", 
              command=calcular_respuesta4).grid(row=2, column=0, columnspan=2, pady=10)

    ttk.Label(seccion4_frame, text="Resultado:").grid(row=3, column=0, sticky="w")
    ttk.Label(seccion4_frame, textvariable=RESPUESTA4_4).grid(row=3, column=1, sticky="w")

    root.mainloop()