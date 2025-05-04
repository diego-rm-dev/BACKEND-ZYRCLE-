from fastapi import FastAPI
from routes import iot, rutas, stats, residencia, status, scan
from services import iot_service
from fastapi.middleware.cors import CORSMiddleware



origins = [
    "http://localhost:8080",
    "https://g9ph372w-8080.use2.devtunnels.ms"
]

app = FastAPI(title="♻️ Eco Backend - Web3 Recycling MVP")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8080",
        "https://g9ph372w-8080.use2.devtunnels.ms"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Cargar contenedores al iniciar
iot_service.load_from_disk()

# Include modular routers
app.include_router(iot.router, prefix="/api/iot", tags=["IoT"])
app.include_router(rutas.router, prefix="/api", tags=["Rutas"])
app.include_router(stats.router, prefix="/api/stats", tags=["Stats"])
app.include_router(residencia.router, prefix="/api/residencia", tags=["Residencia"])
app.include_router(status.router, prefix="/api", tags=["Status"])
app.include_router(scan.router, prefix="/api", tags=["Scan"])
