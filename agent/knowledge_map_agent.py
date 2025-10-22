"""
KnowledgeMap Agent - 自定义智能体实现
基于Cursor的大模型能力构建知识图谱智能体
"""

import json
import logging
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from datetime import datetime

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class Entity:
    """实体类"""
    id: str
    name: str
    type: str
    properties: Dict[str, Any]
    created_at: datetime = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()

@dataclass
class Relation:
    """关系类"""
    id: str
    source: str
    target: str
    relation_type: str
    properties: Dict[str, Any]
    created_at: datetime = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()

class KnowledgeMapAgent:
    """知识图谱智能体"""
    
    def __init__(self, config_path: str = "agent/config.json"):
        """初始化智能体"""
        self.config = self._load_config(config_path)
        self.entities: Dict[str, Entity] = {}
        self.relations: Dict[str, Relation] = {}
        self.knowledge_graph = {}
        
        logger.info(f"KnowledgeMap Agent 初始化完成 - 模型: {self.config.get('model', 'claude-3.7-sonnet')}")
    
    def _load_config(self, config_path: str) -> Dict[str, Any]:
        """加载配置文件"""
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.warning(f"配置文件 {config_path} 不存在，使用默认配置")
            return {
                "name": "KnowledgeMap Agent",
                "model": "claude-3.7-sonnet",
                "capabilities": ["知识图谱构建", "实体关系提取"]
            }
    
    def extract_entities(self, text: str) -> List[Entity]:
        """从文本中提取实体"""
        logger.info(f"开始从文本中提取实体，文本长度: {len(text)}")
        
        # 这里可以集成Cursor的大模型API来提取实体
        # 示例实现
        entities = []
        
        # 模拟实体提取（实际应用中会调用Cursor的AI能力）
        sample_entities = [
            {"name": "人工智能", "type": "技术", "properties": {"category": "AI"}},
            {"name": "机器学习", "type": "技术", "properties": {"category": "ML"}},
            {"name": "深度学习", "type": "技术", "properties": {"category": "DL"}}
        ]
        
        for i, entity_data in enumerate(sample_entities):
            entity = Entity(
                id=f"entity_{i+1}",
                name=entity_data["name"],
                type=entity_data["type"],
                properties=entity_data["properties"]
            )
            entities.append(entity)
            self.entities[entity.id] = entity
        
        logger.info(f"成功提取 {len(entities)} 个实体")
        return entities
    
    def extract_relations(self, text: str, entities: List[Entity]) -> List[Relation]:
        """从文本中提取关系"""
        logger.info(f"开始从实体间提取关系，实体数量: {len(entities)}")
        
        relations = []
        
        # 模拟关系提取
        if len(entities) >= 2:
            relation = Relation(
                id="relation_1",
                source=entities[0].id,
                target=entities[1].id,
                relation_type="相关",
                properties={"strength": 0.8}
            )
            relations.append(relation)
            self.relations[relation.id] = relation
        
        logger.info(f"成功提取 {len(relations)} 个关系")
        return relations
    
    def build_knowledge_graph(self, entities: List[Entity], relations: List[Relation]) -> Dict[str, Any]:
        """构建知识图谱"""
        logger.info("开始构建知识图谱")
        
        graph = {
            "nodes": [],
            "edges": [],
            "metadata": {
                "created_at": datetime.now().isoformat(),
                "entity_count": len(entities),
                "relation_count": len(relations)
            }
        }
        
        # 添加节点
        for entity in entities:
            graph["nodes"].append({
                "id": entity.id,
                "name": entity.name,
                "type": entity.type,
                "properties": entity.properties
            })
        
        # 添加边
        for relation in relations:
            graph["edges"].append({
                "id": relation.id,
                "source": relation.source,
                "target": relation.target,
                "relation_type": relation.relation_type,
                "properties": relation.properties
            })
        
        self.knowledge_graph = graph
        logger.info(f"知识图谱构建完成 - 节点: {len(graph['nodes'])}, 边: {len(graph['edges'])}")
        
        return graph
    
    def query_graph(self, query: str) -> Dict[str, Any]:
        """查询知识图谱"""
        logger.info(f"执行图谱查询: {query}")
        
        # 简单的查询实现
        results = {
            "query": query,
            "results": [],
            "timestamp": datetime.now().isoformat()
        }
        
        # 根据查询类型返回不同结果
        if "实体" in query or "entity" in query.lower():
            results["results"] = list(self.entities.values())
        elif "关系" in query or "relation" in query.lower():
            results["results"] = list(self.relations.values())
        else:
            results["results"] = self.knowledge_graph
        
        return results
    
    def save_graph(self, filepath: str = "knowledge_graph.json"):
        """保存知识图谱到文件"""
        logger.info(f"保存知识图谱到: {filepath}")
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(self.knowledge_graph, f, ensure_ascii=False, indent=2)
        
        logger.info("知识图谱保存成功")
    
    def load_graph(self, filepath: str = "knowledge_graph.json"):
        """从文件加载知识图谱"""
        logger.info(f"从文件加载知识图谱: {filepath}")
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                self.knowledge_graph = json.load(f)
            
            # 重建实体和关系字典
            self.entities = {}
            self.relations = {}
            
            for node in self.knowledge_graph.get("nodes", []):
                entity = Entity(
                    id=node["id"],
                    name=node["name"],
                    type=node["type"],
                    properties=node["properties"]
                )
                self.entities[entity.id] = entity
            
            for edge in self.knowledge_graph.get("edges", []):
                relation = Relation(
                    id=edge["id"],
                    source=edge["source"],
                    target=edge["target"],
                    relation_type=edge["relation_type"],
                    properties=edge["properties"]
                )
                self.relations[relation.id] = relation
            
            logger.info("知识图谱加载成功")
            
        except FileNotFoundError:
            logger.warning(f"文件 {filepath} 不存在")
    
    def get_status(self) -> Dict[str, Any]:
        """获取智能体状态"""
        return {
            "name": self.config.get("name", "KnowledgeMap Agent"),
            "model": self.config.get("model", "claude-3.7-sonnet"),
            "capabilities": self.config.get("capabilities", []),
            "entity_count": len(self.entities),
            "relation_count": len(self.relations),
            "graph_status": "已构建" if self.knowledge_graph else "未构建",
            "timestamp": datetime.now().isoformat()
        }

# 主程序入口
if __name__ == "__main__":
    # 创建智能体实例
    agent = KnowledgeMapAgent()
    
    # 示例使用
    sample_text = "人工智能是计算机科学的一个分支，机器学习是人工智能的核心技术，深度学习是机器学习的一个重要分支。"
    
    print("=== KnowledgeMap Agent 演示 ===")
    print(f"智能体状态: {agent.get_status()}")
    
    # 提取实体
    entities = agent.extract_entities(sample_text)
    print(f"\n提取的实体: {[e.name for e in entities]}")
    
    # 提取关系
    relations = agent.extract_relations(sample_text, entities)
    print(f"\n提取的关系: {[f'{r.source} -> {r.target}' for r in relations]}")
    
    # 构建知识图谱
    graph = agent.build_knowledge_graph(entities, relations)
    print(f"\n知识图谱构建完成: {graph['metadata']}")
    
    # 保存图谱
    agent.save_graph()
    
    print("\n=== 智能体演示完成 ===")
