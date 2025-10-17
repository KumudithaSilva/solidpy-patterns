from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class User:
    first_name: str
    last_name: str
    age: Optional[int] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None
    email: Optional[str] = None

    def get_full_info(self) -> dict:
        """Return all fields of the user as a dictionary."""
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "phone_number": self.phone_number,
            "address": self.address,
            "email": self.email,
        }


class UserBuilder(ABC):
    @abstractmethod
    def add_first_name(self, first_name):
        pass

    @abstractmethod
    def add_last_name(self, last_name):
        pass

    @abstractmethod
    def add_age(self, age):
        pass

    @abstractmethod
    def add_phone_number(self, phone_number):
        pass

    @abstractmethod
    def add_address(self, address):
        pass

    @abstractmethod
    def add_email(self, email):
        pass

    @abstractmethod
    def build(self) -> User:
        pass


class CustomUserBuilder(UserBuilder):
    def __init__(self):
        self.user = {}

    def add_first_name(self, first_name):
        self.user["first_name"] = first_name
        return self

    def add_last_name(self, last_name):
        self.user["last_name"] = last_name
        return self

    def add_age(self, age):
        self.user["age"] = age
        return self

    def add_phone_number(self, phone_number):
        self.user["phone_number"] = phone_number
        return self

    def add_address(self, address):
        self.user["address"] = address
        return self

    def add_email(self, email):
        self.user["email"] = email
        return self

    def build(self) -> User:
        if "first_name" not in self.user or "last_name" not in self.user:
            raise ValueError("Missing required fields: 'first_name' and 'last_name'")
        return User(**self.user)


class UserDirector:
    def __init__(self, builder):
        self.builder = builder

    def build_user(self, user):
        return (
            self.builder.add_first_name(user["first_name"])
            .add_last_name(user["last_name"])
            .add_email(user["email"])
            .build()
        )


builder = CustomUserBuilder()
user = (
    builder.add_first_name("Ann")
    .add_last_name("Bee")
    .add_email("AnnBee@gmail.com")
    .build()
)

# Call the getter
full_info = user.get_full_info()
print(full_info)
