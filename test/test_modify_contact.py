__author__ = 'Olga'


from model.contact import Contact

def test_modify_first_contact(app):

    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(name="John", surname="Roo", title="Mr", phone="87654321", email="john.roo@gmail.com"))
    app.session.logout()