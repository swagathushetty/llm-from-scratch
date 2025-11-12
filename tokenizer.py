import re
from collections import Counter

class Tokenizer:
    def __init__(self):
        self.vocab = {} # word to id
        self.reverse_vocab = {} # id to word

    def build_vocab(self,text,vocab_size=10000):
        words = re.findall(r'\w+|[^\w\s]', text.lower())

        total_words = Counter(words) # {'hello':10,'a':4,..............}

        # Take n(vocab size) most common words
        # we are reserving 2 spots for special tokens
        most_common = total_words.most_common(vocab_size-2) # [('hello',10),('a',4)]

        #special tokens
        self.vocab = {
            '<PAD>': 0,  # Padding
            '<UNK>': 1,  # Unknown
        }

        for word,_ in most_common:
            #note- len(self.vocab) acts like unique auto-incrementing id since len increases with each addition
            # eg - {'<PAD>':0,'<UNK>':1,'hello':2,'a':3,.....}
            self.vocab[word] = len(self.vocab) 

        # need for decoding
        self.reverse_vocab = { v:k for k,v in self.vocab.items()}

        return self.vocab



tokenizerInstance = Tokenizer() 
tokenizerInstance.build_vocab("Hello world! This is a test. Hello again.",vocab_size=10)
print(tokenizerInstance.vocab)
print(tokenizerInstance.reverse_vocab)

