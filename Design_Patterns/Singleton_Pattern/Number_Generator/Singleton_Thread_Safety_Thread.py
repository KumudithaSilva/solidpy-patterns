import threading


class Number_Generator:
    _instance = None
    _init_number = 0
    _lock = threading.Lock()

    # override the new method which is control how object are created
    def __new__(cls):

        with cls._lock:
            if not cls._instance:
                # create a new singleton instance using the parent class's __new__
                cls._instance = super(Number_Generator, cls).__new__(cls)
                # return the singleton instance class or newly created one
        return cls._instance

    def generate_next_number(self):
        with self._lock:
            self._init_number += 1

    def get_next_number(self):
        with self._lock:
            return self._init_number


def singleton_thread_safe():
    generator = Number_Generator()
    generator.generate_next_number()
    print(f"Generated Number: {generator.get_next_number()}")


if __name__ == "__main__":
    # Create a list to store threads
    threads = []

    for _ in range(10):
        t = threading.Thread(target=singleton_thread_safe)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
