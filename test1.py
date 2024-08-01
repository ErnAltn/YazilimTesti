from hypothesis import given
from hypothesis import strategies as st #hypothesis kütüphanelerin yüklenmesi
@given(st.integers(), st.integers()) #Test fonksiyonu için rastgele sayılar üretir.
def test_addition(a,b): 
    assert a + b == b + a #test fonksiyonu oluştur ve assert ile kontrol et.