from fastapi import FastAPI
from handlers.adminhandlers import router as admin_router
from handlers.userhandlers import router as user_router
import uvicorn

app = FastAPI(title="GameSales service")

app.include_router(admin_router)
app.include_router(user_router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, host="127.0.0.1", reload=True)
