import pytest 

@pytest.fixture(scope='module')
def base_url():
    return 'https://turn24.ru/api/virage'
