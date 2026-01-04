from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from core.inference import run_inference

app = FastAPI(title='Ulcer Foot Detection')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=['*'],
    allow_headers=['*']
)
@app.post('/infer')
async def infer(image: UploadFile = File(...)):
    image_bytes = await image.read()
    result = run_inference(image_bytes)
    return result