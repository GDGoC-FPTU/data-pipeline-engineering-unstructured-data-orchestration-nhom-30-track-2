import os
import json
from glob import glob

# Import các thành phần
from schema import UnifiedDocument
from process_unstructured import process_pdf_data, process_video_data
from quality_check import run_semantic_checks

# ==========================================
# ROLE 4: DEVOPS & INTEGRATION SPECIALIST
# ==========================================

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = os.path.join(CURRENT_DIR, "..", "raw_data")
DESTINATION_FILE = os.path.join(CURRENT_DIR, "..", "processed_knowledge_base.json")

def read_json_file(filepath):
    """Đọc file JSON và trả về dict"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def execute_pipeline():
    knowledge_base = []
    
    # 1. Ingest Group A (PDF files)
    pdf_pattern = os.path.join(DATA_FOLDER, "group_a_pdfs", "*.json")
    for file_path in glob(pdf_pattern):
        raw_data = read_json_file(file_path)
        cleaned_doc = process_pdf_data(raw_data)
        
        if run_semantic_checks(cleaned_doc):
            validated_doc = UnifiedDocument(**cleaned_doc)
            knowledge_base.append(validated_doc.model_dump())

    # 2. Ingest Group B (Video files)
    video_pattern = os.path.join(DATA_FOLDER, "group_b_videos", "*.json")
    for file_path in glob(video_pattern):
        raw_data = read_json_file(file_path)
        cleaned_doc = process_video_data(raw_data)
        
        if run_semantic_checks(cleaned_doc):
            validated_doc = UnifiedDocument(**cleaned_doc)
            knowledge_base.append(validated_doc.model_dump())

    # 3. Export Data
    with open(DESTINATION_FILE, 'w', encoding='utf-8') as f:
        json.dump(knowledge_base, f, indent=2, ensure_ascii=False)
        
    print(f"✅ Pipeline executed successfully! Total valid records saved: {len(knowledge_base)}")

if __name__ == "__main__":
    execute_pipeline()
