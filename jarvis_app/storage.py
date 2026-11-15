import os
import json

def load_memory(path):
    if os.path.exists(path):
        try: 
            with open(path, encoding='utf-8') as f:
                return json.load(f)
        except json.decoder.JSONDecodeError:
            print(f'Warning: {path} is broken, starting fresh')
            return {}
            
    return {}

def save_memory(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


