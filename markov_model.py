# markov_model.py

import random

class MarkovChainGenerator:
    def __init__(self, n=2):
        self.n = n
        self.model = {}

    def train(self, text):
        tokens = text.split()
        for i in range(len(tokens) - self.n):
            key = tuple(tokens[i:i+self.n])
            next_word = tokens[i+self.n]
            if key not in self.model:
                self.model[key] = []
            self.model[key].append(next_word)

    def generate(self, length=50):
        if not self.model:
            return ""
        start = random.choice(list(self.model.keys()))
        result = list(start)
        for _ in range(length):
            key = tuple(result[-self.n:])
            next_words = self.model.get(key)
            if not next_words:
                break
            result.append(random.choice(next_words))
        return ' '.join(result)
