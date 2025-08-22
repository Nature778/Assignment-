    #ASSIGNMENT 6(Select at least six formulas in your field. Implement them using classes, objects and methods. Also apply OOP concepts such as polymorphism and inheritance. Use try/catch to handle potential errors.)
import math

# Base class for formulas
class Formula:
    def calculate(self, *args):
        """Calculates the formula result. To be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement the calculate method.")

    def get_name(self):
        """Returns the name of the formula."""
        raise NotImplementedError("Subclasses must implement the get_name method.")

# Concrete formula implementations
class AreaOfCircle(Formula):
    def get_name(self):
        return "Area of Circle"

    def calculate(self, radius):
        try:
            if not isinstance(radius, (int, float)) or radius < 0:
                raise ValueError("Radius must be a non-negative number.")
            return math.pi * (radius ** 2)
        except ValueError as e:
            print(f"Error in {self.get_name()}: {e}")
            return None

class PythagoreanTheorem(Formula):
    def get_name(self):
        return "Pythagorean Theorem"

    def calculate(self, a, b):
        try:
            if not all(isinstance(x, (int, float)) and x >= 0 for x in [a, b]):
                raise ValueError("Sides 'a' and 'b' must be non-negative numbers.")
            return math.sqrt(a*2 + b*2)
        except ValueError as e:
            print(f"Error in {self.get_name()}: {e}")
            return None

class SimpleInterest(Formula):
    def get_name(self):
        return "Simple Interest"

    def calculate(self, principal, rate, time):
        try:
            if not all(isinstance(x, (int, float)) and x >= 0 for x in [principal, rate, time]):
                raise ValueError("Principal, rate, and time must be non-negative numbers.")
            return (principal * rate * time) / 100
        except ValueError as e:
            print(f"Error in {self.get_name()}: {e}")
            return None

class CelsiusToFahrenheit(Formula):
    def get_name(self):
        return "Celsius to Fahrenheit Conversion"

    def calculate(self, celsius):
        try:
            if not isinstance(celsius, (int, float)):
                raise ValueError("Celsius temperature must be a number.")
            return (celsius * 9/5) + 32
        except ValueError as e:
            print(f"Error in {self.get_name()}: {e}")
            return None

class KineticEnergy(Formula):
    def get_name(self):
        return "Kinetic Energy"

    def calculate(self, mass, velocity):
        try:
            if not all(isinstance(x, (int, float)) and x >= 0 for x in [mass, velocity]):
                raise ValueError("Mass and velocity must be non-negative numbers.")
            return 0.5 * mass * (velocity ** 2)
        except ValueError as e:
            print(f"Error in {self.get_name()}: {e}")
            return None

class QuadraticFormula(Formula):
    def get_name(self):
        return "Quadratic Formula"

    def calculate(self, a, b, c):
        try:
            if not all(isinstance(x, (int, float)) for x in [a, b, c]):
                raise ValueError("Coefficients a, b, and c must be numbers.")
            discriminant = (b**2) - 4 * a * c
            if discriminant < 0:
                raise ValueError("Discriminant is negative; no real roots.")
            root1 = (-b + math.sqrt(discriminant)) / (2 * a)
            root2 = (-b - math.sqrt(discriminant)) / (2 * a)
            return root1, root2
        except ValueError as e:
            print(f"Error in {self.get_name()}: {e}")
            return None

# Polymorphism in action
formulas = [
    AreaOfCircle(),
    PythagoreanTheorem(),
    SimpleInterest(),
    CelsiusToFahrenheit(),
    KineticEnergy(),
    QuadraticFormula()
]

print("--- Formula Calculations ---")
for formula in formulas:
    print(f"\nCalculating {formula.get_name()}:")
    if isinstance(formula, AreaOfCircle):
        print(f"Result for radius 5: {formula.calculate(5)}")
        print(f"Result for invalid radius: {formula.calculate(-2)}")
    elif isinstance(formula, PythagoreanTheorem):
        print(f"Result for sides 3, 4: {formula.calculate(3, 4)}")
        print(f"Result for invalid sides: {formula.calculate('a', 4)}")
    elif isinstance(formula, SimpleInterest):
        print(f"Result for P=1000, R=5, T=2: {formula.calculate(1000, 5, 2)}")
    elif isinstance(formula, CelsiusToFahrenheit):
        print(f"Result for 25 Celsius: {formula.calculate(25)}")
    elif isinstance(formula, KineticEnergy):
        print(f"Result for Mass=10, Velocity=5: {formula.calculate(10, 5)}")
    elif isinstance(formula, QuadraticFormula):
        print(f"Result for x^2 - 5x + 6 = 0: {formula.calculate(1, -5, 6)}")
        print(f"Result for x^2 + x + 1 = 0: {formula.calculate(1, 1, 1)}")
