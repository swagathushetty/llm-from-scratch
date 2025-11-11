import re
from collections import Counter

class Tokenizer:
    def __init__(self):
        self.vocab = {} # word to id
        self.reverse_vocab = {} # id to word

    def build_vocab(self,text,vocab_size=10000):
        pass

