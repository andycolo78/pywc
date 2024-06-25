from App.Counters.counter import Counter


class BytesCounter(Counter):

    def get_count(self, chunk: str) -> int:
        return len(chunk)
