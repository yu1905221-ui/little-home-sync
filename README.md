# Notion 小窝整理器（最小演示版）

这是一个**不接真实 Notion API**、不需要任何 token 的 Python 演示项目。
目标是：读取代码里写死的示例文本，生成一张本地的“今日同步卡”。

## 项目结构

```text
.
├─ src/
│  ├─ main.py
│  ├─ sample_data.py
│  └─ summarize.py
├─ output/
│  └─ .gitkeep
├─ requirements.txt
└─ README.md
```

## 每个文件是做什么的

- `src/sample_data.py`
  - 放一段中文示例内容，模拟“小窝里今天新增的内容”。
- `src/summarize.py`
  - 把示例文本整理成固定格式：
    - 今日同步卡
    - 今日新增
    - 值得归档
    - 待确认
    - 给知言看的摘要
- `src/main.py`
  - 程序入口。
  - 负责串起流程：读取示例内容 → 调用整理逻辑 → 写入 `output/today_sync.md`。
- `output/.gitkeep`
  - 用来保留空目录 `output/`（方便 Git 跟踪）。
- `requirements.txt`
  - 当前无第三方依赖（仅标准库）。
- `README.md`
  - 项目说明与运行步骤。

## 如何运行（演示版）

在项目根目录执行：

```bash
python src/main.py
```

运行成功后会看到提示，并生成文件：

- `output/today_sync.md`

你可以直接打开这个文件查看“今日同步卡”。

## 下一步如何升级成真实 Notion 版本

建议按这个顺序升级：

1. **接入配置管理**
   - 新增 `.env`（不提交真实密钥）。
   - 用环境变量保存 `NOTION_API_KEY`、`DATABASE_ID`。
2. **封装 Notion 客户端层**
   - 新增 `src/notion_client.py`，专门处理 API 请求。
3. **把输入来源从“写死文本”改成“Notion 页面/数据库”**
   - 读取今日新增条目，转换成当前的整理函数输入。
4. **把输出从本地文件改成“回写 Notion”**
   - 在 Notion 新建“今日同步卡”页面，并写入整理结果。
5. **增加异常处理和日志**
   - 例如网络失败重试、请求报错提示、基础日志记录。

> 先保持当前结构简单，等流程跑稳后再逐步替换数据来源与输出目标。
