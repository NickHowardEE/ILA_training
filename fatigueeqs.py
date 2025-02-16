import math
# Define a class for an SN curve
class SN_curve:
    def __init__(self, m1, loga1, m2, loga2, k, tref):
        self.m1 = m1
        self.loga1 = loga1
        self.m2 = m2
        self.loga2 = loga2
        self.k = k
        self.tref = tref
    # Calculates the point of inflection of the two lines.
    def inflection_point(self):
        exponent = (self.loga1 - self.loga2) / (self.m1 - self.m2)
        return 10**exponent

# Defien a class to hold a fatigue cycle
class fatigue_cycle:
    def __init__(self, Srange, n):
        self.Srange = Srange
        self.n = n 
    # Calculate the damage for this cycle
    def calculate_damage(self, sn_curve, t):
        if self.Srange < sn_curve.inflection_point():
            logN = sn_curve.loga2 - sn_curve.m2*math.log10(self.Srange*(t/sn_curve.tref)**sn_curve.k)
            N = 10**logN
            damage = self.n/N
            return damage
        else:
            logN = sn_curve.loga1 - sn_curve.m1*math.log10(self.Srange*(t/sn_curve.tref)**sn_curve.k)
            N = 10**logN
            damage = self.n/N
            return damage
        
# Calculate the damage equivalent stress for a given damage.
def damage_equivalent_stress(m, cycles, n_eq):
    total = 0
    for c in cycles:
        total += (c.n*c.Srange**m)
    sigma_eq = (total/n_eq)**(1/m)
    return sigma_eq


