import queue

class CustomerService:
    def __init__(self):
        self.customer_queue = queue.Queue()
        self.ticket_number = 1  # Starting ticket number
    
    def add_customer(self):
        # Assign a ticket number and add the customer to the queue
        customer = self.ticket_number
        self.customer_queue.put(customer)
        print(f"Customer with ticket number {customer} added to the queue.")
        self.ticket_number += 1  # Increment ticket number for the next customer
    
    def serve_customer(self):
        if not self.customer_queue.empty():
            customer = self.customer_queue.get()
            print(f"Serving customer with ticket number {customer}.")
        else:
            print("No customers in the queue.")
    
    def queue_status(self):
        print(f"There are {self.customer_queue.qsize()} customers in the queue.")
        if self.customer_queue.empty():
            print("The queue is empty.")

# Example usage:
service = CustomerService()

# Add customers to the queue
service.add_customer()  # Customer 1
service.add_customer()  # Customer 2
service.add_customer()  # Customer 3

# Check the queue status
service.queue_status()

# Serve customers
service.serve_customer()  # Serving Customer 1
service.serve_customer()  # Serving Customer 2

# Check the queue status again
service.queue_status()

# Serve the last customer
service.serve_customer()  # Serving Customer 3
service.serve_customer()  # No customers in the queue
