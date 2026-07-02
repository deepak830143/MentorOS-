from fastapi import FastAPI
from app.api.auth_routes import router as auth_router

print("Router Type:", type(auth_router))
print("Number of routes:", len(auth_router.routes))

for r in auth_router.routes:
    print(r.path, r.methods)

app = FastAPI()
app.include_router(auth_router)