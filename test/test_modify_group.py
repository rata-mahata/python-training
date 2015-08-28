__author__ = 'Olga'

from model.group import Group

def test_modify_group_name(app):
    if app.group.count()== 0:
        app.group.create(Group(name="test group"))
    app.group.modify_first_group(Group(name="newest group"))


def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="newest header"))
