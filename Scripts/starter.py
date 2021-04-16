import qi
import face_detection, dialog_controller


class Starter:
    def __init__(self):
        self.session = qi.Session()
        self.pepperIP = "localhost"
        self.pepperPort = 9559
        if self.connect_to_pepper():
            self.stand_pepper()
            self.set_LED_eyes("white")
            self.dialog_controller = dialog_controller.DialogController(self.session)
            face_detection.FaceDetection(self.session, self.dialog_controller)

    def connect_to_pepper(self):
        try:
            self.session.connect("tcp://{}:{}".format(self.pepperIP, self.pepperPort))
            print("Connected to {}:{}".format(self.pepperIP, self.pepperPort))
            return True
        except RuntimeError:
            print ("\nCan't connect to Naoqi at IP {} (port {}).\nPlease check your script's arguments."
                   " Run with -h option for help.\n".format(self.pepperIP, self.pepperPort))
            return False

    def stand_pepper(self):
        self.ALRobotPosture = self.session.service("ALRobotPosture")
        self.ALRobotPosture.goToPosture("Stand", 0.8)

    def set_LED_eyes(self, colour):
        self.ALLeds = self.session.service("ALLeds")
        self.ALLeds.fadeRGB("FaceLeds", colour, 1)


if __name__ == "__main__":
    starter = Starter()
