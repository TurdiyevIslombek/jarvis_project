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

print(load_memory("nope.json"))     
print(load_memory("bad.json"))
print(load_memory("ok.json"))