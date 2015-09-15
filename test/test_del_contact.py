__author__ = 'Olga'

from model.contact import Contact


def test_delete_last_contact(app):
    if app.contact.count()== 0:
        app.contact.create(Contact(name="test contact"))

    old_contacts = app.contact.get_contact_list()
    app.contact.delete_last_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1]= []
    assert old_contacts == new_contacts






