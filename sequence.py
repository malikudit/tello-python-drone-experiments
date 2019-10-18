from time import sleep
import tellopy

def handler(event, sender, data, **args):
    drone = sender
    if event is drone.EVENT_FLIGHT_DATA:
        print(data)

def go_one_unit_forward(drone):
	drone.forward(30)
	sleep(2)
	drone.forward(0)

def turn_clockwise(drone):
	drone.clockwise(88)
	sleep(1.24)
	drone.clockwise(0)

def go_one_unit_down(drone):
	drone.down(30)
	sleep(2)
	drone.down(0)

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

	# draws the square part of the sequence
	for i in range(4):
		go_one_unit_forward(drone)
		turn_clockwise(drone)

    # draws the circle part of the sequence
    drone.forward(25)
    drone.clockwise(50)
    sleep(4)
    drone.forward(0)
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

