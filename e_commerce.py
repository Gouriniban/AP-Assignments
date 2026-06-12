from abc import ABC, abstractmethod


# ==============================
# 1. PAYMENT MODULE (OCP, LSP)
# ==============================

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class UPIPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class WalletPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Wallet")


# ==================================
# 2. NOTIFICATION MODULE (ISP, OCP)
# ==================================

class NotificationService(ABC):
    @abstractmethod
    def send_notification(self, message):
        pass


class EmailNotification(NotificationService):
    def send_notification(self, message):
        print(f"Email Sent: {message}")


class SMSNotification(NotificationService):
    def send_notification(self, message):
        print(f"SMS Sent: {message}")


class PushNotification(NotificationService):
    def send_notification(self, message):
        print(f"Push Notification Sent: {message}")


# ==================================
# 3. STORAGE MODULE (DIP, OCP)
# ==================================

class Storage(ABC):
    @abstractmethod
    def save(self, order):
        pass


class DatabaseStorage(Storage):
    def save(self, order):
        print(f"Order {order.order_id} saved in Database")


class FileStorage(Storage):
    def save(self, order):
        print(f"Order {order.order_id} saved in File")


# ==================================
# 4. ORDER MODULE (SRP, LSP)
# ==================================

class Order(ABC):
    def __init__(self, order_id, customer_name, amount):
        self.order_id = order_id
        self.customer_name = customer_name
        self.amount = amount

    @abstractmethod
    def get_total(self):
        pass


class RegularOrder(Order):
    def get_total(self):
        return self.amount


class DiscountedOrder(Order):
    def __init__(self, order_id, customer_name, amount, discount):
        super().__init__(order_id, customer_name, amount)
        self.discount = discount

    def get_total(self):
        return self.amount - self.discount


class PriorityOrder(Order):
    def __init__(self, order_id, customer_name, amount, priority_fee):
        super().__init__(order_id, customer_name, amount)
        self.priority_fee = priority_fee

    def get_total(self):
        return self.amount + self.priority_fee


# ==================================
# 5. ORDER SERVICE (DIP)
# ==================================

class OrderService:
    def __init__(self, payment_method, notification_service, storage):
        self.payment_method = payment_method
        self.notification_service = notification_service
        self.storage = storage

    def place_order(self, order):
        total = order.get_total()

        print("\nProcessing Order...")
        print(f"Customer: {order.customer_name}")
        print(f"Total Amount: ₹{total}")

        # Process Payment
        self.payment_method.pay(total)

        # Save Order
        self.storage.save(order)

        # Send Notification
        self.notification_service.send_notification(
            f"Order {order.order_id} placed successfully."
        )


# ==================================
# MAIN PROGRAM
# ==================================

# Create Order
order1 = DiscountedOrder(
    order_id=101,
    customer_name="Gouriniban",
    amount=5000,
    discount=500
)

# Inject Dependencies
payment = UPIPayment()
notification = EmailNotification()
storage = DatabaseStorage()

# Create Service
service = OrderService(payment, notification, storage)

# Place Order
service.place_order(order1)