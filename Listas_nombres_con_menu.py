# Importo librerías
import json
import os

# Función para cargar los datos
def cargar_personas():
    if os.path.exists("personas.json"):
        with open("personas.json", "r", encoding="utf-8") as archivo:
            contenido = archivo.read(),strip()
            if contenido:
                return json.loads(archivo)
            else:
                return[]
    else:
        return[]

# Función para cargar los datos
def guardar_personas(personas):
    with open("personas.json", "w", encoding="utf-8") as archivo:
        json.dump(personas, archivo, indent=4, ensure_ascii=False)

    
# Determinar el listado de personas
personas = cargar_personas()


while True: 
    print("\n¿Qué deseas hacer?")
    print("1. Listar personas")
    print("2. Agregar persona")
    print("3. Eliminar persona")
    print("4. Editar persona")
    print("5. Salir")
    
    try:
        opcion = int(input("Selecciona una opción del 1 al 5: "))
        if not 1 <= opcion <= 5:
            print("\nError: Número fuera de rango. Intente de nuevo")
            continue
    except ValueError:
        print("\nError: Debes ingresar un número válido")
    
    # Listar personas
    if opcion == 1:
        print("\nLISTADO DE PERSONAS: ")
        for indice, persona in enumerate(personas):
            print(F"{indice} - {persona['nombre']} ({persona['meta']})")
        print("__---___---")
        
    # Agregar persona
    elif opcion == 2:
        nombre = input("\n¿Cuál es el nombre de la persona nueva? ")
        meta = input("\n¿Cuál es la meta de esta persona? ")
        
        nueva_persona = {
            "nombre": nombre,
            "meta" : meta
        }
        personas.append(nueva_persona)
        guardar_personas(personas)
        print("Persona agregada exitosamente")
        
        
    # Eliminar persona
    elif opcion == 3:
        for indice, persona in enumerate(personas):
            print(f"{indice} - {persona['nombre']} ({persona['meta']})")
            
        indice_a_eliminar = int(input("\n¿Que número de usuario quieres eliminar? "))
        
        if 0 <=indice_a_eliminar < len(personas):
            del personas[indice_a_eliminar]
            guardar_personas(personas)
            print("Persona eliminada exitosamente")
        else:
            print("Número inválido, no se eliminó ninguna persona")
          
    # Editar los datos de un usuario  
    elif opcion == 4:
        for indice, persona in enumerate(personas):
            print(f"{indice} - {persona['nombre']} ({persona['meta']})")
            
        indice_a_editar = int(input("\n¿Qué número de usuario deseas editar? "))
        
        if 0 <= indice_a_editar < len(personas):
            opcion_editar = input("¿Qué deseas editar? (nombre/meta/ambos): ").lower()
            if opcion_editar == "nombre":
                nuevo_nombre = input("nuevo nombre: ")
                personas[indice_a_editar]['nombre'] = nuevo_nombre
                guardar_personas(personas)
                print("Nombre actualizado")
            elif opcion_editar == "meta":
                nueva_meta = input("nueva meta: ")
                personas[indice_a_editar]["meta"] = nueva_meta
                guardar_personas(personas)
                print("Meta actualizada")
            elif opcion_editar == "ambos":
                nuevo_nombre = input("nuevo nombre: ")
                nueva_meta = input("nueva meta: ")
                personas[indice_a_editar]["nombre"] = nuevo_nombre
                personas[indice_a_editar]["meta"] = nueva_meta
                guardar_personas(personas)
                print("Nombre y Meta han sido actualizados.")
            else:
                print("Opción de edición no válida")
        else:
            print("Número inválido. No se editó ninguna persona")
              
    # Salir del programa      
    elif opcion == 5:
        print("¡Gracias por usar el sistema!")
        break
    else:
        print("Opción inválida, intente de nuevo")