import ButtonComm
import time

def run():
    """
    Sürekli olarak ESP8266 ile iletişim kurarak pin durumunu kontrol eder.
    """
    while True:
        result = ButtonComm.ButtonClient()
        print(result)

        if result == "1":
            print("Butona basıldı")
        elif result == "0":
            print("Buton serbest")

        if "bağlanılamadı" in result:
            print("Bağlantı hatası tespit edildi. Yeniden denenecek...")
            time.sleep(3)  # Bağlantı hatası durumunda bekle
        else:
            # Normal sorgu döngüsü için kısa bir bekleme süresi
            time.sleep(0.05)

if __name__ == "__main__":
    run()
