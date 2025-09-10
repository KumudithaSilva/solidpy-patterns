"""
Thread Safety in Singleton

In a multithreaded environment, if multiple threads try to create a Singleton instance at the same time,
it can lead to race conditions, resulting in multiple instances being created.
"""
import threading

class ThreadingSafeSingleton:
    # Class-level variable to store the single instance of the class
    _instance = None
    # Class-level lock to ensure thread safety during instance creation
    _lock = threading.Lock()

    # Override the __new__ method to control instance creation
    def __new__(cls, *args, **kwargs):
        # Acquire the lock to enter the critical section
        with cls._lock:
            # Check if the singleton instance has already been created
            if cls._instance is None:
                # Create the single instance of the class
                cls._instance = super().__new__(cls)
        # Return the single instance (existing or newly created)
        return cls._instance

# Create an instance of the singleton class
s1 = ThreadingSafeSingleton()
s2 = ThreadingSafeSingleton()

print(s1 is s2)
