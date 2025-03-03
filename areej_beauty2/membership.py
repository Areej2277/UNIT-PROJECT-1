#Class loyalty program for customers
class Membership:
    def __init__(self,membership:str="White"):  #Initializ the membership with a default type and zero loyalty points
        self.membership:str = membership
        self.loyalty_points = 0

    #Add the specified number of loyalty points to the current total
    def  add_points(self, points: int):
        self.loyalty_points += points

     ## Check if there are enough loyalty points to redeem
    def redeem_points(self, points: int):
        if points > self.loyalty_points:
            return False
        self.loyalty_points -= points
        return True


    def __str__(self):
        return f"Membership Type: {self.membership}, Loyalty Points: {self.loyalty_points}"
            