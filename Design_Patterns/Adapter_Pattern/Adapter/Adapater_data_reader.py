from abc import ABC, abstractmethod
from typing import List
import xml.etree.ElementTree as ET
import json, csv

from numpy.lib.recfunctions import join_by


class Contact:
    """Represents a single contact entry."""

    def __init__(self, full_name: str, email: str, phone_number: str, is_friend: bool):
        self.full_name = full_name
        self.email = email
        self.phone = phone_number
        self.is_friend = is_friend

    def __str__(self):
        friend_tag = " (Friend)" if self.is_friend else ""
        return f"{self.full_name} ({self.email}) - {self.phone}{friend_tag}"


# --------------------------
# Abstract File Reader
# --------------------------
# Defines an abstract base for all file readers.
class FileReader(ABC):
    def __init__(self, file_name: str):
        self.file_name = file_name

    @abstractmethod
    def read(self) -> str:
        """Read and return the raw content of the file."""
        pass


# --------------------------
# Concrete File Readers
# --------------------------
# Implementations of FileReader for specific formats.
class XMLReader(FileReader):
    """Reads data from an XML file."""

    def read(self) -> str:
        with open(self.file_name, encoding="utf-8") as f:
            return f.read()


class JSONReader(FileReader):
    """Reads data from a JSON file."""

    def read(self) -> str:
        with open(self.file_name, encoding="utf-8") as f:
            return f.read()

class CSVReader(FileReader):
    """Reads data from a CSV file."""

    def read(self) -> str:
        with open(self.file_name, encoding="utf-8") as f:
            return f.read()

# --------------------------
# Abstract Contracts Adapter
# --------------------------
# Base adapter class for transforming file data into Contact objects.
class ContractsAdapter(ABC):
    def __init__(self, data_source: FileReader):
        self.data_source = data_source

    @abstractmethod
    def get_contracts(self) -> List[Contact]:
        """Convert the data source content into a list of Contact objects."""
        pass


# --------------------------
# Concrete Contracts Adapters
# --------------------------
# These adapters parse raw file data into structured Contact objects.
class XMLContractsAdapter(ContractsAdapter):
    """Parses XML data and converts it into Contact objects."""

    def get_contracts(self) -> List[Contact]:
        root = ET.fromstring(self.data_source.read())
        contacts = []

        for elem in root.iter("contact"):
            full_name = elem.find("full_name").text
            email = elem.find("email").text
            phone_number = elem.find("phone_number").text
            is_friend = elem.find("is_friend").text.lower() == "true"
            contact = Contact(full_name, email, phone_number, is_friend)
            contacts.append(contact)

        return contacts


class JSONContractsAdapter(ContractsAdapter):
    """Parses JSON data and converts it into Contact objects."""

    def get_contracts(self) -> List[Contact]:
        data_dict = json.loads(self.data_source.read())
        contacts = []

        for contact_data in data_dict["contacts"]:
            contact = Contact(
                contact_data["full_name"],
                contact_data["email"],
                contact_data["phone_number"],
                contact_data["is_friend"],
            )
            contacts.append(contact)

        return contacts

class CSVContractsAdapater(ContractsAdapter):

    def get_contracts(self) -> List[Contact]:
        contacts = []

        csv_content = csv.reader(self.data_source.read().splitlines())
        next(csv_content, None)

        for lines in csv_content:
            full_name = lines[0]
            email = lines[1]
            phone_number = lines[2]
            is_friend = lines[3].lower() == "true"

            contact = Contact(full_name, email, phone_number, is_friend)
            contacts.append(contact)

        return contacts


# --------------------------
# Utility Function
# --------------------------
def print_contact_data(contacts_source: ContractsAdapter):
    """Prints formatted contact information from a given data source."""
    for contact in contacts_source.get_contracts():
        print(contact)


# --------------------------
# Entry Point
# --------------------------
if __name__ == "__main__":
    print("==JSON==")
    json_reader = JSONReader("data/contacts.json")
    json_adapter = JSONContractsAdapter(json_reader)
    print_contact_data(json_adapter)

    print("\n==CSV==")
    csv_adapter = CSVReader("data/contacts.csv")
    csv_adapter = CSVContractsAdapater(csv_adapter)
    print_contact_data(csv_adapter)
