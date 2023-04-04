from janome.tokenizer import Tokenizer

tokenizer = Tokenizer()

class Tokenizer:
    
    @classmethod
    def tokenize(cls, text):
        raise NotImplementedError

class JanomeTokenizer(Tokenizer):
    
    @classmethod
    def tokenize(cls, text):
        return (t for t in cls.tokenize.tokenize(text))