import pytest
from hypothesis import given, strategies as st
from faker import Faker
fake = Faker()
def generate_user(): #kullanıcı bilgilerini rastgele üretmek için fonksiyon
    return {
        "name": fake.name(),
        "email": fake.email(),
        "address": fake.address()
    }

user_strategy = st.builds(generate_user) #hypothesis için strateji tanımlama

@given(user=user_strategy)
def test_user_registration(user):
    is_registered = fake.boolean()
    assert is_registered == st.builds(generate_user)