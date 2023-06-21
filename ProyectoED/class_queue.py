class Queue:
    def __init__(self, value = []):
        self.queue = list(value)
        self.size = len(value)
    
    def enqueue(self, value):
        self.queue.append(value)
        self.size += 1

    def dequeue(self):
        if self.size != 0:
            self.size -=1
            return self.queue.pop(0)
        else:
            print('the Queue is empty')
    
    def sizeQueue(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
    def peek(self):
        if self.size != 0:
            return self.queue[0]
    
    def print(self):
        print(' '.join(map(str, self.queue)),end='')
    
    def reversed(self):
        self.queue.reverse()