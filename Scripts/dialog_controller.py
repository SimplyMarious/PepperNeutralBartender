import time

import tablet_controller, article_controller


class DialogController:
    def __init__(self, session):
        self.session = session
        self.ALDialog = self.session.service("ALDialog")
        self.tablet_controller = tablet_controller.TabletController(self.session, self)
        self.article_controller = article_controller.ArticleController(self.session, self, self.tablet_controller)
        self.topic_names = []
        self.load_topic("C:\Users\Simply\Desktop\Simply\Progetti SW\Programmi\Python\NeutralBartender\Topics\dialogoNeutrale_iti.top",
                       "dialogoNeutrale")
        self.start_topic("dialogoNeutrale")

    def load_topic(self, topic_path, topic_name):
        decoded_topic_path = topic_path.decode('utf-8')
        self.topic_names.append(self.ALDialog.loadTopic(decoded_topic_path.encode('utf-8')))

    def start_topic(self, topic_name):
        self.ALDialog.setLanguage("Italian")
        self.ALDialog.activateTopic(topic_name)
        self.ALDialog.subscribe('my_dialog_example')

    def on_human_detected(self, value):
        print("Conversation {} started!".format(self.topic_names[len(self.topic_names) - 1]))

    def read_article(self, title, description):
        self.ALTextToSpeech = self.session.service("ALTextToSpeech")
        self.ALTextToSpeech.say("'\\vct=50\\ \\rspd=80\\ \\pau=1000\\ Oggi tra le notizie ho letto di " + title)
        time.sleep(3)
        self.ALTextToSpeech.say('\\vct=50\\ \\rspd=80\\ \\pau=1000\\' + description)
        self.tablet_controller.hide_article()

    def start_final_dialog(self):
        self.load_topic("C:\Users\Simply\Desktop\Simply\Progetti SW\Programmi\Python\NeutralBartender\Topics\dialogoNeutrale2_iti.top",
                       "dialogoNeutrale2")
        self.start_topic("dialogoNeutrale2")
        self.ALMemory = self.session.service("ALMemory")
        self.ALMemory.declareEvent("start")
        self.ALMemory.raiseEvent("start", 1)

        self.ALMemory.declareEvent("stop")
        self.subscriber_stop = self.ALMemory.subscriber("stop")
        self.subscriber_stop.signal.connect(self.free_components)

    def free_components(self, value):
        self.ALDialog.unsubscribe('my_dialog_example')
        for topic_name in self.topic_names:
            self.ALDialog.deactivateTopic(topic_name)
            self.ALDialog.unloadTopic(topic_name)
        print("Everything freed")