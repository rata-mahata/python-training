__author__ = 'Olga'


from model.contact import Contact


def test_modify_contact_name(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(name="acdc")
    contact.id = old_contacts[0].id
    if app.contact.count()== 0:
        app.contact.create(Contact(name="test contact"))
    app.contact.modify_first_contact(contact)

    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)








