import heapq as Heapq

class CircularQueue:
    def __init__(self, size):
        self.queue = [None] * size
        self.max_size = size
        self.front = self.rear = -1

    def enqueue(self, item):
        if self.is_full():
            print("Queue is Full\n")
        else:
            if self.is_empty():
                self.front = 0
            self.rear = (self.rear + 1) % self.max_size
            self.queue[self.rear] = item
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty\n")
            return None
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size
        return item
    
    def peek(self):
        if self.is_empty():
            print("Queue is Empty\n")
            return None
        return self.queue[self.front]
    
    def is_empty(self):
        return self.front == -1 and self.rear == -1
    
    def is_full(self):
        return (self.rear + 1) % self.max_size == self.front


class PrintQueue:
    def __init__(self):
        self.queue = []
        self.temp_queue = []
        self.index = 0
    
    def add_document(self, doc_id, name, priority):
        Heapq.heappush(self.queue, (-priority, self.index, doc_id, name))
        Heapq.heappush(self.temp_queue, (-priority, self.index, doc_id, name))
        self.index += 1
    
    def print_document(self):
        if len(self.queue):
            print(f"Finished printing {self.queue[0][2]}\n")
            Heapq.heappop(self.queue)
        else:
            print("No documents in queue\n")
        
        if len(self.temp_queue):
            Heapq.heappop(self.temp_queue)
    
    def view_next_doc(self):
        if len(self.temp_queue):
            next_doc = self.temp_queue[0]
            print(f"Next document in queue: {next_doc[2]}\n")
        else:
            print("No more documents in queue\n")
        
    def view_all_documents(self):
        print("Documents in Queue:")
        for doc in self.queue:
            print(f"Document ID: {doc[3]}, Name: {doc[2]}, Priority: {-doc[0]}")
        print()
