class User:
    def __init__(self, name):
        self.name = name
        self.memory = {}
        self.runs = 0

    def remember(self, key, value):
        self.memory[key] = value

    def recall(self, key):
        if key in self.memory:
            return self.memory[key]
        return "I don't know"

    def add_run(self):
        self.runs += 1

    def to_dict(self):
        return {'name': self.name, 'memory': self.memory, 'runs': self.runs}

    def __str__(self):
        return f'{self.name} (runs: {self.runs}, facts: {len(self.memory)})'    

    def greet(self):
        return f"Hello, {self.name}!"

    def bye(self):
        return f"Bye, {self.name}!"


if __name__ == '__main__':
    u = User("Ali")
    u.remember("city", "Buxoro")
    u.add_run()
    u.add_run()
    print(u.recall("city"), u.recall("age"))
    print(u)

# comment 2