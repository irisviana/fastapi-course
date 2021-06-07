from fastapi import FastAPI
from core.config import settings
from db.session import engine
from db.base_class import Base


def create_tables():
    Base.metadata.create_all(bind=engine)


def star_application():
    app = FastAPI(title=settings.PROJECT_TITTLE,
                  varion=settings.PROJECT_VERSION)
    create_tables()
    return app

app = star_application()


@app.get("/")
def hello_api():
    return {"detail": "Hello word"}

