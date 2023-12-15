class MobilePhone:
    def __init__(self, name, operating_system, battely_life, status):
        self.name = name
        self.operating_system = operating_system
        self.battely_life = battely_life
        self.status = status

    def turn_on(self):
        self.status = True

    def turn_off(self):
        self.status = False

    def check_battery_life(self):
        return self.battely_life
