from fastapi import (FastAPI, responses, Request)
from fastapi.staticfiles import StaticFiles
from .dependencies import templates
from .middlewares.token import TokenAuthMiddleware, CORSMiddleware
from .middlewares.ip_bans import IPBanMiddleware
from .routers.files import files
from .routers.products import products
from .settings import (IP_BANED, BASE_DIR, MEDIA_DIR, MEDIA_ENDPOINT, STAICS_DIR, STAICS_ENDPOINT, os, TEMPLATES_DIR)
from rich.console import Console
from rich.text import Text
from .models.users import User
from .database import engine, Base

console = Console()

app = FastAPI()
app.include_router(
    files,
    prefix="/files",
    tags=["files"],
    responses={404: {"description": "Not found"}},
)

app.include_router(
    products,
    prefix="/products",
    tags=["products"],
    responses={404: {"description": "Not found"}},
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    TokenAuthMiddleware,
    activate = False
    )

app.add_middleware(
    IPBanMiddleware,
    ip_bans=IP_BANED,
    )

app.mount(STAICS_ENDPOINT, StaticFiles(directory=STAICS_DIR), name="static")
app.mount(MEDIA_ENDPOINT, StaticFiles(directory=MEDIA_DIR), name="media")

@app.on_event("startup")
async def startup_event():
    if not os.path.exists(STAICS_DIR):
        os.makedirs(STAICS_DIR)
        console.print(f"Directorio creado: [bold green]{STAICS_DIR}[/bold green]", style="bold green")
    else:
        console.print(f"Directorio encontrado: [bold green]{STAICS_DIR}[/bold green]", style="bold green")

    if not os.path.exists(MEDIA_DIR):
        os.makedirs(MEDIA_DIR)
        console.print(f"Directorio creado: [bold green]{MEDIA_DIR}[/bold green]", style="bold green")
    else:
        console.print(f"Directorio encontrado: [bold green]{MEDIA_DIR}[/bold green]", style="bold green")

    if not os.path.exists(f"{BASE_DIR}/data"):
        os.makedirs(f"{BASE_DIR}/data")
        console.print(f"Directorio creado: [bold green]{BASE_DIR}/data[/bold green]", style="bold green")
    else:
        console.print(f"Directorio encontrado: [bold green]{BASE_DIR}/data[/bold green]", style="bold green")

    if not os.path.exists(f"{BASE_DIR}/data/database.db"):
        with open(f"{BASE_DIR}/data/database.db", "w") as f:
            pass
        console.print(f"Archivo creado: [bold green]{BASE_DIR}/data/database.db[/bold green]", style="bold green")
    else:
        console.print(f"Archivo encontrado: [bold green]{BASE_DIR}/data/database.db[/bold green]", style="bold green")
    
    Base.metadata.create_all(engine)
    console.print(f"Tablas creadas en la base de datos", style="bold green")

@app.get("/")
async def root(request:Request):
    return templates.TemplateResponse(
        request,
        name = "base.html",
    )