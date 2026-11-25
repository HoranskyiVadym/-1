class Inventory:
    def init(self, slots, stack):
        self.slots, self.stack, self.items = slots, stack, {}

    def used(self):
        return sum(-(-c // self.stack) for c in self.items.values())

    def add(self, name, n=1):
        added = 0
        for _ in range(n):
            if self.items.get(name, 0) % self.stack == 0 and self.used() >= self.slots:
                break
            self.items[name] = self.items.get(name, 0) + 1
            added += 1
        return added

    def remove(self, name, n=1):
        if self.items.get(name, 0) < n:
            raise ValueError(f"Недостатньо: {name}")
        self.items[name] -= n
        if self.items[name] == 0:
            del self.items[name]

    def show(self, title):
        print(f"\n{title} ({self.used()}/{self.slots} слотів)")
        for name, c in self.items.items():
            print(f"  {name} x{c}")