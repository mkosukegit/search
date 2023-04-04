import analyzer.CharFilter as CharFilter
import re

class HtmlSplitFilter(CharFilter):
    
    @classmethod
    def filter(cls, text : str):
        html_pattern = re.compile(r"<[^>]*?")
        return html_pattern.sub("", text)