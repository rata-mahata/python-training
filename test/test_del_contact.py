__author__ = 'Olga'

from model.contact import Contact
from random import randrange

def test_delete_some_contact(app):
    if app.contact.count()== 0:
        app.contact.create(Contact(name="test contact"))

    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) - 1 == len(new_contacts)
#    old_contacts[index:index+1]= []
    assert old_contacts == new_contacts

#def test_delete_last_contact(app):
#    if app.contact.count()== 0:
#        app.contact.create(Contact(name="test contact"))
#
#    old_contacts = app.contact.get_contact_list()
#    app.contact.delete_last_contact()
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) - 1 == len(new_contacts)
#    old_contacts[0:1]= []
#    assert old_contacts == new_contacts





