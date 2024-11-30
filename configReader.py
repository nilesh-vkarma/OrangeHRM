import configparser


class ConfigReader:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(r"C:\Users\nilja\PycharmProjects\OrangeHRM\config.properties")

    def get_value(self, section, key):
        return self.config.get(section, key)
