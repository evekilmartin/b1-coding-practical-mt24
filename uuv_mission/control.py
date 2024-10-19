# Module to implement PD Feedback Controller
# u[t] = KP · e[t] + KD · (e[t] − e[t − 1])
# e[t] = r[t] − y[t]

class controller:
    def __init__(self, KP: float, KD: float):
        self.KP = KP
        self.KD = KD 

    def find_error(self,reference: float, observation: float):
        error = reference - observation
        return error

            
    def control(self, reference: float, observation: float, error_prev: float):
        #Function to implement the PD controller
        #error_prev is the error at the previous time step (e[t-1])
        #observation is the depth (y[t])
        
        #Calculate the error term
        error = self.find_error(reference, observation)

        #Calculate the action
        action = self.KP*error + self.KD*(error - error_prev)

        #Output the action
        return action, error