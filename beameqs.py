import math

# Material class to store material properties.
class Material:
    def __init__(self, name, density, E):
        self.name = "structural steel"
        self.density = density
        self.E = E

# Beam class to store beam properties.
class Beam:
    def __init__(self, D_outer, t, L, material):
        # Input parameters.
        self.D_outer = D_outer
        self. thickness = t
        self.L = L
        self.material = material
        # Derived parameters.
        self.D_inner = D_outer - 2*t # Inner diameter of the beam.
        self.I = self.moment_of_inertia()
        self.mass = self.mass_of_chs()
        #self.natural_frequency = natural_frequency(E, self.I, self.mass, L)

    def moment_of_inertia(self):
        return (math.pi / 64) * (self.D_outer**4 - self.D_inner**4)
    
    def mass_of_chs(self):
        volume = math.pi * (self.D_outer**2 - self.D_inner**2) / 4 * self.L
        return volume * self.material.density

# Equation to calculate deflection of cantilever beam with a point load at the end.
# x: distance from the fixed end of the beam.
# P: point load at the end of the beam.
# beam: beam object containing beam properties.
def deflection(x, P, beam):
    return (P * x**2) / (6 * beam.material.E * beam.I) * (3 * beam.L - x)



def natural_frequency(E, I, m, L):
    mul = m/L # mass per unit length
    return (1.875**2 / (2 * math.pi)) * ((E * I) / (mul * L**4))**0.5

def bending_stress(M, D, I):
    y = D / 2
    return (M * y / I)

def fatigue_damage(DEM, SN_curve):
    return 1

class SN_curve:
    def __init__(self, log_a, m, k):
        self.log_a = log_a
        self.m = m
        self.k = k