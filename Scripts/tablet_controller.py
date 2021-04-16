import time


class TabletController:
    def __init__(self, session, dialog_controller):
        self.session = session
        self.dialog_controller = dialog_controller
        self.ALMemory = self.session.service("ALMemory")
        self.set_listener_show_image()

    def set_listener_show_image(self):
        self.ALMemory.declareEvent("image")
        self.subscriber = self.ALMemory.subscriber("image")
        self.subscriber.signal.connect(self.on_image_to_show)

    def on_image_to_show(self, image):
        """Stubbing the image showing"""
        print("Showing image of {}".format(image))
        time.sleep(2)
        print("Hiding image of {}".format(image))

    def show_article(self, url):
        """Stubbing the webview showing"""
        print("Showing webview with the article to user...")

    def hide_article(self):
        """Stubbing the hiding"""
        print("Hiding webview...")
        self.dialog_controller.start_final_dialog()