import requests

from schemes import ProductToBasket, Receive

def test_add_product_to_basket(base_url, pytestconfig):
    item = [{'product_id': '171341b3-cc19-11ec-bea6-a4bf0158334a', 'quantity': 1}]
    request = requests.post(f'{base_url}/basket',
                            json={'items': item})
    assert request.status_code == 200
    data = request.json()
    assert data 
    item = data[0]
    ProductToBasket(**item)
    token = request.cookies.get_dict()['sessionId']
    assert item['type'] == 'basket'
    assert item['product_id'] == '171341b3-cc19-11ec-bea6-a4bf0158334a'
    assert item['quantity'] == 1
    assert item['selected'] == True 
    assert token
    pytestconfig.cache.set('token', token)

def test_get_basket(base_url, pytestconfig):
    request = requests.get(f'{base_url}/basket',
                           cookies={'sessionId': pytestconfig.cache.get("token", None)})
    assert request.status_code == 200
    data = request.json()
    assert data
    assert data[0]['product_id'] == '171341b3-cc19-11ec-bea6-a4bf0158334a'

def test_prepare_order(base_url, pytestconfig):
    '''Получение данных для оформления заказа'''
    request = requests.get(f'{base_url}/orders/prepare',
                           cookies={'sessionId': pytestconfig.cache.get('token', None)})
    assert request.status_code == 200
    data = request.json()
    assert data['receives']
    Receive(**data['receives'][0])
    assert data['receives'][0]["id"] == 'PickupVirage'
    assert data['receives'][1]["id"] == 'PickupPvz'
    assert data['receives'][2]["id"] == 'Delivery'

def test_change_receive_id_to_pickup_pvz(base_url, pytestconfig):
    request = requests.post(f'{base_url}/orders/prepare',
                            cookies={'sessionId': pytestconfig.cache.get('token', None)},
                            json={'receive_id': 'PickupPvz'})
    assert request.status_code == 200
    data = request.json()
    assert data 
    assert data['data']['receive_id'] == 'PickupPvz'

def test_change_receive_id_to_pickup_virage(base_url, pytestconfig):
    request = requests.post(f'{base_url}/orders/prepare',
                            cookies={'sessionId': pytestconfig.cache.get('token', None)},
                            json={'receive_id': 'PickupVirage'})
    assert request.status_code == 200
    data = request.json()
    assert data 
    assert data['data']['receive_id'] == 'PickupVirage'

def test_change_receive_ud_to_delivery(base_url, pytestconfig):
    request = requests.post(f'{base_url}/orders/prepare',
                            cookies={'sessionId': pytestconfig.cache.get('token', None)},
                            json={'receive_id': 'Delivery'})    
    assert request.status_code == 200
    data = request.json()
    assert data 
    assert data['data']['receive_id'] == 'Delivery'

def test_set_profile_params(base_url, pytestconfig):
    '''Заполнение профиля данными о пользователе'''
    request = requests.post(f'{base_url}/orders/prepare',
                            json={"organization_id": None, "recipient": {"first_name": "хело", "phone": "79000000000", "email": "asd@mail.ru"}},
                            cookies={'sessionId': pytestconfig.cache.get('token', None)})
    assert request.status_code == 200
    data = request.json()
    assert data 

def test_order_prepare_change_pay_method_to_sbp(base_url, pytestconfig):
    '''Смена способа оплаты на СБП'''
    request = requests.post(f'{base_url}/orders/prepare',
                            json={'payment_id': 'PaymentSBPKrsk'},
                            cookies={'sessionId': pytestconfig.cache.get('token', None)})
    assert request.status_code == 200
    data = request.json()
    assert data
    assert data['data']['payment_id'] == 'PaymentSBPKrsk'

def test_order_prepare_change_pay_method_to_online(base_url, pytestconfig):
    '''Смена спобоа оплаты на оплату онлайн картой'''
    request = requests.post(f'{base_url}/orders/prepare',
                            json={'payment_id': 'PaymentBankCardKrsk'},
                            cookies={'sessionId': pytestconfig.cache.get('token', None)})
    assert request.status_code == 200
    data = request.json()
    assert data 
    assert data['data']['payment_id'] == 'PaymentBankCardKrsk'

def test_order_prepare_change_pay_method_to_split(base_url, pytestconfig):
    '''Смена спобоа оплаты на Яндекс сплит'''
    request = requests.post(f'{base_url}/orders/prepare',
                            json={'payment_id': 'PaymentSplitKrsk'},
                            cookies={'sessionId': pytestconfig.cache.get('token', None)})
    assert request.status_code == 200
    data = request.json()
    assert data 
    assert data['data']['payment_id'] == 'PaymentSplitKrsk'

def test_order_prepare_change_pay_method_to_podeli(base_url, pytestconfig):
    '''Смена спобоа оплаты на Подели'''
    request = requests.post(f'{base_url}/orders/prepare',
                            json={'payment_id': 'PaymentPodeliKrsk'},
                            cookies={'sessionId': pytestconfig.cache.get('token', None)})
    assert request.status_code == 200
    data = request.json()
    assert data 
    assert data['data']['payment_id'] == 'PaymentPodeliKrsk'

def test_order_prepare_change_pay_method_to_upon_receipt(base_url, pytestconfig):
    '''Смена спобоа оплаты на оплату при получении'''
    request = requests.post(f'{base_url}/orders/prepare',
                            json={'payment_id': 'PaymentPickupUponReceipt'},
                            cookies={'sessionId': pytestconfig.cache.get('token', None)})
    assert request.status_code == 200
    data = request.json()
    assert data 
    assert data['data']['payment_id'] == 'PaymentSBPKrsk'
