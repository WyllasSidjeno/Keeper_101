from abc import ABC


class AbstractModel(ABC):
    """Abstract class for models"""
    def __init__(self):
        """Create the model"""
        self.data = None
        """The data of the model"""
    def get_data(self):
        """Get the data from the model"""
        return self.data

    def set_data(self, data):
        """Set the data in the model"""
        self.data = data


def format_text_to_path(name, imgtype=".png", destination="./"):
class MainModel(AbstractModel):
    """The model of the main window"""
    def __init__(self):
        """Create the model"""
        super().__init__()

class ContentModel(AbstractModel):
    """The model of the content area"""
    def __init__(self):
        """Create the model"""
        super().__init__()


    name = name.lower().replace(" ", "_")
    path = destination + name + imgtype
    return path
