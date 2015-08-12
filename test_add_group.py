# -*- coding: utf-8 -*-

import pytest
from group import Group
from application import Application


    # функция которая инициализирует текстуру. Метка @ превращает функцию в инициализатор текстуры #
@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
    def test_add_group(app):
        app.login(username="admin", password="secret")
        app.create_group(Group(name="first", header="dfadsf", footer="dfdsf"))
        app.logout()

    def test_add_empty_group(app):
        app.login(username="admin", password="secret")
        app.create_group(Group(name="", header="", footer=""))
        app.logout()



