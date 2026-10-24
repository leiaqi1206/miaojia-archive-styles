from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="喵家档案 API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/api/health")
def health_check() -> dict[str, str]:
    """报告 API 服务状态。"""
    return {"status": "ok"}


@app.get("/api/message")
def get_message() -> dict[str, str]:
    """返回供前端联调使用的欢迎消息。"""
    return {"message": "喵家档案后端连接成功"}
