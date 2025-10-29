from abc import ABC, abstractmethod
from typing import List
import xml.etree.ElementTree as ET
import json

class Contact:
    def __init__(self, full_name, email, phone_number, is_friend):
        self.full_name = full_name
        self.email = email
        self.phone = phone_number
        self.is_friend = is_friend

    def __str__(self):
        return f"{self.full_name} ({self.email}) - {self.phone} {'(Friend)' if self.is_friend else ''}"


# Base class for reading file data
class FileReader(ABC):
    def __init__(self, file_name):
        self.file_name = file_name

    @abstractmethod
    def read(self) -> str:
        pass


# Add specific file readers
class XMLReader(FileReader):
    def read(self) -> str:
        with open(self.file_name) as f:
            return f.read()


class JSONReader(FileReader):
    def read(self) -> str:
        with open(self.file_name) as f:
            return f.read()



if __name__ == '__main__':
    print(JSONReader('data/contacts.json').read())