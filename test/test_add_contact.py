# -*- coding: utf-8 -*-

import pytest
from model.contact import Contact
from fixture.application_contact import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):

    app.login(username="admin", password="secret")
    app.create_contact(Contact(name="Jane", surname="Doe", title="Ms", phone="012345678", email="jane.doe@gmail.com"))
    app.logout()
