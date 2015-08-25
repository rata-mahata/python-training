# -*- coding: utf-8 -*-


from model.contact import Contact

def test_add_contact(app):
    app.contact.create(Contact(name="Jane", surname="Doe", title="Ms", phone="012345678", email="jane.doe@gmail.com"))


