import json
import os

# Almacenamiento en memoria
containers = []

# Archivo para guardar los contenedores
DATA_FILE = "containers.json"

def store_containers(new_data: list):
    containers.clear()
    containers.extend(new_data)
    save_to_disk()

def get_all_containers():
    return containers

# Guarda los contenedores en un archivo JSON
def save_to_disk():
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(containers, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"[ERROR] No se pudo guardar contenedores: {e}")

# Carga los contenedores al iniciar si el archivo existe
def load_from_disk():
    global containers
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                containers = json.load(f)
                print(f"[INFO] {len(containers)} contenedores cargados desde disco.")
        except Exception as e:
            print(f"[ERROR] No se pudo cargar contenedores: {e}")
