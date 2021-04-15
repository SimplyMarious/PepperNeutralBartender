import time


class FaceDetection:
    def __init__(self, session):
        self.session = session
        self.ALMemory = session.service("ALMemory")
        self.set_face_detection()
        self.wait_for_detection()

    def set_face_detection(self):
        self.subscriber = self.ALMemory.subscriber("FaceDetected")
        self.subscriber.signal.connect(self.on_human_tracked)

    def on_human_tracked(self, value):
        """TODO: start topic 'DialogoNeutrale' (it should be setted into the Starter)"""
        """Note that in now, in the Choregraphe's project, it would raise the event AttentionEvent/FullyEngaged5,
            even if the user doesn't stares Pepper for 5 seconds"""

    def wait_for_detection(self):
        """Stubbing the face detection"""
        #while True:
        #   time.sleep(1)
        self.ALMemory.raiseEvent("FaceDetected", "Human tracked!")

