# Wheel-Fitment-Calculator

This program is a Python class called "WheelFitment" which is designed to calculate the fitment of a set of wheels and tires on a vehicle. The class takes 8 inputs, 4 for the front wheel and 4 for the rear wheel: wheel diameter, wheel width, offset, and tire width. It calculates the tire to fender clearance and tire to strut clearance based on the input values, and checks if the fitment is safe. It also takes into account the minimum safe tire to fender and strut clearance, which are defined as class variables, MIN_TIRE_CLEARANCE and MIN_STRUT_CLEARANCE, and are set to a default value of 15mm.

The class has two main methods:

__init__(self, front_wheel_diameter, front_wheel_width, front_offset, front_tire_width, rear_wheel_diameter, rear_wheel_width, rear_offset, rear_tire_width): This is the constructor method which is called when an instance of the class is created. It takes 8 inputs and assigns them to the object's variables.

calculate_fitment(self): This method is used to perform the fitment calculation. It calls the calculate_fitment_per_wheel() method for both front and rear wheel and returns a dictionary with the status of the fitment, the tire clearance and the strut clearance for each wheel.

calculate_fitment_per_wheel(self, wheel_diameter, wheel_width, offset, tire_width): This method does the calculation for each wheel and the input validation. It calculates the tire to fender clearance and tire to strut clearance based on the input values, and checks if the fitment is safe. If the tire to fender or strut clearance is negative, the fitment is considered unsafe and the program returns a dictionary with the status "Invalid fitment - not safe" along with the values for tire clearance and strut clearance. If the fitment is safe, it returns a dictionary with the status "Valid fitment - safe" along with the values for tire clearance and strut clearance.

To use the class, you will first need to create an instance of it by providing the 8 inputs in the constructor. For example:

```fitment = WheelFitment(18, 9, 35, 245, 18, 9, 35, 245)```

Then you can call the calculate_fitment() method to perform the fitment calculation and get the result.

```result = fitment.calculate_fitment()```

The result will be a dictionary with two keys "front" and "rear" that contain the status of the fitment, the tire clearance and the strut clearance for each wheel.

Please note that this program is a basic example and doesn't take into account all the possible factors that can affect wheel fitment, such as brake caliper clearance or suspension components. It's a good starting point to get a general idea of wheel fitment but it's not definitive.
