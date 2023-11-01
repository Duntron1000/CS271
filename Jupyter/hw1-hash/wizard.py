class Wizard:
    def __init__(self, name, month, day, year):
        self.name = name
        self.month = month
        self.day = day
        self.year = year
    
    def __repr__(self):
        return "{}: {}/{}/{}".format(self.name, self.month, self.day, self.year)
    
    def __hash__(self):
        return self.day * 12 + self.month
    
    def __eq__(self, obj):
        return self.name == obj.name and self.month == obj.month and self.day == obj.day and self.year == obj.year

def get_all_wizards():
    """
    Return a set of all of the wizards in the database
    """
    wizards = set([])
    fin = open("HarryPotter.csv")
    for line in fin.readlines():
        name, month, day, year = line.split(",")
        wizards.add(Wizard(name, int(month), int(day), int(year)))
    return wizards

if __name__ == '__main__':
    wizards = get_all_wizards()
    for w in wizards:
        print(w, hash(w))