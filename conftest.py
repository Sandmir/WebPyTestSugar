from fixture.application import Application
import pytest


# fixture for user mode
@pytest.fixture(scope='module')
def appLogin(request):
    fixture = Application()
    fixture.session.login(psw=fixture.session.get_new_psw())
    fixture.session.return_to_home_page()

    def fin():
        # fixture.session.logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


# fixture for guest mode
@pytest.fixture(scope='module')
def appGuest(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


#  general fixture
# @pytest.fixture(scope='module')
@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
