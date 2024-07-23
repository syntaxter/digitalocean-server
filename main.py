from fastapi import FastAPI, HTTPException
import subprocess
import os

app = FastAPI()

@app.get("/webhook")
async def webhook():
    # Obtén el directorio actual donde se ejecuta el script
    repo_directory = os.getcwd()

    # Verifica que el directorio actual es válido
    if not os.path.isdir(repo_directory):
        raise HTTPException(status_code=500, detail="Directorio actual no encontrado")

    try:
        # Ejecuta el comando git pull en el directorio actual
        result = subprocess.run(["git", "pull"], cwd=repo_directory, capture_output=True, text=True, check=True)
        return {"status": "success", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        # Maneja errores en la ejecución del comando
        raise HTTPException(status_code=500, detail=repo_directory)
