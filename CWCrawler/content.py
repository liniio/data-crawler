import requests
from bs4 import BeautifulSoup

url = "https://dragonflyenergy.com/how-dragonfly-energy-is-manufacturing-the-safest-batteries-on-the-market/"

# Thêm User-Agent vào headers để giả mạo trình duyệt web
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Gửi yêu cầu GET với headers
response = requests.get(url, headers=headers)

# Kiểm tra xem yêu cầu có thành công không (status code 200)
if response.status_code == 200:
    # Sử dụng BeautifulSoup để phân tích nội dung HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Tìm phần tử div có class là 'post-content'
    post_content_div = soup.find('div', class_='content-sidebar-wrap')

    if post_content_div:
        # Lấy tiêu đề bài viết
        title = soup.find('h1').text.strip()

        # Lấy mô tả bài viết (nếu có)
        description_tag = soup.find('meta', {'name': 'description'})
        description = description_tag['content'].strip() if description_tag else ''

        # Lấy nội dung bài viết
        content = ''
        content_tags = post_content_div.find_all(['p', 'h2', 'h3'])
        for tag in content_tags:
            content += tag.text.strip() + '\n'

        # In kết quả bằng tiếng Việt
        print("Tiêu đề:", title)
        print("Mô tả:", description)
        print("Nội dung:")
        print(content)

    else:
        print("Không tìm thấy phần tử 'post-content' trên trang web.")

else:
    print("Yêu cầu không thành công. Mã trạng thái:", response.status_code)
