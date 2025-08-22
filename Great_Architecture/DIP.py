"""

Dependency Inversion Principal (DIP)

It states that high-level models should not depend on low-level modules.

"""

"""
This class violates the Dependency Inversion Principal (DIP).

The Computer is high-level class and, it directly depends on Keyboard class 
it can’t easily change the input devices.

This breaks the DIP because high-level class never should depends on low-level class.
"""

class Keyboard:
    def keboard_message(self):
        return "Keyboard - User typed: Hello"

class Mic:
    def mic_message(self):
        return "Microphone - User sayed: Hello"

class Computer:
    def __init__(self):
        self.keyboard = Keyboard()
        self.mic = Mic()

    def send_message(self, method):
        if method == "keyboard":
            self.keyboard.keboard_message()
        elif method == "mic":
            self.mic.mic_message()

# ===============================================================================#

"""
Refactored Solution:

- The Machine class depends only on the abstraction IMessageDevice, not on concrete implementations.
- Any message device (e.g., KeyboardService, MicService) can be injected into the Machine class without changing its code.
- This design adheres to the Dependency Inversion Principal (DIP): High-level modules (like Machine) do not depend on low-level modules (like KeyboardService or MicService);
  instead, both depend on abstractions (IMessageDevice).
- This promotes flexibility, extensibility, and maintainability, allowing new input devices to be added without modifying existing high-level logic.

"""

from abc import ABC, abstractmethod

class IMessageDevice(ABC):
    @abstractmethod
    def send(self, message):
        pass

class KeyboardService(IMessageDevice):
    def send(self, message):
        return f"Keyboard - User typed: {message}"

class MicService(IMessageDevice):
    def send(self, message):
        return f"Mic - User sayed: {message}"

class Machine:
    def __init__(self, message_device : IMessageDevice):
        self.message_device = message_device

    def send_message(self, message):
        return self.message_device.send(message)

keyboard_machine = Machine(KeyboardService())
print(keyboard_machine.send_message("Hello Keyboard"))

mic_machine = Machine(MicService())
print(mic_machine.send_message("Hello Mic"))
