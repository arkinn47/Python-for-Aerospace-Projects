
# Pre-defined variable values
fuel_capacity = 1000  # gallons
fuel_consumption_rate = 50  # gallons per hour
true_air_speed = 150  # knots
payload = 5000  # pounds
fuel_weight = 6000  # pounds
moment_list = [10000, 2500]  # pound-feet
total_weight = 1500  # pounds
cl = 1.5  # lift coefficient
rho = 1.225  # air density in kg/m^3
v = 100  # velocity in m/s
s = 20  # wing area in m^2
cd = 0.02  # drag coefficient
mass = 5000  # mass in kg
g = 9.81  # acceleration due to gravity in m/s^2
thrust = 6000  # thrust in N
drag = 5000  # drag in N
velocity = 50  # initial velocity in m/s
acceleration = 2  # acceleration in m/s^2
time = 10  # time in seconds


def calculate_range(fuel_capacity, fuel_consumption_rate, true_air_speed):
    return true_air_speed*fuel_capacity/fuel_consumption_rate

def calculate_endurance(fuel_capacity, fuel_consumption_rate):
    return fuel_capacity/fuel_consumption_rate

def calculate_total_weight(payload, fuel_weight):
    return payload + fuel_weight

def calculate_cg_position(moment_list, total_weight):
    return sum(moment_list)/total_weight

def calculate_moment(weight, arm):
    return weight*arm

def calculate_lift(cl, rho, v, s):
    return 0.5 * cl * rho * v**2 * s

def calculate_drag(cd, rho, v, s):
    return 0.5 * cd * rho * v**2 * s

def calculate_weight(mass, g):
    return mass*g

def calculate_acceleration(thrust, drag, weight, mass):
    return (thrust - drag - weight)/mass

def calculate_velocity(velocity, acceleration, time):
    return velocity + acceleration*time

def calculate_distance(velocity, time):
    return velocity*time

def run_performance_calculator():
    return 

def save_info_to_file(range_, endurance, total_weight, cg_position, lift, drag, weight, acceleration, velocity, distance, file):
    input_list = [range_, endurance, total_weight, cg_position, lift, drag, weight, acceleration, velocity, distance, file]
    open_file = open('aircraft_performance_analysis.txt', w)
    for i in input_list:
        open_file.write(i)

def pretty_print(range_, endurance, total_weight, cg_position, lift, drag, weight, acceleration, velocity, distance):
    print("Performance Calculations:")
    print("Range: {} miles".format(range_))
    print("Endurance: {} hours".format(endurance))
    print("Total Weight: {} pounds".format(total_weight))
    print("Center of Gravity Position: {} feet".format(cg_position))
    print("Lift: {} Newtons".format(lift))
    print("Drag: {} Newtons".format(drag))
    print("Weight: {} Newtons".format(weight))
    print("Acceleration: {} m/s^2".format(acceleration))
    print("Velocity: {} m/s".format(velocity))
    print("Distance: {} meters".format(distance))