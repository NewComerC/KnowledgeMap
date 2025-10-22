# KnowledgeMap Agent - 自定义智能体实现指南

## 项目简介

KnowledgeMap Agent 是一个基于 Cursor 大模型能力的自定义智能体，专门用于知识图谱的构建、管理和查询。该智能体可以：

- 🔍 从文本中自动提取实体和关系
- 🧠 构建结构化的知识图谱
- 🔎 提供智能查询功能
- 💾 支持图谱的保存和加载
- 🌐 提供现代化的Web界面

## 功能特性

### 核心功能
- **实体提取**: 从文本中识别和提取关键实体
- **关系识别**: 发现实体之间的语义关系
- **图谱构建**: 自动构建结构化的知识图谱
- **智能查询**: 支持自然语言查询图谱内容
- **数据持久化**: 支持图谱的保存和加载

### 技术特点
- 基于 Cursor 的大模型能力
- 支持多种实体类型和关系类型
- 提供 RESTful API 接口
- 现代化的 Web 用户界面
- 可扩展的架构设计

## 项目结构

```
KnowledgeMap/
├── agent/
│   ├── config.json              # 智能体配置文件
│   └── knowledge_map_agent.py   # 核心智能体实现
├── templates/
│   └── index.html               # Web界面模板
├── app.py                       # Flask Web应用
├── requirements.txt             # Python依赖
└── README.md                    # 项目文档
```

## 安装和运行

### 1. 环境要求
- Python 3.8+
- Cursor IDE
- 支持 Agent 模式的模型（如 claude-3.7-sonnet）

### 2. 安装依赖
```bash
pip install -r requirements.txt
```

### 3. 运行智能体
```bash
# 运行Web应用
python app.py

# 或者直接运行智能体
python agent/knowledge_map_agent.py
```

### 4. 访问Web界面
打开浏览器访问: http://localhost:5000

## 使用方法

### 1. 在Cursor中使用后台智能体

1. **启动后台智能体**:
   - 在 Cursor 侧边栏选择"后台代理"标签页
   - 或按 `Ctrl+E` 触发后台代理模式

2. **配置环境**:
   - 智能体会在隔离的 Ubuntu 环境中运行
   - 自动安装依赖并启动服务

3. **连接GitHub**:
   - 智能体会从 GitHub 克隆仓库
   - 在单独分支上工作并推送更改

### 2. Web界面使用

1. **查看智能体状态**: 显示当前实体数量、关系数量和图谱状态
2. **知识提取**: 输入文本，自动提取实体和关系
3. **图谱查询**: 使用自然语言查询图谱内容
4. **图谱管理**: 保存和加载知识图谱

### 3. API接口

#### 获取智能体状态
```http
GET /api/status
```

#### 提取知识
```http
POST /api/extract
Content-Type: application/json

{
    "text": "要分析的文本内容"
}
```

#### 查询图谱
```http
POST /api/query
Content-Type: application/json

{
    "query": "查询语句"
}
```

#### 保存图谱
```http
POST /api/save
```

#### 加载图谱
```http
POST /api/load
```

## 配置说明

### agent/config.json
```json
{
    "name": "KnowledgeMap Agent",
    "description": "知识图谱构建和管理智能体",
    "version": "1.0.0",
    "model": "claude-3.7-sonnet",
    "capabilities": [
        "知识图谱构建",
        "实体关系提取",
        "知识推理",
        "文档分析",
        "代码生成"
    ],
    "environment": {
        "snapshot": "POPULATED_FROM_SETTINGS",
        "install": "pip install -r requirements.txt",
        "terminals": [
            {
                "name": "知识图谱服务",
                "command": "python app.py"
            }
        ]
    }
}
```

## 扩展开发

### 1. 添加新的实体类型
在 `KnowledgeMapAgent` 类中修改 `extract_entities` 方法：

```python
def extract_entities(self, text: str) -> List[Entity]:
    # 添加新的实体识别逻辑
    # 可以集成Cursor的AI能力进行更精确的实体提取
    pass
```

### 2. 自定义关系类型
修改 `extract_relations` 方法：

```python
def extract_relations(self, text: str, entities: List[Entity]) -> List[Relation]:
    # 添加新的关系识别逻辑
    # 支持更复杂的关系类型
    pass
```

### 3. 集成Cursor AI能力
可以通过以下方式集成Cursor的大模型能力：

```python
# 使用Cursor的AI API进行实体提取
def extract_entities_with_ai(self, text: str):
    # 调用Cursor的AI接口
    # 返回结构化的实体信息
    pass
```

## 注意事项

1. **模型选择**: 确保在Cursor设置中启用了支持Agent模式的模型
2. **权限配置**: 为GitHub仓库授予读写权限以支持智能体协作
3. **环境隔离**: 后台智能体在隔离环境中运行，确保安全性
4. **资源管理**: 大型知识图谱可能消耗较多内存，注意监控资源使用

## 故障排除

### 常见问题

1. **智能体无法启动**
   - 检查Cursor设置中的模型配置
   - 确认网络连接正常
   - 查看错误日志

2. **实体提取不准确**
   - 调整文本预处理逻辑
   - 优化实体识别算法
   - 考虑使用更强大的模型

3. **Web界面无法访问**
   - 检查Flask应用是否正常启动
   - 确认端口5000未被占用
   - 查看控制台错误信息

## 贡献指南

欢迎贡献代码和建议！请遵循以下步骤：

1. Fork 项目
2. 创建功能分支
3. 提交更改
4. 发起 Pull Request

## 许可证

MIT License

## 联系方式

如有问题或建议，请通过以下方式联系：
- 创建 Issue
- 发送邮件
- 参与讨论

---

**注意**: 此智能体基于Cursor的大模型能力构建，需要有效的Cursor订阅才能使用完整的AI功能。