import requests

def test_auth_request_with_non_existen_user(base_url):
    request = requests.post('https://turn24.ru/api/auth/v2/credentialsLogin',
                            json={
                                'password': '+7 (908) 200-98-29',
                                'email': 'yura.voskanyan.2003@mail.ru'})
    assert request.status_code == 422
    data = request.json()
    assert data 
    assert data == {"message":"Invalid credentials","errors":{"email":["Invalid credentials"]}}