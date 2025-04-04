import tkinter as tk
from tkinter import messagebox
from tkinter import font

# Función para limpiar el texto antes del cifrado
# Convierte ñ en N, elimina espacios y tildes y pasa todo a mayúsculas
def limpiar_texto(texto):
    REEMPLAZOS = {
        'á': 'A',
        'é': 'E',
        'í': 'I',
        'ó': 'O',
        'ú': 'U',
        'ñ': 'N',  # La ñ se convierte en N mayúscula
    }
    
    texto_limpio = (
        REEMPLAZOS.get(c.lower(), c.upper())  # Reemplaza tildes y ñ
        for c in texto
        if c.isalpha()  # Solo permite letras (sin números ni símbolos como el espacio o cáracteres especiales)
    )
    
    return ''.join(texto_limpio)

# Función para generar una clave del mismo tamaño que el texto claro
# Se repite la clave hasta igualar la longitud del texto o se corta si el texto es más corto que la llave
def generar_clave(texto, clave):
    clave = limpiar_texto(clave)
    return (clave * (len(texto) // len(clave) + 1))[:len(texto)]

# Función que implementa el cifrado de Vigenère
def cifrar_vigenere(texto, clave):
    texto = limpiar_texto(texto)  # Se limpia el texto
    clave = generar_clave(texto, clave)  # Se ajusta la clave a la longitud del texto
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    texto_cifrado = ''
    # Lo que hace zip es emparejar los elementos iterables, o sea que el primer caracter del texto se alinea con el primero de la clave
    for t, k in zip(texto, clave): 
        # Se calcula el nuevo índice sumando los valores del texto y la clave
        nuevo_indice = (alfabeto.index(t) + alfabeto.index(k)) % len(alfabeto) # Aquí se aplica Yi = (Xi + Zi) ModT 
        texto_cifrado += alfabeto[nuevo_indice]
    
    return texto_cifrado

# Función que obtiene los valores de la interfaz y realiza el cifrado
def cifrar():
    texto_claro = entrada_texto.get()
    clave = entrada_clave.get()
    if not texto_claro or not clave:
        messagebox.showerror("Error", "Debe ingresar texto y clave.")
        return
    texto_cifrado = cifrar_vigenere(texto_claro, clave)
    resultado_label.config(text=f"Texto cifrado: {texto_cifrado}")

# Interfaz gráfica
root = tk.Tk()
root.title("Cifrado de Vigenère")
root.geometry("500x400")
root.configure(bg="#2C3E50")

titulo_font = font.Font(family="Helvetica", size=16, weight="bold")
label_font = font.Font(family="Helvetica", size=12)
resultado_font = font.Font(family="Helvetica", size=14, weight="bold")

titulo = tk.Label(root, text="Cifrado de Vigenère", bg="#2C3E50", fg="white", font=titulo_font)
titulo.pack(pady=10)

tk.Label(root, text="Texto Claro:", bg="#2C3E50", fg="white", font=label_font).pack()
entrada_texto = tk.Entry(root, width=45, font=label_font)
entrada_texto.pack(pady=5)

tk.Label(root, text="Clave:", bg="#2C3E50", fg="white", font=label_font).pack()
entrada_clave = tk.Entry(root, width=45, font=label_font)
entrada_clave.pack(pady=5)

boton_cifrar = tk.Button(root, text="Cifrar", command=cifrar, font=label_font, bg="#E74C3C", fg="white", padx=10, pady=5)
boton_cifrar.pack(pady=15)

resultado_label = tk.Label(root, text="", bg="#34495E", fg="#ECF0F1", font=resultado_font, wraplength=450, padx=10, pady=10, relief="groove", bd=2)
resultado_label.pack(pady=15, fill="both", expand=True)

root.mainloop()