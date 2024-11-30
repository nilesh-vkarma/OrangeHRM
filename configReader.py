import configparser


class ConfigReader:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("add absolute path of config.properties file")

    def get_value(self, section, key):
        return self.config.get(section, key)
