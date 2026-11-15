from jarvis_app.user import User
from jarvis_app.storage import load_memory, save_memory

class Jarvis:
    def __init__(self):
        self.users = {}

    def get_user(self, name):
        if name in self.users:
            return self.users[name]
        
        self.users[name] = User(name)
        return self.users[name]

    def report(self):
        summaries = []
        for name in self.users:
            summaries.append(str(self.users[name]))
        return summaries
    
    def save(self, path):
        result = {}
        for name in self.users:
            obj = self.users[name]
            result[name] = obj.to_dict()
        save_memory(path, result)

    def load(self, path):
        memory = load_memory(path)
        for name, info in memory.items():
            u = User(name)
            u.memory = info['memory']
            u.runs = info['runs']
            self.users[name] = u

