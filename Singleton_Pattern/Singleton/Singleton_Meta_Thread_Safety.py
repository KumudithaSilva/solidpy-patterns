import threading

# Define Singleton Meta Class
class ThreadingSafeSingletonMeta(type):
    _instance = {}
    _lock = threading.Lock()

    # Override the __call__ methods to control clas creation
    def __call__(cls, *args, **kwargs):
        # Acquire the lock
        with cls._lock:
            # Create the instance if it not in the instance dictionary
            if  cls not in cls._instance:
                cls._instance[cls] = super().__call__(*args, *kwargs)
            # Return the existing or newly created instance of the class
            return cls._instance[cls]

class Singleton(metaclass=ThreadingSafeSingletonMeta):
    def some_implementation(self):
        pass

# Get the memory location of the singleton object
def get_singleton_instance():
    s = Singleton()
    print(s)

# Create a list to store threads
threads = []

# Create thread objects
for _ in range(10):
    t = threading.Thread(target=get_singleton_instance())
    threads.append(t)

# Start each thread
for t in threads:
    t.start()

# Wait for each thread to finish
for t in threads:
    t.join()