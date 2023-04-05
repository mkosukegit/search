from janome.tokenizer.Token import Token
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

STOPWORDS = ("is", "was", "to", "the")

class TokenFilter:
    
    @classmethod
    def filter(cls, token):
        raise NotImplementedError
    
class StopWordFilter(TokenFilter):
    
    @classmethod
    def filter(cls, token):
        if isinstance(token, Token):
            if token.surface in STOPWORDS:
                return None
        if token in STOPWORDS:
            return None
        return token

"""
複数形を除く
"""
class Stemmer(TokenFilter):
    
    @classmethod
    def filter(cls, token):
        if token:
            return ps.stem(token)