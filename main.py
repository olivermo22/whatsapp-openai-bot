from fastapi import FastAPI, Request
import openai
import os

app = FastAPI()

# Lee tu API key desde una variable de entorno
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.get("/")
def inicio():
    return {"mensaje": "Servidor funcionando correctamente"}

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    mensaje_usuario = data.get("Body", "")
    numero = data.get("From", "")

    if not mensaje_usuario:
        return {"message": "No se recibió mensaje"}

    respuesta_ai = openai.ChatCompletion.create(
        model="gpt-4o mini",
        messages=[
            {"role": "system", "content": "Eres un asistente útil y amigable."},
            {"role": "user", "content": mensaje_usuario}
        ]
    )

    mensaje_respuesta = respuesta_ai.choices[0].message["content"]
    return {"message": mensaje_respuesta}
