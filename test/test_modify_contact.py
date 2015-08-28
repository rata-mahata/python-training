__author__ = 'Olga'


from model.contact import Contact


def test_modify_contact_phone(app):
    app.contact.modify_first_contact(Contact(phone="87651111"))

def test_modify_contact_title(app):
    app.contact.modify_first_contact(Contact(title="Dr"))





