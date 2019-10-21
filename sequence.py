# team epsilon
# udit malik and max kirimi

from time import sleep
import tellopy

def handler(event, sender, data, **args):
    drone = sender
    if event is drone.EVENT_FLIGHT_DATA:
        print(data)

# function to move the drone forward by one arbitrary unit
def go_one_unit_forward(drone):
	drone.forward(30)
	sleep(2)
	drone.forward(0)

# function to turn the drone by approximately 90 degrees or a right angle
def turn_clockwise(drone):
	drone.clockwise(88)
	sleep(1.24)
	drone.clockwise(0)

# brings the drone down by one arbitrary unit
def go_one_unit_down(drone):
	drone.down(30)
	sleep(2)
	drone.down(0)

# takes the drone up by one arbitrary unit
def go_one_unit_up(drone):
	drone.up(30)
	sleep(2)
	drone.up(0)

def test():
    drone = tellopy.Tello()
    try:
        drone.subscribe(drone.EVENT_FLIGHT_DATA, handler)

        drone.connect()
        drone.wait_for_connection(60.0)
        drone.takeoff()
        sleep(3)

	drone.up(20)
	sleep(3)
	drone.up(0)

    # drawing the square in the sequence
	for i in range(4):
		go_one_unit_forward(drone)
		turn_clockwise(drone)

    # drawing the circle in the sequence
	drone.clockwise(60)
	drone.forward(30)
	sleep(7)
	drone.clockwise(0)
	drone.forward(0)
	sleep(2)
	
    # drawing the triangle in the sequence
	for i in range(3):
		go_one_unit_forward(drone)
		drone.clockwise(88)
		sleep(1.8)
		drone.clockwise(0)

        drone.down(10)
        sleep(3)

        drone.land()
        sleep(3)
    except Exception as ex:
        print(ex)
    finally:
        drone.quit()

if __name__ == '__main__':
    test()
