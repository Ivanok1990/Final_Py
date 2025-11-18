from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="Keiser University Grade Processor",
    description="Proyecto Final - Omar Quintanilla",
    version="1.0"
)

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
        <head>
            <title>¡TODO FUNCIONA!</title>
            <style>
                body { font-family: Arial; text-align: center; margin-top: 100px; background: #f0f8ff; }
                h1 { color: #2c3e50; }
                p { font-size: 20px; color: #27ae60; }
            </style>
        </head>
        <body>
            <h1>¡FastAPI está funcionando perfectamente!</h1>
            <p>Backend listo para el proyecto final</p>
            <p>Ve a: <a href="/docs">/docs</a> para ver la documentación interactiva</p>
            <hr>
            <small>Omar Quintanilla - Fall 2025</small>
        </body>
    </html>
    """

@app.get("/hola")
async def hola():
    return {"mensaje": "¡Todo bien, Omar y alexis! El backend ya sirve"}