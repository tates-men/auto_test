from selenium import webdriver
import time
import logging
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#Настройка логирования
logging.basicConfig(filename='test-results.log', format='%(asctime)s %(levelname)s: %(message)s', level=logging.INFO)


url = "https://spb.hh.ru/"
try:
    driver.get(url=url)
    logging.info("1. Start test Авторизация с помощью почты и пароля используя целевой Браузер")
    #Кнопка
    button_kod = driver.find_elements(By.CLASS_NAME, 'supernova-button')[1]
    button_kod.click()
    logging.info('"Button on" clicked')
    now_url = driver.current_url
    if now_url=='https://spb.hh.ru/account/login?backurl=%2F&hhtmFrom=main':
        logging.info('Translate Okey')
    else: logging.error('Translate not okey')

   #Заполнение логина
    time.sleep(1)
    email_input = driver.find_element(By.NAME,'login')
    email_input.clear()
    email_input.send_keys("john_tates@mail.ru")
    logging.info('Mail enter okey')
    #Нажатие на кнопку "вход с паролем"
    button_vhod_with_password = driver.find_elements(By.CLASS_NAME, 'bloko-link_pseudo')[1]
    time.sleep(4)
    button_vhod_with_password.click()
    logging.info('Button vhod with password" clicked')
    time.sleep(5)
    #Заполнение пароля
    password_input = driver.find_elements(By.CLASS_NAME, 'bloko-input-text')[2]
    password_input.clear()
    logging.info("cleared")
    password_input.send_keys("16072002El")
    logging.info("send")
    time.sleep(1)
    logging.info('Password entered')
    #Нажатие на кнопку "Войти"
    button_enter = driver.find_elements(By.CLASS_NAME, 'bloko-button')[3]
    time.sleep(2)
    button_enter.click()
    logging.info('Button Enter was clicked')
    time.sleep(2)
    #Проверка страницы
    now_url = driver.current_url
    if now_url=='https://spb.hh.ru/?hhtmFrom=account_login':
        logging.info('Translate to account_login Okey')
    else: logging.error('Translate not okey')
    time.sleep(1)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
