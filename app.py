#!/usr/bin/env python3
from flask import Flask, render_template, request, jsonify
from database import init_database, create_extraction, get_extraction, get_all_extractions
from worker import worker
import os
import atexit

app = Flask(__name__)

with app.app_context():
    init_database()
    worker.start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/extract', methods=['POST'])
def extract():
    try:
        data = request.json
        
        start_url = data.get('startUrl')
        tool_name = data.get('toolName', 'MyAPI')
        api_base_url = data.get('apiBaseUrl')
        
        if not start_url or not api_base_url:
            return jsonify({'error': 'Campos obrigatórios não preenchidos'}), 400
        
        extraction_id = create_extraction({
            'startUrl': start_url,
            'toolName': tool_name,
            'apiBaseUrl': api_base_url
        })
        
        if not extraction_id:
            return jsonify({'error': 'Erro ao criar extração no banco de dados'}), 500
        
        return jsonify({
            'success': True,
            'message': 'Extração adicionada à fila de processamento',
            'extraction_id': extraction_id,
            'status': 'pending'
        })
    
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

@app.route('/api/extraction/<int:extraction_id>', methods=['GET'])
def get_extraction_status(extraction_id):
    try:
        extraction = get_extraction(extraction_id)
        
        if not extraction:
            return jsonify({'error': 'Extração não encontrada'}), 404
        
        return jsonify({
            'success': True,
            'extraction': extraction
        })
    
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

@app.route('/api/extractions', methods=['GET'])
def list_extractions():
    try:
        limit = request.args.get('limit', 50, type=int)
        extractions = get_all_extractions(limit=limit)
        
        return jsonify({
            'success': True,
            'extractions': extractions,
            'count': len(extractions)
        })
    
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

def cleanup():
    worker.stop()

atexit.register(cleanup)

if __name__ == '__main__':
    init_database()
    worker.start()
    try:
        app.run(debug=True, port=5000)
    finally:
        cleanup()
