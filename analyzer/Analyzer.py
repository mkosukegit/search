class Analyzer:
    tokenizer = None
    char_filters = []
    token_filters = []
    
    @classmethod
    def analyze(cls, text_input: str):
        text = cls.char_filter(text_input)
        
    @classmethod
    def char_filter(cls, text_input):
        for char_filter in cls.char_filters:
            text = char_filter.filter(text_input)
        return text
        
    @classmethod
    def token_filter(cls, token_input):
        for token_filter in cls.token_filters:
            token = token_filter.filter(token_input)
        return token