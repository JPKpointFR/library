from selenium import webdriver


def test_my_website_is_online(live_server):
    '''Description détaillée du test.'''
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('window-size=1366x768')

    driver = webdriver.Chrome(
        executable_path='./tools/chromedriver.exe',
        options=chrome_options,
    )
    driver.get(live_server.url)
    print(driver.title)
    assert driver.title != "Not Found"
