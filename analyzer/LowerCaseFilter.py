import CharFilter

class LowerCaseFilter(CharFilter):
    
    @classmethod
    def filter(cls, text:str):
        return text.lower()