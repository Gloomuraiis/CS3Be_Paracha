class Machine:
    def __init__(self, serial_number):
        self.serial_number = serial_number

    def show_info(self):
        print("Machine serial number:", self.serial_number)


class ControlBoard:
    def activate(self):
        print("Control board activated.")


class DeliveryRobot(Machine):
    def __init__(self, serial_number, cargo_capacity):
        super().__init__(serial_number)
        self.cargo_capacity = cargo_capacity
        self.control_board = ControlBoard()

    def use_control_board(self):
        self.control_board.activate()


class RoboticsRoom:
    def __init__(self, robot):
        self.robot = robot

    def show_robot(self):
        print("Robot assigned to the robotics room:")
        self.robot.show_info()


class DiagnosticTool:
    def scan(self, robot):
        print("Scanning robot:", robot.serial_number)
        print("Scan complete.")


class Technician:
    def inspect(self, robot, tool):
        print("Technician is inspecting the robot.")
        tool.scan(robot)


robot = DeliveryRobot("DR-1218", 20)

robot.show_info()
print("Cargo capacity:", robot.cargo_capacity)

robot.use_control_board()

room = RoboticsRoom(robot)
room.show_robot()

del room
print("The robot still works after the room is removed.")
robot.show_info()

tool = DiagnosticTool()
technician = Technician()

technician.inspect(robot, tool)