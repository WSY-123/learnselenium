# 2019.2.28
# 获取前程无忧网上海地区python相关岗位信息
# 将结果导入xls文件
from selenium import webdriver
import xlrd
import xlwt
driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('https://www.51job.com/')

ele = driver.find_element_by_id('kwdselectid')

ele.send_keys('python')
ele = driver.find_element_by_id('work_position_input')
ele.click()

# 清除已选中选项
ele = driver.find_element_by_id('work_position_click_ip_location_000000_120500')
ele.click()

# 查找并点选上海
ele = driver.find_element_by_id('work_position_click_center_right_list_category_000000_020000')
ele.click()

# 保存选择结果
ele = driver.find_element_by_id('work_position_click_bottom_save')
ele.click()

# 搜索
ele = driver.find_element_by_css_selector('.ush button').click()

# 搜索结果分析
jobs = driver.find_elements_by_css_selector('#resultList div[class=el]')

for job in jobs:
    fields = job.find_elements_by_tag_name('span')
    stringFields = [field.text for field in fields]
    print('|'.join(stringFields))

# 创建excel对象
book = xlwt.Workbook()

# 增加一个sheet
sh = book.add_sheet('统计')

# 写入内容
row = 0
for job in jobs:
    fields = job.find_elements_by_tag_name('span')
    col = 0
    for field in fields:
        text = field.text
        sh.write(row,col,text)
        col += 1

    row += 1

#保存内容
book.save('D:\\51job.xls')
