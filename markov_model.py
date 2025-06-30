import random

class MarkovChain:
    def __init__(self, order=1):
        self.order = order
        self.model = {}

    def train(self, text):
        words = text.split()
        for i in range(len(words) - self.order):
            key = tuple(words[i:i+self.order])
            next_word = words[i + self.order]
            if key not in self.model:
                self.model[key] = []
            self.model[key].append(next_word)

    def generate(self, length=50):
        if not self.model:
            return ""
        key = random.choice(list(self.model.keys()))
        result = list(key)
        for _ in range(length - self.order):
            next_words = self.model.get(key)
            if not next_words:
                break
            next_word = random.choice(next_words)
            result.append(next_word)
            key = tuple(result[-self.order:])
        return ' '.join(result)
