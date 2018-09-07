class Registration():
    def __init__(self):
        self.user_bio = dict()

    def add(self, email, firstname, lastname):
        self.user_bio[firstname] = lastname

    def get_email(self, email):
        return self.user_bio[email]

    def user_bio_length(self, user_bio):
        return len(self.user_bio)