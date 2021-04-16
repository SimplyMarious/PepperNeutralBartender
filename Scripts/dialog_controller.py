class DialogController:
    def __init__(self, session):
        # Getting the service ALDialog
        self.ALDialog = session.service("ALDialog")
        self.loadTopic("C:\Users\Simply\Desktop\Simply\Progetti SW\Programmi\Python\NeutralBartender\Topics\dialogoNeutrale_iti.top")
        self.startTopic(self.topic_name)

    def loadTopic(self, topic_path):
        decoded_topic_path = topic_path.decode('utf-8')
        self.ALDialog.unloadTopic("dialogoNeutrale")
        self.topic_name = self.ALDialog.loadTopic(decoded_topic_path.encode('utf-8'))

    def startTopic(self, topic_name):
        self.ALDialog.setLanguage("Italian")
        self.ALDialog.activateTopic(topic_name)
        self.ALDialog.subscribe('my_dialog_example')

    def on_human_detected(self, value):
        print("Conversation {} started!".format(self.topic_name))
        """TODO: set event listeners for images on tablet
            with a tablet_controller having a on_image_to_show method"""