import time
import asyncio
from asyncio import Queue
from random import randrange

class Product:
    def __init__(self, product_name: str, checkout_time: float):
        self.product_name = product_name
        self.checkout_time = checkout_time

class Customer:
    def __init__(self, customer_id: int, products: list[Product]):
        self.customer_id = customer_id
        self.products = products

async def checkout_customer(queue: Queue, cashier_number: int):
    cashier_take = {'id': cashier_number, 'time': 0, 'customer': 0}
    
    while not queue.empty():
        customer: Customer = await queue.get()
        customer_start_time = time.perf_counter()
        cashier_take['customer'] += 1
        
        print(f"The Cashier_{cashier_number} "
              f"will checkout Customer_{customer.customer_id}")
              
        for product in customer.products:
            product_take_time = round(product.checkout_time, ndigits=2)
            print(f"The Cashier_{cashier_number} "
                  f"will checkout Customer_{customer.customer_id}'s "
                  f"Product+{product.product_name} "
                  f"in {product.checkout_time} secs")
            await asyncio.sleep(product_take_time)
            cashier_take['time'] += product_take_time

        cashier_finish_time = round(time.perf_counter() - customer_start_time, ndigits=2)
        print(f"The Cashier_{cashier_number} "
              f"finished checkout Customer_{customer.customer_id} "
              f"in {cashier_finish_time} secs")
        
        queue.task_done()
    return cashier_take

def generate_customer(customer_id: int) -> Customer:
    all_products = [Product('beef', 1), Product('banana', .4), Product('sausage', .4), Product('diapers', .2)]
    return Customer(customer_id, all_products)

async def customer_generation(queue: Queue, customer_limit: int):
    customer_count = 0
    while customer_count < customer_limit:
        customer = generate_customer(customer_count)
        print(f"Waiting to put Customer_{customer.customer_id} in line.... ")
        await queue.put(customer)
        print(f"Customer_{customer.customer_id} put in line...")
        customer_count += 1
        await asyncio.sleep(.001)

async def main():
    CUSTOMER = 3  # Total number of customers to generate
    QUEUE = 2     # Capacity of the queue
    CASHIER = 2   # Number of cashiers
    customer_queue = Queue(QUEUE)
    customer_start_time = time.perf_counter()
    
    customer_producer = asyncio.create_task(customer_generation(customer_queue, CUSTOMER))
    cashiers = [checkout_customer(customer_queue, i) for i in range(CASHIER)]

    results = await asyncio.gather(customer_producer, *cashiers)
    
    print("-" * 20)
    total_time = 0
    total_customers = 0
    for cashier in results[1:]:
        total_customers += cashier['customer']
        total_time += cashier['time']
        print(f"The Cashier_{cashier['id']} "
              f"take {cashier['customer']} customers "
              f"total {round(cashier['time'], ndigits=2)} secs")

    print(f"\n"
          f"The supermarket process finished "
          f"{total_customers} customers "
          f"in {round(time.perf_counter() - customer_start_time, ndigits=2)} secs")
    
if __name__ == "__main__":
    asyncio.run(main())
