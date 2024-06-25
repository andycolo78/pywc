from App.Counters.counter import Counter


class LinesCounter(Counter):

    def get_count(self, chunk: str) -> int:
        return str(chunk).count('\n')
