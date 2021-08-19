from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
    return {"message": "alhamdulillah wa syukurillah. Allahu Akbar! Allahu Akbar! Allahu Akbar!"}
