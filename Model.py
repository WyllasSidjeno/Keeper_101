
class MainModel:
    def __init__(self):
        self.data = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data


def format_text_to_path(name, imgtype=".png", destination="./"):
    name = name.lower().replace(" ", "_")
    path = destination + name + imgtype
    return path
