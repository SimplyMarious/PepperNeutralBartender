import ast
import random


class ArticleController:
    def __init__(self, session, dialog_controller, tablet_controller):
        self.session = session
        self.dialog_controller = dialog_controller
        self.tablet_controller = tablet_controller
        self.ALMemory = self.session.service("ALMemory")

        self.set_listener_read_article()
        self.article = self.load_random_article("../Resources/articolo.txt")

    def load_random_article(self, documentPath):
        self.document = open(documentPath)
        articles = ast.literal_eval(self.document.read())
        return articles[random.randint(0, 8)]

    def set_listener_read_article(self):
        self.ALMemory.declareEvent("articolo")
        self.subscriber = self.ALMemory.subscriber("articolo")
        self.subscriber.signal.connect(self.on_article_to_read)

    def on_article_to_read(self, value):
        title = self.get_article_title()
        description = self.get_article_description()
        self.tablet_controller.show_article(self.article['url'])
        self.dialog_controller.read_article(title, description)

    def get_article_title(self):
        return self.article["title"].encode("utf-8")

    def get_article_description(self):
        return self.article["description"].encode("utf-8")
