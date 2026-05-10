
#Etapa 1: Datos sin normalizar
print("\nEtapa 1: Datos crudos (no normalizados)")
estudiantes = [
    [1, "Juan", "Pérez", 20, "Madrid", ["Matemáticas", "Programación"], [85, 90]],
    [2, "María", "García", 22, "Barcelona", ["Anatomía", "Fisiología"], [88, 92]],
    [1, "Juan", "Pérez", 20, "Madrid", ["Matemáticas", "Programación"], [85, 90]]  
]
for e in estudiantes:
    print(e)

# Etapa 2: Primera Forma Normal (1FN)
print("\nEtapa 2: 1FN - Valores simples")
datos_1fn = []
for e in estudiantes:
    i = 0
    for materia in e[5]:  # Materias
        fila = [e[0], e[1], e[2], e[3], e[4], materia, e[6][i] if i < len(e[6]) else 0]
        datos_1fn.append(fila)
        i += 1
for d in datos_1fn:
    print(d)

# Etapa 3: Segunda Forma Normal (2FN)
print("\nEtapa 3: 2FN - Separamos estudiantes e inscripciones")
estudiantes_2fn = []
inscripciones = []
ids_vistos = []
for d in datos_1fn:
    if d[0] not in ids_vistos:
        estudiantes_2fn.append([d[0], d[1], d[2], d[3], d[4]])
        ids_vistos.append(d[0])
    inscripciones.append([d[0], d[5], d[6]])
print("Estudiantes:")
for e in estudiantes_2fn:
    print(e)
print("Inscripciones:")
for i in inscripciones:
    print(i)

# Etapa 4: Tercera Forma Normal (3FN) 
print("\nEtapa 4: 3FN - Separamos direcciones")
direcciones = []
estudiantes_3fn = []
direcciones_vistas = {}
id_dir = 1
for e in estudiantes_2fn:
    clave = e[4]  # Ciudad
    if clave not in direcciones_vistas:
        direcciones_vistas[clave] = id_dir
        direcciones.append([id_dir, clave])
        id_dir += 1
    estudiantes_3fn.append([e[0], e[1], e[2], e[3], direcciones_vistas[clave]])
print("Direcciones:")
for d in direcciones:
    print(d)
print("Estudiantes finales:")
for e in estudiantes_3fn:
    print(e)
print("Inscripciones (iguales):")
for i in inscripciones:
    print(i)
