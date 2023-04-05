from janome.tokenizer import Tokenizer
import re

tokenizer = Tokenizer()

class Tokenizer:
    
    @classmethod
    def tokenize(cls, text):
        raise NotImplementedError

class JanomeTokenizer(Tokenizer):
    
    @classmethod
    def tokenize(cls, text):
        return (t for t in cls.tokenize.tokenize(text))

class WhiteSpaceTokenizer(Tokenizer):
    
    @classmethod
    def tokenize(cls, text):
        return (t for t in re.finditer(r"[^ \t\r\n]+", text))