from selenium import webdriver
from time import sleep
my_driver = webdriver.Chrome()
my_driver.get("file:///Users/liavnefesh/PycharmProjects/DevOps2402/tip_calc/index.html")
my_driver.find_element_by_id("billamt").send_keys(100)
my_driver.find_element_by_id("peopleamt").send_keys(5)
my_driver.find_element_by_xpath("//*[@id=\"serviceQual\"]/option[4]").click()
my_driver.find_element_by_id("calculate").click()
total_tip = my_driver.find_element('id', "tip").text

expected = "3.00"
print(total_tip)
assert expected == total_tip


