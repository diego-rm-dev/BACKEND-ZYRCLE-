# scan.py
from fastapi import APIRouter
from services.scan_containers import validar_codigo, finalizar, CodigoRequest, FinalizarRequest, ValidationResponse, FinalizeResponse

router = APIRouter()

@router.post("/contenedor/validar-codigo", response_model=ValidationResponse)
async def validate_code(codigo: CodigoRequest):
    """
    Endpoint para validar el código del contenedor.
    """
    return validar_codigo(codigo.codigo)

@router.post("/contenedor/finalizar", response_model=FinalizeResponse)
async def finish_recycling(data: FinalizarRequest):
    """
    Endpoint para finalizar el proceso de reciclaje.
    """
    return finalizar(data.codigo, data.tiempoTranscurrido)
