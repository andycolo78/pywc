from App.Counters.counter import Counter


class LinesCounter(Counter):

    def get_count(self, chunk: str) -> int:
        return str(chunk).count('\n')

    def should_count_last(self, chunk: str) -> bool:
        return not chunk.endswith(('\n', '\r\n'))
