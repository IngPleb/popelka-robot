class System:
    def __init__(self, name):
        self.name = name
        print("System {} initialized".format(self.name))

    def system_print(self, message):
        print("System {}: {}".format(self.name, message))
