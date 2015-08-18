__author__ = 'Olga'




def test_delete_last_contact(app):
        app.session.login(username="admin", password="secret")
        app.contact.delete_last_contact()
        app.session.logout()



