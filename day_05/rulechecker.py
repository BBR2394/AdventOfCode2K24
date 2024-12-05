

class RuleChecker:
    def __init__(self, num):
        print("bonjour nombre : ", num)
        #the Number
        self.number = 0
        # number before the Number
        self.previouser = []
        # number after the Number
        self.follower = []
        self.number = num

    def getNumber(self):
        return self.number

    