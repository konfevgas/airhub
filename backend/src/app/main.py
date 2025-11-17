from fastapi import FastAPI

app = FastAPI(title="KinderHub API")


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok", "service": "kinderhub-api"}
