__author__ = 'Olga'

from model.group import Group

def test_modify_first_group(app):
        app.session.login(username="admin", password="secret")
        app.group.modify_first_group(Group(name="five", header="six", footer="seven"))
        app.session.logout()
