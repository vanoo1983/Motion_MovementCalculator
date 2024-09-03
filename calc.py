import matplotlib.pyplot as plt

# Parameters

Distance = 450
Velocity = 700
Acceleration = 3000
Deceleration = 3000


class MovementParameter:
    def __init__(self, acceleration_distance,
                 acceleration_time,
                 deceleration_distance,
                 deceleration_time,
                 full_speed_time,
                 max_speed,
                 total_time):
        self.acceleration_distance = acceleration_distance
        self.acceleration_time = acceleration_time
        self.deceleration_distance = deceleration_distance
        self.deceleration_time = deceleration_time
        self.full_speed_time = full_speed_time
        self.max_speed = max_speed
        self.total_time = total_time


# calculation of movement time
def calc_time(distance, velocity, acceleration, deceleration):
    acceleration_distance = velocity**2 / (2 * acceleration)
    deceleration_distance = velocity**2 / (2 * deceleration)
    acceleration_time = 0.0
    velocity_time = 0.0
    deceleration_time = 0.0
    if (acceleration_distance + deceleration_distance) <= distance:
        acceleration_time = velocity / acceleration
        deceleration_time = velocity / deceleration
        velocity_time = (distance - acceleration_distance - deceleration_distance) / velocity
        max_reached_speed = velocity
    else:
        deceleration_distance = acceleration * distance / (acceleration + deceleration)
        acceleration_distance = distance - deceleration_distance
        max_reached_speed = (2 * acceleration * acceleration_distance)**0.5
        acceleration_time = max_reached_speed / acceleration
        deceleration_time = max_reached_speed / deceleration
    total_time = acceleration_time + velocity_time + deceleration_time

    return MovementParameter(acceleration_distance, acceleration_time,
                             deceleration_distance, deceleration_time,
                             velocity_time, max_reached_speed,
                             total_time)


movement = calc_time(Distance, Velocity, Acceleration, Deceleration)

print(f'Movement time: {movement.total_time}')



## plot graph with velocity over time
# x = [0, movement.acceleration_time, movement.acceleration_time + movement.full_speed_time, movement.total_time]
# y = [0, movement.max_speed, movement.max_speed, 0]
# plt.plot(x, y)
# plt.grid()
# plt.show()

