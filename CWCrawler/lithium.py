from selenium import webdriver
from bs4 import BeautifulSoup
import time

url = "https://dragonflyenergy.com/category/batteries/"

# Sử dụng trình duyệt Selenium
driver = webdriver.Chrome()

try:
    driver.get(url)

    # Khoảng thời gian để trang web tải hoàn tất
    time.sleep(5)

    # Lấy nội dung của trang web sau khi đã tải hoàn tất
    page_source = driver.page_source

    # Sử dụng BeautifulSoup để phân tích nội dung HTML
    soup = BeautifulSoup(page_source, 'html.parser')

    # Tìm tất cả các thẻ <h5> có class là "post-title"
    post_titles = soup.find_all('h5', class_='post-title')

    # In ra các đường link của các bài viết
    for post_title in post_titles:
        post_link = post_title.find('a')  # Lấy thẻ <a> bên trong thẻ <h5>
        if post_link and 'href' in post_link.attrs:
            print(post_link['href'])

finally:
    # Đóng trình duyệt khi hoàn thành
    driver.quit()