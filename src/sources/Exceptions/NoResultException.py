class NoResultException(Exception):
    def __init__(self, message):
        self.messge = message

    def __str__(self):
        return self.message

