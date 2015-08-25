__author__ = 'Olga'

from model.group import Group

def test_modify_group_name(app):

    app.group.modify_first_group(Group(name="newest group"))


def test_modify_group_header(app):

    app.group.modify_first_group(Group(header="newest header"))
