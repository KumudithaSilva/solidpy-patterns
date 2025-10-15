"""

Open/Close Principal(OCP)

A class should have one, and only one, reason to change.
Each class should focus on a single task or functionality.

"""

"""
This class violates the Open/Closed Principle.

The NotificationSender class requires modification whenever a new 
notification type (e.g., WhatsApp, Slack) is introduced.

This breaks the OCP, as the class is not closed for modification.
"""


class NotificationSender:
    def send(self, notification_type, message):
        if notification_type == "email":
            print(f"Sending email with message: {message}")
        elif notification_type == "sms":
            print(f"Sending SMS with message: {message}")
        elif notification_type == "push":
            print(f"Sending push notification with message: {message}")


# Usage
sender = NotificationSender()
sender.send("email", "Your order has been shipped!")
sender.send("sms", "Your OTP is 123456")


# ===============================================================================#

"""
Refactored Solution:

- Introduces an abstract base class (Notification) with an abstract `send()` method.
- Each notification type implements its own `send()` logic.
- The NotificationSender class works with any object implementing the Notification interface.
- This design adheres to the Open/Closed Principle: this enables to add new notification types without modifying existing code.
"""

from abc import ABC, abstractmethod


# Abstract base class for all notification types
class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass


# Email Notification
class EmailNotification(Notification):
    def send(self, message):
        print(f"Sending email with message: {message}")


# SMS Notification
class SMSNotification(Notification):
    def send(self, message):
        print(f"Sending SMS with message: {message}")


# Push Notification
class PushNotification(Notification):
    def send(self, message):
        print(f"Sending push notification with message: {message}")


# New Notification Type: WhatsApp
class WhatsAppNotification(Notification):
    def send(self, message):
        print(f"Sending WhatsApp message: {message}")


# Sender class that uses polymorphism
class NotificationSender:
    def send(self, notification: Notification, message: str):
        notification.send(message)


# Usage
notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification(),
    WhatsAppNotification(),
]

sender = NotificationSender()

for notification in notifications:
    sender.send(notification, "System update available at 9 PM.")
