class PotentialFunction:
    def __init__(self):
        self.stack = []
        self.potential = 0

    def push(self, x):
        self.stack.append(x)
        self.potential += 1 

    def pop(self):
        if not self.stack:
            return None
        self.potential -= 1 
        return self.stack.pop()

    def get_potential(self):
        return self.potential

pf = PotentialFunction()
pf.push(1)
pf.push(2)
print(f"Потенциал: {pf.get_potential()}")  # Потенциал = 2
pf.pop()
print(f"Потенциал: {pf.get_potential()}")  # Потенциал = 1
