import re

from App.Counters.counter import Counter


class WordsCounter(Counter):

    def get_count(self, chunk: str) -> int:
        words = re.findall(r'(\s+)', chunk)
        return len(words)

    def should_count_last(self, chunk: str) -> bool:
        return not bool(re.search(r'\s$', chunk))