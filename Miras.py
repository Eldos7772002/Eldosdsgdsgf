class MemoryManager:
    def __init__(self, memory_size):
        self.memory = [None] * memory_size

    def first_fit(self, process_id, process_size):
        for i in range(len(self.memory)):
            if self.memory[i] is None:
                if i + process_size <= len(self.memory):
                    self.memory[i:i+process_size] = [process_id] * process_size
                    return i
        return -1

    def best_fit(self, process_id, process_size):
        best_fit = None
        for i in range(len(self.memory)):
            if self.memory[i] is None:
                if i + process_size <= len(self.memory):
                    if best_fit is None or (self.memory[i:i+process_size].count(None) < self.memory[best_fit:best_fit+process_size].count(None)):
                        best_fit = i
        if best_fit is not None:
            self.memory[best_fit:best_fit+process_size] = [process_id] * process_size
            return best_fit
        return -1

    def next_fit(self, process_id, process_size):
        last_index = getattr(self, 'last_index', 0)
        for i in range(last_index, len(self.memory)):
            if self.memory[i] is None:
                if i + process_size <= len(self.memory):
                    self.memory[i:i+process_size] = [process_id] * process_size
                    self.last_index = i
                    return i
        for i in range(last_index):
            if self.memory[i] is None:
                if i + process_size <= last_index:
                    self.memory[i:i+process_size] = [process_id] * process_size
                    self.last_index = i
                    return i
        return -1

    def worst_fit(self, process_id, process_size):
        worst_fit = None
        for i in range(len(self.memory)):
            if self.memory[i] is None:
                if i + process_size <= len(self.memory):
                    if worst_fit is None or (self.memory[i:i+process_size].count(None) > self.memory[worst_fit:worst_fit+process_size].count(None)):
                        worst_fit = i
        if worst_fit is not None:
            self.memory[worst_fit:worst_fit+process_size] = [process_id] * process_size
            return worst_fit
        return -1
memory_manager = MemoryManager(100)

# First Fit
index = memory_manager.first_fit(process_id=1, process_size=20)
if index != -1:
    print("Allocated", 20 ,"units of memory for process ",1)

