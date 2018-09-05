from collections import deque
class MatcherQueue:
    def __init__(self):
        self.queue = deque()
        self.list_is_filled = False

    def enqueue(self, item):
        self.queue.append(item)
        self.list_is_filled = True

    def __len__(self):
        return len(self.queue)

    def dequeue(self):
        if self.list_is_filled:
            item = self.queue.popleft()
            if len(self.queue) == 0:
                self.list_is_filled = False
            return item
        return (None, None)


