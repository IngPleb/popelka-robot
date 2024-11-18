import math

from model.waypoint import Waypoint
from systems.DriveSystem import DriveSystem


class WaypointSystem:
    def __init__(self, drive_system: DriveSystem):
        self.drive_system = drive_system
        self.waypoints = []
        self.current_x = 0
        self.current_y = 0
        self.current_angle = 0  # Starting angle is 0 degrees

    def add_waypoint(self, waypoint: Waypoint):
        self.waypoints.append(waypoint)

    def navigate_waypoints(self):
        for waypoint in self.waypoints:
            delta_x = waypoint.x - self.current_x
            delta_y = waypoint.y - self.current_y
            # Fucking hate it, took so many tries to get this right, I am tired
            # - IngPleb
            distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
            angle = math.degrees(math.atan2(delta_y, delta_x)) - self.current_angle

            # Rotate to the new heading
            self.drive_system.rotate_angle(angle)
            self.current_angle += angle

            # Move forward to the waypoint
            if waypoint.use_correction:
                self.drive_system.move_distance(distance)
            else:
                self.drive_system.move_distance_without_correction(distance)

            self.current_x = waypoint.x
            self.current_y = waypoint.y
