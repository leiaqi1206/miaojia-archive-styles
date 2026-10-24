# 喵家档案 · 视觉风格教学版

本项目复制自 `miaojia-archive`，后端完全相同。最终首页采用 Japanese Minimalist（日系极简）风格。目前仍不包含数据库、登录或猫咪档案管理功能。

## 最终首页风格

本次首页采用 **Japanese Minimalist（日系极简）**：用自然留白、细线分隔和清晰字级呈现猫咪档案，保持安静、易读的感觉。

- 背景浅蓝灰：`#F2F5F8`
- 主色靛蓝：`#2B4C6F`
- 正文深灰：`#2C363F`
- 点缀蓝灰：`#5B82A6`、鼠尾草绿：`#7A9A8B`
- 分隔线：`#D3DEEA`

十种风格草稿、对应提示词、14 种现有风格简评和最终选择记录见 [`style-exploration/`](style-exploration/index.html)。首页保留原有导航、四类功能、三步开始、CTA 和后端连接状态；最终页面只呈现选定的日系极简风格。

### 实现方式

- `frontend/src/App.vue`：首页结构和后端连接状态。
- `frontend/src/themes/base.css`：最终选定的日系极简视觉样式和响应式布局。
- `frontend/public/welcome-cat.jpg`：首页使用的猫咪照片。

## 环境要求

- Node.js 20+
- Python 3.10+

## 安装与启动后端

### Windows PowerShell

在项目根目录打开 PowerShell：

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

### macOS / Linux

在项目根目录打开终端：

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

后端地址：<http://127.0.0.1:8000>

- 健康检查：<http://127.0.0.1:8000/api/health>
- 消息接口：<http://127.0.0.1:8000/api/message>
- Swagger API 文档：<http://127.0.0.1:8000/docs>

健康检查预期返回：

```json
{"status":"ok"}
```

消息接口预期返回：

```json
{"message":"喵家档案后端连接成功"}
```

## 安装与启动前端

另开一个终端，在项目根目录运行（Windows PowerShell、macOS 和 Linux 命令相同）：

```bash
cd frontend
npm ci
npm run dev
```

前端地址：<http://localhost:5173>

前端默认请求 `http://127.0.0.1:8000`。如需更换后端地址，可在 `frontend` 目录创建 `.env` 文件并设置：

```text
VITE_API_BASE_URL=http://127.0.0.1:8000
```

## 验证流程

1. 启动后端和前端。
2. 打开 <http://localhost:5173>，页脚的状态点应为绿色，并显示后端消息。
3. 在后端终端按 `Ctrl+C` 停止后端，刷新页面，页脚应显示"后端暂不可用"和"重试"按钮。
4. 重新运行后端启动命令，点击页脚的"重试"，页面应恢复显示成功消息。
5. 单独访问上面的健康检查和消息接口地址，检查 JSON 响应。

运行后端测试：

Windows PowerShell：

```powershell
cd backend
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

macOS / Linux：

```bash
cd backend
source .venv/bin/activate
python -m unittest discover -s tests -v
```
