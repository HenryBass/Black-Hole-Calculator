import math

G = 6.674e-11
c = 299792458
sun = 1.9891 * 10**30
pi = 3.14159265358979323846
lightyear = c * 31536000
plankconstant = 6.62607015*10**-34
reducedplankconstant = plankconstant / (pi*2)
boltzmannconstant = 1.380649 * 10**-23

class blackhole:
    def __init__(self, mass):
        self.mass = mass
        self.event_horizon_radius = mass*(2*G)/(c**2)
        self.gravforce = (G * self.mass) / self.event_horizon_radius ** 2
        self.temperature = reducedplankconstant * c**3 / (8 * pi * G * self.mass * boltzmannconstant)
        self.secondlength = math.sqrt(1 - 2 * ((self.mass * G) / ((self.event_horizon_radius * 2.6) * (c ** 2))))
        self.energy = self.mass * (c ** 2)
        self.lifetime = (self.mass ** 3) * (5120 * pi * (G**2))/(1.8083*reducedplankconstant*(c**4))

    def returnvalues(self):
        print("Mass (kg): " + str(self.mass))
        print("Solar Masses: " + str(self.mass / sun))
        print("Schwarzschild Radius (m): " + str(self.event_horizon_radius))
        print("Schwarzschild Radius (km): " + str(self.event_horizon_radius / 1000))
        print("Schwarzschild Radius (Light Year): " + str(self.event_horizon_radius / lightyear))
        print("Newtonian Gravitational Force (At Event Horizon) (M/S^2): " + str(self.gravforce))
        print("Temperature (k): " + str(self.temperature))
        print("Energy (j): " + str(self.energy))
        print("Length of second at 2x Event Horizon radius to an inertial observer: " + str(self.secondlength))
        print("Time to decay from Hawking Radiation: " + str(self.lifetime))

blackhole = blackhole(sun * float(input("Solar Masses: ")))
blackhole.returnvalues()