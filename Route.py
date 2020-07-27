class route:
    def __init__(self, name, start, end, time, directions, link):
        self.name = name
        self.start = start
        self.end = end
        self.time = time
        self.directions = directions
        self.link = link

    def to_object(self):
        return self.__dict__


        