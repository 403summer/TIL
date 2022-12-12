class Note(object):
    def __init__(self, contents = None):
        self.contents = contents

    def write_contents(self, contents):
        self.contents = contents

    def remove_all(self):
        self.contents = ""

    def __str__(self):
        return self.contents
