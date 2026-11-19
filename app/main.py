
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import carro_routes
from app.routes import pedido_routes
from app.routes import cliente_routes

from app.database.inicializar import inicializar_banco
from app.database.popular_banco import popular_carros


app = FastAPI(
    title="LA Motors API",
    description="API do aplicativo mobile LA Motors",
    version="1.0.0"
)

@app.on_event("startup")
def iniciar_sistema():
    inicializar_banco()
    popular_carros()

# Permitir comunicacao com Flutter Web durante o desenvolvimento
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Rota inicial
@app.get("/")
def inicio():
    return {
        "mensagem": "Bem-vindo a API da LA Motors!"
    }


# Rota de teste
@app.get("/teste")
def teste():
    return {
        "status": "API funcionando!"
    }


# Registrar rotas
app.include_router(carro_routes.router)
app.include_router(cliente_routes.router)
app.include_router(pedido_routes.router)
