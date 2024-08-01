def inc(x): #geriye değer döndüren bir fonksiyon.
    return x + 1
def test_answer(): #tanımlanan fonksiyonun test fonksiyonunu.
    assert inc(3) == 5 #yanlış sonuç testi.
    #assert inc(4) == 5 #doğru sonuç testi.
    #assert inc(2) == 6, "Girilen değer sonuçla uyuşmuyor."  #hata mesajı yazdırma.
# assert verilen koşulun doğru olup olmadığını kontrol eder.