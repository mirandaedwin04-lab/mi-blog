import os
import datetime
#1. Obtener fecha y hora para el mensaje del summit
ahora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
mensaje = input(f"Escribe un mensaje para el commit (Enter para usar '{ahora}'):")
if not mensaje:
    mensaje = f"Actualización automática: {ahora}"

#2. Ejecutar comandos de git
os.system("git add .")  
print(f"Creando commit: '{mensaje}'...")
os.system(f'git commit -m "{mensaje}"')

print("Subiendo a la nube...")
os.system("git pusH")
print("¡Hecho!")
