from fastapi import FastAPI

app = FastAPI(title="cupinudous ai")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}