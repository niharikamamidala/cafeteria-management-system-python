from queue import Queue
from collections import deque

class CafeteriaSystem:
    def __init__(self):
        self.normal_orders = Queue()
        self.priority_orders = deque()
        self.completed_orders = []
        self.order_id = 1

    def place_order(self, customer, item, priority=False):
        order = {
            "id": self.order_id,
            "customer": customer,
            "item": item
        }
        self.order_id += 1

        if priority:
            self.priority_orders.appendleft(order)
            print("⭐ Priority order placed!")
        else:
            self.normal_orders.put(order)
            print("📦 Normal order placed!")

    def process_order(self):
        if self.priority_orders:
            order = self.priority_orders.popleft()
        elif not self.normal_orders.empty():
            order = self.normal_orders.get()
        else:
            print("No orders to process")
            return

        self.completed_orders.append(order)
        print(f"✅ Order served: {order['customer']} - {order['item']}")

    def view_completed_orders(self):
        print("\n📜 Completed Orders:")
        if not self.completed_orders:
            print("No completed orders yet")
        for order in self.completed_orders:
            print(f"{order['id']} - {order['customer']} ordered {order['item']}")


def main():
    system = CafeteriaSystem()

    while True:
        print("\n--- CAFETERIA ORDER SYSTEM ---")
        print("1. Place Order")
        print("2. Process Order")
        print("3. View Completed Orders")
        print("4. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            name = input("Customer Name: ")
            item = input("Food Item: ")
            priority = input("Priority order? (yes/no): ").lower() == "yes"
            system.place_order(name, item, priority)

        elif choice == 2:
            system.process_order()

        elif choice == 3:
            system.view_completed_orders()

        elif choice == 4:
            print("Thank you for using Cafeteria System!")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
