import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200


def test_index_content(client):
    response = client.get("/restapi?phrase=H")
    assert response.content_type == "application/json"


def test_insert_and_delete_book(client):
    book_name = "1qaz@wsx3edc$rfv"
    # Sprawdź, czy książka "123test123" nie istnieje w bazie
    response = client.get("/restapi?phrase=123test123")
    assert book_name not in response.get_data(as_text=True)

    # Dodaj książkę "123test123" do bazy
    response = client.post(
        "/insert",
        data={
            "title": f"{book_name}",
            "authors": "John Doe",
            "published_date": "2023-01-01",
            "ISBN10": "1234567890",
            "ISBN13": "9781234567890",
            "page_count": "100",
            "preview_link": "https://example.com",
            "language": "English",
        },
    )

    # Sprawdź, czy książka "123test123" istnieje w bazie
    response = client.get(f"/restapi?phrase={book_name}")
    data = response.get_json()
    book_id = data[0]["id"]  # Pobierz identyfikator dodanej książki
    assert book_name in response.get_data(as_text=True)

    response = client.get(f"/delete/{book_id}/")
    response = client.get(f"/restapi?phrase={book_name}")
    assert book_name not in response.get_data(as_text=True)


def test_google(client):
    response = client.get("/google")
    assert response.status_code == 200


def test_google_data_search(client):
    response = client.get("/google?search=harry+potter+komnata+i+tajemnic")
    assert b"Harry Potter i komnata tajemnic" in response.data
