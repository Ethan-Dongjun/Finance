from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

with webdriver.Chrome(ChromeDriverManager().install(), options=options) as driver:
    driver.get("https://securities.koreainvestment.com/main/mall/openels/EdlsInfo.jsp?cmd=TF02cc000000_Main")
    wait = WebDriverWait(driver, 20)
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe#ifrm_list")))
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body")))
    html = driver.page_source
    with open('iframe_source.html', 'w', encoding='utf-8') as f:
        f.write(html)
