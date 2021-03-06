# -*- coding: utf-8 -*-

from sys import maxsize
from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(name="Jane", surname="Doe", title="Ms", phone="012345678", email="jane.doe@gmail.com")
    app.contact.create(contact)

    assert len(old_contacts)+ 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


