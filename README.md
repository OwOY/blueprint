# Blueprint 專案架構說明

<br>

## 📋 專案概述
Blueprint 是一個基於 **Clean Architecture（整潔架構）** 設計的 Python 專案模板，旨在提供一個可擴展、可維護、可測試的應用程式架構基礎。專案採用分層設計原則，確保關注點分離和依賴倒置。

## 專案架構
```text
app/
│
├── main.py                         # FastAPI 啟動入口
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env
├── .gitignore
│
├── src/
│   │
│   ├── main.py                     # 建立 FastAPI app
│   │
│   ├── routers/                    # API 路由層
│   │   ├── __init__.py
│   │   ├── users.py
│   │   ├── auth.py
│   │   └── health.py
│   │
│   ├── services/                   # 商業邏輯層
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── auth.py
│   │
│   ├── dependencies/               # FastAPI Depends
│   │   ├── __init__.py
│   │   ├── database.py
│   │   ├── auth.py
│   │
│   ├── models/                     # ORM Models
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── base.py
│   │
│   ├─  dtos/                       # 物件傳輸(DataTansferObject)
│   │   ├─ user.py
│   │   ├─ client/
│   │   │  └─azure.py
│   │   └─ auth.py
│   │
│   ├── schemas/                    # Pydantic Request/Response
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── auth.py
│   │
│   ├── repositories/               # Repository/Data Access(資料存取層)
│   │   ├── __init__.py
│   │   ├── user_repository.py
│   │   └── base.py
│   │
│   ├── infra/                      # 外部系統整合
│   │   ├── __init__.py
│   │   ├── database.py             # DB connection
│   │   ├── redis.py
│   │   ├── mail.py
│   │   └── storage.py
│   │
│   ├── enums/                      # 系統固定語意
│   │
│   │
│   ├── core/                       # 核心設定
│   │   ├── __init__.py
│   │   ├── config.py               # Settings
│   │   ├── security.py             # JWT/hash ...
│   │   ├── logging.py
│   │   ├── context.py              # 自定義存取物件
│   │   ├── exceptions.py
│   │   └── exception_handler.py
│   │
│   └── utils/                      # 共用工具
│       ├── __init__.py
│       └── datetime.py
│
├── migrations/                     # Alembic migration
│
├── tests/
│   ├── test_users.py
│   └── conftest.py
│
└── scripts/
    └── init_db.py
```
## 🏗️ 架構設計原則
### Clean Architecture 核心概念
- **依賴倒置**：內層不依賴外層，依賴關係指向內部
- **關注點分離**：每一層都有明確的職責範圍
- **可測試性**：業務邏輯與外部依賴解耦，便於單元測試
- **可擴展性**：新功能可以在不影響核心邏輯的情況下添加
<br>

### 分層架構圖
```text
┌─────────────────────────────────────────────────────────────┐
│                      Controllers Layer                      │
│                        (API 接口層)                          |
├─────────────────────────────────────────────────────────────┤
│                       Services Layer                        │
│                        (應用服務層)                          │
├─────────────────────────────────────────────────────────────┤
│      Repositories Layer      │        Clients Layer         │
│         (資料存取層)          │         (外部服務層)          │
├─────────────────────────────────────────────────────────────┤
│                       Schemas Layer                         │
│                        (資料模型層)                          │
├─────────────────────────────────────────────────────────────┤
│    Dependencies Layer        │          Cores Layer         │
│        (依賴注入層)           │          (核心配置層)         │
└─────────────────────────────────────────────────────────────┘
```

## 📁 資料夾結構與職責

###  `routers/` - API 接口層
**職責**：
- 提供 HTTP API 接入入口
- 管理 API 路由與資料格式
- 定義外部請求與回應契約
- 隔離 HTTP 層與內部業務邏輯

---

### `schemas/` - API 資料模型層
**職責**：
- 定義 HTTP Request 格式
- 定義 HTTP Response 格式
- 驗證 API 輸入資料
- 控制 API 輸出資料結構
- 隔離 API 契約與內部資料模型

---

### `services/` - 業務服務層
**職責**：
- 實現業務流程
- 處理商業規則
- 協調 Repository 與外部服務
- 管理應用層邏輯
- 接收與返回 DTO

---

### `dtos/` - 資料傳輸物件層
**職責**：
- 定義 Layer 間資料交換格式
- 作為 Service 層資料契約
- 隔離 API Schema 與 Database Model
- 避免不同 Layer 直接依賴

---

### `repositories/` - 資料存取層
**職責**：
- 管理資料庫存取
- 封裝 CRUD 操作
- 執行資料查詢
- 管理資料持久化邏輯
- 隔離 Service 與 Database

---

### `models/` - ORM 資料模型層
**職責**：
- 定義資料庫 Table 結構
- 建立 ORM 映射關係
- 管理資料欄位與關聯
- 提供資料庫操作模型

---

### `enums/` - 枚舉定義層
**職責**：
- 管理系統固定值
- 避免 Magic String
- 統一狀態與類型定義
- 提供跨 Layer 共用枚舉

---

### `dependencies/` - 依賴注入層
**職責**：
- 提供 FastAPI Dependency Injection
- 管理共享資源生命週期
- 注入 Service、Repository 與其他服務
- 處理認證與權限依賴

---

### `infra/` - 基礎設施層
**職責**：
- 管理外部系統整合
- 封裝第三方服務
- 提供基礎技術能力
- 隔離外部套件與服務依賴

---

### `core/` - 核心功能層
**職責**：
- 提供系統核心能力
- 管理全域設定
- 提供跨模組共用功能
- 定義系統級規則

---

### `utils/` - 工具函式層
**職責**：
- 提供共用工具函式
- 提供無狀態輔助功能
- 避免重複程式碼

---

### `tests/` - 測試層
**職責**：
- 驗證系統功能
- 測試 API 行為
- 測試 Service 業務邏輯
- 測試 Repository 資料操作

---

### `main.py` - 應用程式入口
**職責**：
- 初始化 FastAPI Application
- 註冊 Middleware
- 載入 Router
- 啟動應用程式