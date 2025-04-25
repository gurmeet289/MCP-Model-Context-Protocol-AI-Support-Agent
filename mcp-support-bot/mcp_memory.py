import json
from datetime import datetime

MEMORY_FILE_PATH = 'sample_data/memory_store.json'

def load_memory():
    try:
        with open(MEMORY_FILE_PATH, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except UnicodeDecodeError as e:
        print(f"Decode error: {e}")
        return []

def save_memory(memory):
    try:
        with open(MEMORY_FILE_PATH, 'w', encoding='utf-8') as file:
            json.dump(memory, file, indent=4, ensure_ascii=False)
    except UnicodeEncodeError as e:
        print(f"Save error: {e}")

def store_memory(user_id, issue_type, plan, message):
    memory = load_memory()
    new_chunk = {
        "user_id": user_id,
        "timestamp": datetime.now().isoformat(),
        "issue_type": issue_type,
        "plan": plan,
        "message": message
    }
    memory.append(new_chunk)
    save_memory(memory)

def retrieve_relevant_chunks(user_id, issue_type=None):
    memory = load_memory()
    if issue_type:
        return [chunk for chunk in memory if chunk['user_id'] == user_id and chunk['issue_type'] == issue_type]
    return [chunk for chunk in memory if chunk['user_id'] == user_id]
