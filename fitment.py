import math

class WheelFitment:
    MIN_TIRE_CLEARANCE = 15  # Minimum safe tire to fender clearance
    MIN_STRUT_CLEARANCE = 15  # Minimum safe tire to strut clearance

    def __init__(self, front_wheel_diameter, front_wheel_width, front_offset, front_tire_width, rear_wheel_diameter, rear_wheel_width, rear_offset, rear_tire_width):
        self.front_wheel_diameter = front_wheel_diameter
        self.front_wheel_width = front_wheel_width
        self.front_offset = front_offset
        self.front_tire_width = front_tire_width
        self.rear_wheel_diameter = rear_wheel_diameter
        self.rear_wheel_width = rear_wheel_width
        self.rear_offset = rear_offset
        self.rear_tire_width = rear_tire_width
        
    # Function to calculate wheel fitment
    def calculate_fitment(self):
        results = {}
        results["front"] = self.calculate_fitment_per_wheel(self.front_wheel_diameter, self.front_wheel_width, self.front_offset, self.front_tire_width)
        results["rear"] = self.calculate_fitment_per_wheel(self.rear_wheel_diameter, self.rear_wheel_width, self.rear_offset, self.rear_tire_width)
        return results
    
    def calculate_fitment_per_wheel(self, wheel_diameter, wheel_width, offset, tire_width):
        # Validate input
        if not (isinstance(wheel_diameter, int) and isinstance(wheel_width, int) and isinstance(offset, int) and isinstance(tire_width, int)):
            raise ValueError("Input values must be integers")
        
        if not (math.isclose(wheel_diameter, int(wheel_diameter), rel_tol=1e-9) and math.isclose(wheel_width, int(wheel_width), rel_tol=1e-9) and math.isclose(offset, int(offset), rel_tol=1e-9) and math.isclose(tire_width, int(tire_width), rel_tol=1e-9)):
            raise ValueError("Input values must be integers")
        
        if not (self.MIN_TIRE_CLEARANCE < offset < wheel_diameter - self.MIN_TIRE_CLEARANCE):
            raise ValueError("Invalid offset")
        
        if not (self.MIN_TIRE_CLEARANCE < tire_width < wheel_width - self.MIN_TIRE_CLEARANCE):
            raise ValueError("Invalid tire width")
        
        # Calculate tire to fender clearance
        tire_clearance = offset + (wheel_width / 2) - (tire_width / 2)
    
        # Calculate tire to strut clearance
        strut_clearance = (wheel_diameter / 2) - offset

        # Check if fitment is safe
        if tire_clearance < self.MIN_TIRE_CLEARANCE or strut_clearance < self.MIN_STRUT_CLEARANCE:
            return {"status":"Invalid fitment - not safe", "tire_clearance": tire_clearance, "strut_clearance": strut_clearance}
        else:
            return {"status":"Valid fitment - safe", "tire_clearance": tire_clearance, "strut_clearance": strut_clearance}

# Example usage
fitment = WheelFitment(18, 9, 35, 245, 18, 9, 35, 245)

print(fitment.calculate_fitment())
