import requests

def test_get_version():
    response = requests.get("http://localhost:8000/version")
    assert response.status_code == 200
    assert response.json() == {"version": "1.0.0"}  # Cập nhật theo API của bạn

def test_prime_number():
    response = requests.get("http://localhost:8000/prime?number=7")
    assert response.status_code == 200
    assert response.json() == {"number": 7, "is_prime": True}  # Cập nhật theo API của bạn

# Thêm các test case khác ở đây

def test_prime_number_2():
    response = requests.get("http://localhost:8000/prime?number=10")
    assert response.status_code == 200
    assert response.json() == {"number": 10, "is_prime": False}  # Cập nhật theo API của bạn

def test_invalid_prime_number():
    response = requests.get("http://localhost:8000/prime?number=-5")
    assert response.status_code == 400  # Nếu API của bạn trả về lỗi cho giá trị không hợp lệ
    assert response.json() == {"detail": "Invalid number"}  # Cập nhật theo API của bạn

def test_get_version_not_found():
    response = requests.get("http://localhost:8000/version_not_found")
    assert response.status_code == 404  # Nếu đường dẫn không tồn tại
    assert response.json() == {"detail": "Not Found"}  # Cập nhật theo API của bạn

def test_get_version_with_invalid_url():
    response = requests.get("http://localhost:8000/verssion")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}

def test_prime_number_edge_case():
    response = requests.get("http://localhost:8000/prime?number=2")
    assert response.status_code == 200
    assert response.json() == {"number": 2, "is_prime": True}

def test_prime_number_zero():
    response = requests.get("http://localhost:8000/prime?number=0")
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid number"}

def test_prime_number_one():
    response = requests.get("http://localhost:8000/prime?number=1")
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid number"}

def test_large_prime_number():
    response = requests.get("http://localhost:8000/prime?number=104729")
    assert response.status_code == 200
    assert response.json() == {"number": 104729, "is_prime": True}

