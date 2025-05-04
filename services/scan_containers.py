# scan_containers.py
from datetime import datetime
from fastapi import HTTPException
from pydantic import BaseModel

# Simulando base de datos
contenedores_db = {
    "123456": {"id": 1, "peso_inicial": 100, "volumen_inicial": 50, "peso_actual": 100, "volumen_actual": 50},
    "654321": {"id": 2, "peso_inicial": 120, "volumen_inicial": 60, "peso_actual": 120, "volumen_actual": 60},
}

class CodigoRequest(BaseModel):
    codigo: str

class FinalizarRequest(BaseModel):
    codigo: str
    tiempoTranscurrido: float

class ValidationResponse(BaseModel):
    message: str

class FinalizeResponse(BaseModel):
    message: str

def validar_codigo(codigo: str) -> ValidationResponse:
    """
    Función para validar si el código del contenedor es válido.
    """
    contenedor = contenedores_db.get(codigo)
    
    if not contenedor:
        raise HTTPException(status_code=400, detail="Código no válido")
    
    return ValidationResponse(message="Acceso permitido")

def finalizar(codigo: str, tiempo_transcurrido: float) -> FinalizeResponse:
    """
    Función para finalizar el proceso de reciclaje y actualizar la base de datos.
    """
    contenedor = contenedores_db.get(codigo)
    
    if not contenedor:
        raise HTTPException(status_code=400, detail="Código no válido")

    # Simulación de la cantidad de reciclaje añadido
    contenedor["peso_actual"] += 5  # Incrementamos el peso en 5 kg
    contenedor["volumen_actual"] += 2  # Incrementamos el volumen en 2 m³

    # Registra el tiempo transcurrido
    tiempo_minuto = tiempo_transcurrido / 60  # Convertir a minutos
    
    # Generamos el mensaje de respuesta
    message = (
        f"Reciclaje completado en {tiempo_minuto:.2f} minutos. "
        f"Reciclaje añadido: 5 kg y 2 m³. "
        f"Nuevo peso: {contenedor['peso_actual']} kg, nuevo volumen: {contenedor['volumen_actual']} m³."
    )
    
    return FinalizeResponse(message=message)
