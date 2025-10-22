"""
Flask Web应用 - 为KnowledgeMap Agent提供Web界面
"""

from flask import Flask, render_template, request, jsonify
import json
import os
from agent.knowledge_map_agent import KnowledgeMapAgent

app = Flask(__name__)

# 初始化智能体
agent = KnowledgeMapAgent()

@app.route('/')
def index():
    """主页"""
    return render_template('index.html')

@app.route('/api/status')
def get_status():
    """获取智能体状态"""
    return jsonify(agent.get_status())

@app.route('/api/extract', methods=['POST'])
def extract_knowledge():
    """提取知识"""
    data = request.get_json()
    text = data.get('text', '')
    
    if not text:
        return jsonify({'error': '文本不能为空'}), 400
    
    try:
        # 提取实体
        entities = agent.extract_entities(text)
        
        # 提取关系
        relations = agent.extract_relations(text, entities)
        
        # 构建知识图谱
        graph = agent.build_knowledge_graph(entities, relations)
        
        return jsonify({
            'success': True,
            'entities': [{'id': e.id, 'name': e.name, 'type': e.type} for e in entities],
            'relations': [{'id': r.id, 'source': r.source, 'target': r.target, 'type': r.relation_type} for r in relations],
            'graph': graph
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/query', methods=['POST'])
def query_graph():
    """查询知识图谱"""
    data = request.get_json()
    query = data.get('query', '')
    
    if not query:
        return jsonify({'error': '查询不能为空'}), 400
    
    try:
        results = agent.query_graph(query)
        return jsonify(results)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/save', methods=['POST'])
def save_graph():
    """保存知识图谱"""
    try:
        agent.save_graph()
        return jsonify({'success': True, 'message': '知识图谱保存成功'})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/load', methods=['POST'])
def load_graph():
    """加载知识图谱"""
    try:
        agent.load_graph()
        return jsonify({'success': True, 'message': '知识图谱加载成功'})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # 确保templates目录存在
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static', exist_ok=True)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
