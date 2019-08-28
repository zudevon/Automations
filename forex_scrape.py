from selenium import webdriver
"""https://selenium-python.readthedocs.io"""


def investing_dot_com_scrape():
    driver = webdriver.Chrome()
    driver.get("https://www.investing.com/currencies/eur-usd-technical")
    summary = driver.find_element_by_class_name("summary")
    summary = summary.text
    MA_summary = driver.find_element_by_css_selector('span.redFont.bold.uppercaseText').text
    print("EUR-USD 5-HOUR", summary[8:19], "\nMoving Avg : ", MA_summary)

    driver.get("https://www.investing.com/currencies/usd-jpy-technical")
    summary = driver.find_element_by_class_name("summary")
    summary = summary.text
    print("USD-JPY 5-HOUR", summary[8:26], "\nMoving Avg : ", MA_summary)

    driver.get("https://www.investing.com/currencies/eur-jpy-technical")
    summary = driver.find_element_by_class_name("summary")
    summary = summary.text
    print("EUR-JPY 5-HOUR", summary[8:26], "\nMoving Avg : ", MA_summary)


def investing_dot_com_table_scrape():
    driver = webdriver.Chrome()
    driver.get("https://www.investing.com/technical/technical-summary")
    table = driver.find_element_by_class_name("technicalSummaryTbl").text
    print(table)

def inv_dc_MA_scrape(fs, ss):
    driver = webdriver.Chrome()


investing_dot_com_scrape()
# investing_dot_com_table_scrape()
