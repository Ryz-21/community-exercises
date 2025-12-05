from datetime import datetime

def obtener_respuesta(texto):
    t = texto.lower().strip()

    # saludos
    if any(w in t for w in ["hola","buenas","hey","buenos"]):
        return "Hola. ¿En qué puedo ayudarte hoy?"
    
    # despedidas
    if any(w in t for w in ["adios", "chao","hasta luego", "nos vemos"]):
        return "Hasta luego, que tengas un buen día."
    
    # ayuda o problema
    if "ayuda" in t or "problema" in t:
        return "Dime tu problema y te voy a ayudar."
    
    # hora
    if "hora" in t or "que hora" in t:
        return "La hora actual es " + datetime.now().strftime("%H:%M")
    
    return "Lo siento. Aún estoy aprendiendo, ¿puedo reformularlo?"

def main():
    print("Chatbot (escribe salir para terminar)")
    while True:
        entrada = input("tu: ")
        if entrada.lower().strip() in ("salir","exit","quit"):
            print("bot: Adiós!")
            break
        respuesta = obtener_respuesta(entrada)
        print("bot:", respuesta)

if __name__ == "__main__":
    main()
