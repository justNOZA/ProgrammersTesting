class Title:
    def __init__(self, title):
        self.title = title
    def change(self) :
        mainT = self.title.split(':')[0].upper().center(60) + '\n' + self.title.split(':')[1].title().center(60)
        return mainT

t = 'star wars : the empire strikes back'
a = Title(t)
print(a.change())
