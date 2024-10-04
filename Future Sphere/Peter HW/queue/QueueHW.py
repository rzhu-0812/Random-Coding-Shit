import Heapq

class Customer:
    def __init__(self, id, service_time, priority):
        self.id = id    
        self.service_time = service_time
        self.priority = priority
    
class BankQueue:
    def __init__(self):
        self.queue = []
        self.temp_queue = []
        self.index = 0
    
    def enqueue(self, customer):
        Heapq.heappush(self.queue, [-customer.priority, self.index, customer.service_time, customer.id])
        Heapq.heappush(self.temp_queue, [-customer.priority, self.index, customer.service_time, customer.id])
        self.index += 1 


    def dequeue(self):
        if len(self.queue):
            print(f"Finished serving {self.queue[0][3]}\n")
            Heapq.heappop(self.queue)
        else:
            print("No customers in queue\n")
        
        if len(self.temp_queue):
            Heapq.heappop(self.temp_queue)
    
    def peek(self):
        if len(self.temp_queue):
            print(f"Next customer in line: {self.temp_queue[0][3]}\n")
        else:
            print(f"No more customers in line\n")
    
    def display(self):
        print("Customers Info:")
        for customer in self.queue:
            print(f"Customer ID: {customer[3]}, Service Time: {customer[2]}, Priority: {-customer[0]}")
        print()
    
    def total_waiting_time(self):
        total_wait = 0

        for queue in self.queue:
            total_wait += queue[2]
        
        print(f"The total wait time is {total_wait} minutes\n")
    
    def change_priority(self, customer_id, priotity):
        for customer in self.queue:
            if customer[3] == customer_id:
                customer[0] = -priotity
                break
        
        Heapq.heapify(self.queue)
    
    def get_info(self, customer_id):
        for customer in self.queue:
            if customer[3] == customer_id:
                print(f"Customer ID: {customer[3]}, Service Time: {customer[2]}, Priority: {-customer[0]}")
   