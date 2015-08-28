__author__ = 'Olga'

from model.contact import Contact


def test_delete_last_contact(app):
    if app.contact.count()== 0:
        app.contact.create(Contact(name="test contact"))
    app.contact.delete_last_contact()





