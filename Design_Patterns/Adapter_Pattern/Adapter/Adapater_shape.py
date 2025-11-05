from abc import ABC, abstractmethod


class Rectangle:

    def __init__(self, left_upper: int, right_upper: int,
                 left_lower: int, right_lower:int):
        self.left_upper = left_upper
        self.right_upper = right_upper
        self.left_lower = left_lower
        self.right_lower = right_lower

    def __str__(self):
        return(f"Drawing rectangle: LU=({self.left_upper},{self.right_upper}),"
          f"LL=({self.left_lower},{self.right_lower})")


# --------------------------
# Abstract Contracts Adapter
# --------------------------
# Base adapter class for converting constructor data.
class RectangleContractsAdapter(ABC):
    def __init__(self, rectangle):
        self.rectangle = rectangle

    @abstractmethod
    def get_contracts(self) -> Rectangle:
        pass


# --------------------------
# Legacy & Normal Rectangle Formats
# --------------------------
class LegacyRectangle:
    def __init__(self, x, y1, x2, y2):
        self.x = x
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class NormalRectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h


# --------------------------
# Concrete Contracts Adapters
# --------------------------
class LegacyRectangleAdapter(RectangleContractsAdapter):
    # Convert (x1, y1, x2, y2) → (left_upper, right_upper, left_lower, right_lower)
    def get_contracts(self):
        left_upper = self.rectangle.x
        right_upper = self.rectangle.y1
        left_lower =self.rectangle.x2
        right_lower =self.rectangle.y2
        rectangle = Rectangle(left_upper, right_upper, left_lower, right_lower)
        return rectangle


class NormalRectangleAdapter(RectangleContractsAdapter):
    # Convert (x, y, w, h) → (left_upper, right_upper, left_lower, right_lower)
    def get_contracts(self):
        left_upper = self.rectangle.x
        right_upper = self.rectangle.y
        left_lower = self.rectangle.x + self.rectangle.w
        right_lower = self.rectangle.y + self.rectangle.h
        rectangle = Rectangle(left_upper, right_upper, left_lower, right_lower)
        return rectangle


# --------------------------
# Entry Point
# --------------------------
if __name__ == "__main__":
    print("== Legacy Rectangle ==")
    legacy_rectangle = LegacyRectangle(10, 20, 110, 70)
    legacy_adapter = LegacyRectangleAdapter(legacy_rectangle)
    print(legacy_adapter.get_contracts())

    print("\n== Normal Rectangle ==")
    normal_rectangle = NormalRectangle(10, 20, 100, 50)
    normal_adapter = NormalRectangleAdapter(normal_rectangle)
    print(normal_adapter.get_contracts())