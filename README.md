# Cifrando un Mensaje a lo Vigenère

Este programa implementa el cifrado de una sola vía usando el algoritmo de Vigenère, siguiendo la fórmula:  
**Yi = (Xi + Zi) mod T**,  
donde cada letra del texto se cifra usando una clave también ingresada por el usuario.

## 🧩 Descripción

El objetivo del proyecto es sistematizar el algoritmo de cifrado de Vigenère mediante un programa con interfaz gráfica.  
Las principales características del programa son:

- Permite ingresar tanto el texto claro como la clave a través de una interfaz sencilla construida con Tkinter.
- No admite caracteres especiales, espacios ni la letra "ñ".  
- Aplica limpieza al texto:  
  - Convierte todo a mayúsculas  
  - Elimina símbolos  
  - Reemplaza letras acentuadas por su versión sin tilde  
  - La letra ñ se convierte en N
- Ajusta automáticamente la clave para que tenga la misma longitud que el texto ingresado.
- Muestra el mensaje cifrado por pantalla, aplicando la fórmula del cifrado Vigenère.


## 💻 Tecnologías usadas

- Python
- Tkinter (para la interfaz gráfica)

## 📝 Ejemplo de uso
### Entrada: 
**Texto claro:** seguridad de la información 
**Clave:** electiva 

### Salida: (al presionar el botón "Cifrar"): 
**Texto cifrado:** WPKWKQYAHOINTQIFSCQCVQJN

### Ejemplo visual:
![image](https://github.com/user-attachments/assets/602463f1-d0eb-44aa-8c59-b0ba7cf18b8a)

## ▶️ Cómo ejecutar

1. Asegúrate de tener instalado Python.
2. Tkinter viene incluido por defecto en la mayoría de instalaciones de Python.
3. Ejecuta el archivo desde la terminal o editor de código con el botón de "Run".

```bash
python Vigenère.py
