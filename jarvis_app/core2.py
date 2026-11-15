# comment
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
            result[name] = self.users[name].to_dict()
        save_memory(path, result)

    def load(self, path):
        data = load_memory(path)
        for name, info in data.items():
            new_u = User(name)
            new_u.memory = info['memory']
            new_u.runs = info['runs']
            self.users[name] = new_u

