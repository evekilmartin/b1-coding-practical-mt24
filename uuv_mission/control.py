# Module to implement PD Feedback Controller
# u[t] = KP · e[t] + KD · (e[t] − e[t − 1])
# e[t] = r[t] − y[t]
# Initial thoughts
# y[t] would just be the current position of the submarine (so need to read that from Submarine class? Or trajectory)
# Get e[t] (and need to store these to be able to use e[t-1])
# Then u[t] ...what is u[t]? It is the control action at discrete time. The output of the controller
# Represents a desired change in depth, can be positive or negative

# Import anything you need (maybe numpy)
#Controller class, method to calculate the u[t] value
#Using a class allows you to change the Kd/Kp values for a test fairly easily but write as a function first and then change
#There is a variable called "actions" in the ClosedLoop class already
# force_y = -self.drag * self.vel_y + self.actuator_gain * (action + disturbance)
#^ only time I think actions is used, doesn't specify what the hell it is. Lack of other information, assume it is equal to u[t]


#Inputs:
#the arrays to put the values into
# the reference and observation signals

#Outputs:
# action
# current error

class controller:
    def __init__(self):
        self.KP = 0.15
        self.KD = 0.6

            
    def control(self, reference, observation, error_prev):
        #error_prev is the error at the previous time step
        #Calculate the error term
        error = reference - observation

        #Calculate the action
        action = self.KP*error - self.KD*(error - error_prev)

        #Output the action and the current error
        return action, error