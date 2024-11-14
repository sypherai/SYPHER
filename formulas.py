import math

# Basic Mathematical Constants
PI = math.pi
E = math.e

# Logarithmic Functions
def change_of_base_log(value, base, new_base):
    """Change the base of a logarithm."""
    return math.log(value, new_base) / math.log(base, new_base)

def natural_log(value):
    """Calculate the natural logarithm (base e)."""
    if value <= 0:
        raise ValueError("Value must be greater than 0.")
    return math.log(value)

# Exponential Functions
def exponential(value):
    """Calculate e raised to the power of the value."""
    return math.exp(value)

def power(base, exponent):
    """Calculate base raised to the power of exponent."""
    return math.pow(base, exponent)

# Trigonometric Functions
def sine(angle):
    """Calculate sine of an angle in radians."""
    return math.sin(angle)

def cosine(angle):
    """Calculate cosine of an angle in radians."""
    return math.cos(angle)

def tangent(angle):
    """Calculate tangent of an angle in radians."""
    return math.tan(angle)

def arc_sine(value):
    """Calculate arc sine (inverse sine) in radians."""
    if value < -1 or value > 1:
        raise ValueError("Value must be in the range [-1, 1].")
    return math.asin(value)

def arc_cosine(value):
    """Calculate arc cosine (inverse cosine) in radians."""
    if value < -1 or value > 1:
        raise ValueError("Value must be in the range [-1, 1].")
    return math.acos(value)

def arc_tangent(value):
    """Calculate arc tangent (inverse tangent) in radians."""
    return math.atan(value)

# Geometry Formulas
def circle_area(radius):
    """Calculate the area of a circle."""
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return PI * radius ** 2

def sphere_volume(radius):
    """Calculate the volume of a sphere."""
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return (4 / 3) * PI * radius ** 3

def triangle_area(base, height):
    """Calculate the area of a triangle."""
    if base < 0 or height < 0:
        raise ValueError("Base and height cannot be negative.")
    return 0.5 * base * height

# Algebraic Functions
def quadratic_roots(a, b, c):
    """Calculate the roots of a quadratic equation ax^2 + bx + c = 0."""
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        raise ValueError("No real roots exist for the given coefficients.")
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    return root1, root2
