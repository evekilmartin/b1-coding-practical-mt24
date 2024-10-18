# Module to implement PD Feedback Controller
# u[t] = KP · e[t] + KD · (e[t] − e[t − 1])
# e[t] = r[t] − y[t]

#Inputs:
# the reference and observation signals
# the error on the previous time step

#Outputs:
# action
# current error

class controller:
    def __init__(self, KP, KD):
        self.KP = KP
        self.KD = KD

    #def find_error(self,reference, observation):
        #error = reference - observation
        #return error
        #This was useful when a slightly different method was being trialled, which worked but didn't improve anything
        #No longer useful so commented out
            
    def control(self, reference, observation, error_prev):
        #error_prev is the error at the previous time step
        #Calculate the error term
        #error = self.find_error(reference, observation)
        error = reference - observation

        #Calculate the action
        action = self.KP*error + self.KD*(error - error_prev)

        #Output the action
        return action, error