class Trial:
    def __init__(self, trials):
        self.trials = sorted(trials.split())

    def __repr__(self):
        return f"Trial('{self.trials[0]}')"

    def get_trials(self):
        return ' '.join(self.trials)


class GhostRescue(Trial):
    def __init__(self, trials, name):
        super().__init__(trials)
        self.name = name

    def __repr__(self):
        return f"GhostRescue('{self.trials[0]}', '{self.name}')"

    def add(self, value):
        self.trials.append(value)
        self.trials.sort()

    def pop(self, key):
        self.trials.remove(key)
        return key

    def __contains__(self, key):
        return key in self.trials

    def __iter__(self):
        return iter(self.trials)

    def __len__(self):
        return len(self.trials)
    
tr = Trial("come see win")
print(tr)
print(tr.get_trials())
gr = GhostRescue("visions horror whispers", "Centerville")
print(len(gr))
print(gr.pop("horror"))
print(gr.get_trials())
print(gr)
gr = GhostRescue("pursue harass", "Outiss")
gr.add("harm")
for item in gr:
   print(item)
print(gr)
print(gr.get_trials())
print(issubclass(GhostRescue, Trial))