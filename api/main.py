from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="demo api",
    description="To test api deployment using docker containers in azure vm"
)

allowed_origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# playtation exlusives as a dictionary with keys of name and studio
games_list = [
    {"name": "God of War", "studio": "Santa Monica Studio"},
    {"name": "Uncharted", "studio": "Sony"},
    {"name": "Mortal Kombat", "studio": "Warner Bros"},
    {"name": "The Last of Us", "studio": "Naughty Dog"},
    {"name": "Spiderman", "studio": "Sony"},
    {"name": "Halo", "studio": "Microsoft"},
    {"name": "Call of Duty", "studio": "Infinity Ward"},
    {"name": "Gears of War", "studio": "Earthworm"},
    {"name": "Assasins Creed", "studio": "Ubisoft"},
]


@app.get("/home")
def home():
    return {"message": "Hello World"}

@app.get("/games")
def games():
    return {"games":games_list}


@app.post("/upload")
def upload(file: UploadFile = File(...)):
    with open(f"./uploads/{file.filename}", "wb") as buffer:
        contents = file.file.read()
        buffer.write(contents)
    return {"filename": file.filename}