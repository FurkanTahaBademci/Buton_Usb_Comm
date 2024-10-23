# Python'un 'serial' modülünü içe aktararak seri port işlemleri için gerekli fonksiyonlara erişim sağlar
import serial.tools.list_ports
# Python'un 're' modülünü içe aktararak düzenli ifade işlemleri için gerekli fonksiyonlara erişim sağlar
import re

# Seri port üzerinden veri okuma işlevini tanımlayan fonksiyon


def read_serial(port, baudrate):
    # Serial port nesnesini belirtilen port ve baudrate ile başlatır
    ser = serial.Serial(port, baudrate)
    print(f"Connected to {port}")
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
                    print(f"Pin Value: {pin_value}")
    except KeyboardInterrupt:
        # Eğer kullanıcı klavyeden kesme işlemi yaparsa mesaj yazdırır
        print("Program durduruldu.")
    finally:
        # Her durumda portu kapatmayı garantiler
        ser.close()

def find_and_connect(baudrate):
    # Mevcut tüm portları bulur
    ports = serial.tools.list_ports.comports()

    print("Detected ports len:",len(ports))

    if len(ports) == 0:
        print("No port detected")
        return

    for port in ports:
        print(f"Trying to connect to {port.device}")
        try:
            read_serial(port.device, baudrate)
            break  # Bağlantı başarılı olursa döngüden çık
        except serial.SerialException:
            print(f"Failed to connect to {port.device}")

if __name__ == "__main__":
    # Bağlantı hızı olarak 115200 baudrate kullanılacak
    baudrate = 115200
    # Mevcut portları bulup bağlanmayı dener
    find_and_connect(baudrate)