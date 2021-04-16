import time


class FaceDetection:
    def __init__(self, session, dialog_controller):
        self.dialog_controller = dialog_controller
        self.session = session
        self.ALMemory = session.service("ALMemory")
        self.set_face_detection()
        self.wait_for_detection()

    def set_face_detection(self):
        self.subscriber = self.ALMemory.subscriber("FaceDetected")
        self.subscriber.signal.connect(self.dialog_controller.on_human_detected)

    def wait_for_detection(self):
        """Stubbing the face detection"""
        #while True:
        #   time.sleep(1)
        self.ALMemory.raiseEvent("FaceDetected", 1)

