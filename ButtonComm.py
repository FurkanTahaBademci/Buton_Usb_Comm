import serial
import serial.tools.list_ports
import re

baudrate = 115200
ser = None  # Başlangıçta seri port nesnesi None

def find_and_connect(baudrate):
    """
    Mevcut tüm seri portları bulur ve uygun olanı bağlanmak için dener.
    Eğer bağlantı sağlanamazsa None döndürür.
    """
    ports = serial.tools.list_ports.comports()
    print("Bulunan port sayısı:", len(ports))

    if len(ports) == 0:
        print("Hiçbir port algılanamadı.")
        return None

    for port in ports:
        print(f"{port.device} portuna bağlanmayı deniyor...")
        try:
            ser = serial.Serial(port.device, baudrate)
            # Bağlantı başarılı, seri port nesnesini döndür
            print(f"{port.device} portuna başarıyla bağlanıldı.")
            return ser
        except serial.SerialException:
            print(f"{port.device} portuna bağlanılamadı.")

    print("Hiçbir portla bağlantı sağlanamadı.")
    return None

def ButtonClient():
    """
    Seri port üzerinden veri okuma işlevi.
    Bağlantı kurulduktan sonra aynı portta kalır.
    """
    global ser  # Ser değişkenini global olarak kullan

    # Eğer ser değişkeni None ise, bağlantı kurmaya çalış
    if ser is None:
        ser = find_and_connect(baudrate)
        if ser is None:
            return "Bağlantı sağlanamadı."

    try:
        if ser.in_waiting > 0:
            # Veriyi okur ve UTF-8 formatında çözümler
            line = ser.readline().decode('utf-8').strip()
            # Gelen veride 'Pin:' ifadesini arar ve eğer bulursa pin değerini çıkarır
            match = re.search(r'Pin:(\d)', line)
            if match:
                pin_value = match.group(1)
                print(pin_value)
                return str(pin_value)
        return "0"  # Veri yoksa "0" döner
    except KeyboardInterrupt:
        print("Program durduruldu.")
        return "Program durduruldu."
    except serial.SerialException:
        print("Bağlantı kesildi, yeniden bağlanılacak.")
        ser.close()
        ser = None  # Bağlantı kesildiğinde ser'i None yap
        return "bağlanılamadı"
