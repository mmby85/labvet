from fastapi import FastAPI
import uvicorn
import  models
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from database import  engine
from  routes import auth,user,famile,nature,methode,echantillon,client,demande,association,statistique,parametre,departement




models.Base.metadata.create_all(bind=engine)   
    


origins = ["*"]
middleware = [ Middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'])]
app = FastAPI(middleware=middleware)


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def home():
    return 'hello world'

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(famile.router)
app.include_router(nature.router)
app.include_router(methode.router)
app.include_router(parametre.router)
app.include_router(echantillon.router)
app.include_router(client.router)
app.include_router(demande.router)
app.include_router(parametre.router)
app.include_router(departement.router)
app.include_router(association.router)
app.include_router(statistique.router)

if __name__ == "__main__":
    uvicorn.run(app, port=5000)
