import datetime
import threading


class FileAuditManager:
    """This is a thread-safe Singleton class that write to common file"""
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, filename = 'audit.log'):
        """This will control the creation of the instance"""
        with  cls._lock:
            if cls._instance is None:
                cls._instance = super(FileAuditManager, cls).__new__(cls)
                cls._instance._filename = filename
                with open(cls._instance._filename, 'a') as file:
                    file.write(f"Log Started {datetime.datetime.now()}\n")
        return cls._instance

    def log_message(self, message):
        """This method writes a log entry to the files."""
        with self._lock:
            time_stamp = datetime.datetime.now().strftime('%Y-%m-%d, %H:%M:%S')
            with open(self._filename, 'a') as file:
                file.write(f"{time_stamp}: {message}\n")


def file_audit_log():
    log = FileAuditManager()
    log.log_message("test logs")

if __name__ == "__main__":
    threads = []

    for _ in range(10):
        thread = threading.Thread(target=file_audit_log)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()



