from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome()

# # 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
# wd.get('https://www.byhy.net/_files/stock1.html')
# # 根据id选择元素，返回的就是该元素对应的WebElement对象
# element = wd.find_element(By.ID, 'kw')
# # 通过该 WebElement对象，就可以对页面元素进行操作了
# # 比如输入字符串到 这个 输入框里
# # element.send_keys('通讯\n')
# # element.send_keys('通讯')
# # element = wd.find_element(By.ID, 'go')
# # element.click()

wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')
# 根据 class name 选择元素，返回的是 一个列表
# 里面 都是class 属性值为 animal的元素对应的 WebElement对象
elements = wd.find_elements(By.CLASS_NAME, 'animal')
# find_elements 返回的是找到的符合条件的 所有 元素 (这里有3个元素)， 放在一个 列表 中返回。
# 而如果我们使用 wd.find_element (注意少了一个s) 方法， 就只会返回 第一个 元素。

# 取出列表中的每个 WebElement对象，打印出其text属性的值
# text属性就是该 WebElement对象对应的元素在网页中的文本内容
for element in elements:
    print(element.text)

wd.quit()