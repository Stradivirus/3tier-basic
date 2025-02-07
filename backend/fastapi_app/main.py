from fastapi import FastAPI

app = FastAPI(
    docs_url="/api/docs",
    openapi_url="/api/openapi.json"
)

@app.get("/api/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/health")
async def health_check():
    return {"status": "ok"}