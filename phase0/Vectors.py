class Vector:
    def __init__(self, component):
        self.component = component
        self.dim = len(self.component)
    
    def __add__(self, other):
        if self.dim != other.dim:
            raise ValueError("Vectors must have the same dimension for addition.")
        return Vector([a + b for a,b in zip(self.component, other.component)])
    
    def __sub__(self, other):
        if self.dim != other.dim:
            raise ValueError("Vectors must have the same dimension for subtraction.")
        return Vector([a-b for a,b in zip(self.component, other.component)])
    
    def __mul__(self, scalar):
        return Vector([scalar * a for a in self.component])
    
    def __dot__(self, other):
        if self.dim != other.dim:
            raise ValueError("Vectors must have the same dimension for dot product.")
        return sum(a * b for a,b in zip(self.component, other.component))
    
    def __magnitude__ (self):
        return sum(a**2 for a in self.component) ** 0.5
    
    def __normalize__(self):
        mag = self.__magnitude__()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return Vector([a / mag for a in self.component])
    
    def __cosine_similarity__(self, other):
        if self.dim != other.dim:
            raise ValueError("Vectors must have the same dimension for cosine similarity.")
        dot_product = self.__dot__(other)
        mag_self = self.__magnitude__()
        mag_other = other.__magnitude__()
        if mag_self == 0 or mag_other == 0:
            raise ValueError("Cannot compute cosine similarity with a zero vector.")
        return dot_product / (mag_self * mag_other)
    
    def __str__(self):
        return f"Vector({self.component})"
    

a = Vector([1, 2, 3])
b = Vector([4, 5, 6])

print(a + b)  # Vector([5, 7, 9])
print(a - b)  # Vector([-3, -3, -3])
print(a * 2)  # Vector([2, 4, 6])
print(a.__dot__(b))  # 32
print(a.__magnitude__())  # 3.7416573867739413
print(a.__normalize__())  # Vector([0.2672612419124244, 0.5345224838248488, 0.8017837257372732])
print(a.__cosine_similarity__(b))  # 0.974631846197076
