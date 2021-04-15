import qi
from naoqi import ALProxy





class Starter:
    def __init__(self):
        self.session = qi.Session()
        self.pepperIP = "localhost"
        self.pepperPort = 9559
        if self.connectToPepper():
            self.standPepper()

    def connectToPepper(self):
        try:
            self.session.connect("tcp://{}:{}".format(self.pepperIP, self.pepperPort))
            print("Connected to {}:{}".format(self.pepperIP, self.pepperPort))
            return True
        except RuntimeError:
            print ("\nCan't connect to Naoqi at IP {} (port {}).\nPlease check your script's arguments."
                   " Run with -h option for help.\n".format(self.pepperIP, self.pepperPort))
            return False

    def standPepper(self):
        ALRobotPosture = self.session.service("ALRobotPosture")
        ALRobotPosture.goToPosture("Stand", 0.8)


if __name__=="__main__":
    starter = Starter()