# Python'un 'serial' modülünü içe aktararak seri port işlemleri için gerekli fonksiyonlara erişim sağlar
import serial
# Python'un 're' modülünü içe aktararak düzenli ifade işlemleri için gerekli fonksiyonlara erişim sağlar
import re

# Seri port üzerinden veri okuma işlevini tanımlayan fonksiyon


def read_serial(port, baudrate):
    # Serial port nesnesini belirtilen port ve baudrate ile başlatır
    ser = serial.Serial(port, baudrate)
    try:
        # Sonsuz döngü içinde veri bekler
        while True:
            # Eğer portta bekleyen veri varsa
            if ser.in_waiting > 0:
                # Veriyi okur ve UTF-8 formatında çözümler
                line = ser.readline().decode('utf-8').strip()
                # Gelen veride 'Pin:' ifadesini arar ve eğer bulursa pin değerini çıkarır
                match = re.search(r'Pin:(\d)', line)
                if match:
                    # Bulunan pin değerini yazdırır
                    pin_value = match.group(1)
                    print(pin_value)
    except KeyboardInterrupt:
        # Eğer kullanıcı klavyeden kesme işlemi yaparsa mesaj yazdırır
        print("Program durduruldu.")
    finally:
        # Her durumda portu kapatmayı garantiler
        ser.close()


# Programın ana giriş noktası
if __name__ == "__main__":
    # Seri port olarak COM4 kullanılacak
    port = 'COM4'
    # Bağlantı hızı olarak 115200 baudrate kullanılacak
    baudrate = 115200
    # Seri port okuma fonksiyonunu belirtilen port ve baudrate ile çağırır
    read_serial(port, baudrate)
