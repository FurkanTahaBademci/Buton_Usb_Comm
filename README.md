# Seri Port Veri Okuyucu

Bu proje, belirli bir seri port üzerinden gelen verileri sürekli olarak okumak ve işlemek için Python dilinde yazılmış bir uygulamadır. Özellikle, bağlı cihazlardan gelen "Pin" değerlerini yakalar ve ekrana yazdırır.

## Başlangıç

Bu rehber, projenin nasıl kurulup çalıştırılacağına dair adımları içermektedir.

### Gereksinimler

Bu kodu çalıştırmak için Python'un yanı sıra `pyserial` paketine ihtiyacınız vardır. Eğer sisteminizde bu paket yüklü değilse, aşağıdaki komut ile yükleyebilirsiniz:

```
pip3 install pyserial
```
## Çalıştırmadan önce USB yetkilendirmesi yapılması gerekmektedir. Aşağıdaki komutu konsola yazdırın

```
sudo chmod a+rw /dev/ttyUSB0
```
## Çalıştırmak için:
```
python3 main.py
```
Program çalıştırıldığında, belirtilen seri port üzerinden gelen verileri okuyacak ve ekrana "Pin" değerlerini yazdıracaktır.

## Programı Durdurma
Programı durdurmak için, terminalde CTRL+C tuş kombinasyonunu kullanabilirsiniz.
