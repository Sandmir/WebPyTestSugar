from fixture.application import Application
import pytest
import json
import os.path


configfile = None

def run_app(request):
    global configfile
    run_browser = request.config.getoption("--browser")
    if configfile is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),request.config.getoption("--configfile"))
        with open(config_file) as config_file:
            configfile = json.load(config_file)
    fixture = Application(browser=run_browser, base_url=configfile["baseUrl"])
    return fixture

# fixture for user mode
@pytest.fixture(scope='module')
def appLogin(request):
    fixture = run_app(request)
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
    fixture = run_app(request)
    request.addfinalizer(fixture.destroy)
    return fixture


#  general fixture
# @pytest.fixture(scope='module')
@pytest.fixture()
def app(request):
    fixture = run_app(request)
    request.addfinalizer(fixture.destroy)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action = "store", default = "chrome")
    parser.addoption("--configfile", action="store", default= "configfile.json")

