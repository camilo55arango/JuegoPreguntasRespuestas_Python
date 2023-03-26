preguntas = [
    ("¿Cuál es el océano más grande del mundo?", "Pacífico"),
    ("¿En qué país se encuentra la Torre Eiffel?", "Francia"),
    ("¿Cuál es la capital de España?", "Madrid"),
    ("¿Quién pintó la Mona Lisa?", "Da Vinci"),
    ("¿Cuál es el río más largo del mundo?", "Nilo"),
]

def jugar():
    puntuacion = 0
    for pregunta, respuesta in preguntas:
        print(pregunta)
        intento = input("Respuesta: ")
        if intento.lower() == respuesta.lower():
            print("¡Correcto!")
            puntuacion += 1
        else:
            print(f"Incorrecto. La respuesta correcta era {respuesta}")
    print(f"Tu puntuación final es: {puntuacion}")

jugar()
