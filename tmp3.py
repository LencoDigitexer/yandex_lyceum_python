class Talking:
    def __init__(self, name, time, topics=None):
        self.name = name
        self.time = time
        self.topics = topics or []

    def add_theme(self, value):
        self.topics.append(value)

    def change_theme(self):
        first = self.topics.pop(0)
        self.topics.append(first)

    def change_time(self, number):
        self.time += number

    def __eq__(self, other):
        return (self.time == other.time) and (len(self.topics) == len(other.topics)) and (self.name == other.name)

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return (self.time < other.time) or (
            (self.time == other.time) and (len(self.topics) < len(other.topics))) or (
            (self.time == other.time) and (len(self.topics) == len(other.topics)) and
            (self.name < other.name))

    def __gt__(self, other):
        return not ((self < other) or (self == other))

    def __le__(self, other):
        return (self < other) or (self == other)

    def __ge__(self, other):
        return not (self < other)

    def __str__(self):
        if self.topics:
            main_theme = self.topics[0]
        else:
            main_theme = "None"

        return f"{self.name}'s Conversation, main theme is {main_theme} for {self.time} minutes"
    
tk = Talking('Alice', 5)
tk1 = Talking('Hatter', 5)
print(tk < tk1)
tk.add_theme('cricket')
tk1.add_theme('teatime')
print(tk == tk1)
tk.change_time(1)
print(tk >= tk1)