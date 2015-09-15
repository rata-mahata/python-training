__author__ = 'Olga'
from sys import maxsize
class Contact:

    def __init__(self, surname=None, name=None, title=None, phone=None, email=None, id=None):
        self.name = name
        self.surname = surname
        self.title = title
        self.phone = phone
        self.email = email
        self.id = id

    def __repr__(self):
        return "%s:%s %s" % (self.id, self.surname, self.name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and (self.surname is None or other.surname is None or self.surname == other.surname) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize