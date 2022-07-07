from re import T
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = "https://twitter.com/i/flow/login"
ayarlar = "https://twitter.com/settings/your_twitter_data/account"
driver = webdriver.Firefox()
gmail = "https://accounts.google.com/signin/v2"

foxyproxy = "foxyproxy_standard-7.5.1.xpi"
driver.install_addon(foxyproxy, temporary=True)
driver.profile = webdriver.FirefoxProfile()
driver.profile.add_extension(foxyproxy)
driver.profile.set_preference("security.fileuri.strict_origin_policy", False)
driver.profile.set_preference("general.useragent.override", "userAgent=Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/101.0.4951.44 Mobile/15E148 Safari/604.1")
driver.profile.update_preferences()

driver.get(url)
a=input("asdddddddddd")
time.sleep(1)
driver.maximize_window()
#time.sleep(1)
proxytab = driver.window_handles[1]
asil_sayfa = driver.window_handles[0]
driver.switch_to.window(window_name=proxytab)
driver.close()
driver.switch_to.window(window_name=asil_sayfa)
time.sleep(1)
#bilgileri topla
kullanici_adi=input("Kullanıcı Adı: ")
sifre=input("Şifre: ")
yenimail=input("Yeni mail: ")
ready=input("Ready?")
#login
print("Kullanıcı adı giriliyor.")
kullanici_adi_type = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'text')))
kullanici_adi_type.send_keys(kullanici_adi)
time.sleep(1)
#ileri
ileri = driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div').click()
time.sleep(1)
#şifre gir
print("Şifre giriliyor.")
password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))
password.send_keys(sifre)
time.sleep(1)
#login ol
print("Giriş yapılıyor.")
loginbutton = driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div').click()
time.sleep(5)
driver.get(ayarlar)
#ayarlar ekranında şifre gir
print("Ayarlar ekranında şifre girilecek.")
ayarlarsifre = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'current_password')))
ayarlarsifre.click()
ayarlarsifre.send_keys(sifre)
time.sleep(1)
#onayla
print("Giriş yapılıyor.")
onayla = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div[4]/div').click()
time.sleep(2)
#phone'a tıkla
print("Telefona tıklanacak.")
phone=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div/a[2]/div/div/div/span').click()
time.sleep(3)
#telefon numarası kaldırma
try:
    #telefon numarası ekli ise onu silecek
    pass
except:
    #telefon ekli değilse geri gidiyoruz
    print("Telefon numarası bulunamadı, diğer işleme geçiliyor.")
    back=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/section[2]/div[1]/div/div/div/div/div[1]/div/div').click()
    time.sleep(1)
try:
    print("Telefon numarası bulunamadı, diğer işleme geçiliyor.")
    back=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/section[2]/div[1]/div/div/div/div/div[1]/div/div').click()
    time.sleep(1)
except:
    pass
#mail güncellemek için email'e tıklıyoruz.
print("Mail değişimine başlanıyor.")
maildegis=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div/a[3]/div/div').click()
time.sleep(1)
updatemail=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div/div[3]/a/div').click()
#tekrar şifre giriyoruz,
print("Mail değişimi için şifre girilecek.")
password2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))
password2.click()
password2.send_keys(sifre)
time.sleep(1)
#next
next=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div').click()
#yeni e-mail'i giriyoruz
print("Yeni mail adresi yazılacak.")
emailaddress = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'email')))
emailaddress.click()
emailaddress.send_keys(yenimail)
time.sleep(2)
#next
print("Mail adresi yazıldı kod için next'e tıklanacak.")
next2=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div').click()
time.sleep(5000)

#driver.find_element_by_xpath('').click()
driver.close()