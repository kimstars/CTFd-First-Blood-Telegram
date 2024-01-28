# CTFd First Blood Telegram

# ⚠️ Notice ⚠️
Tôi sửa từ con bot Discord của ông anh ```https://github.com/jordanbertasso/CTFd-First-Blood-Discord ```sang bot Telegram cho dễ dùng 
---



## Usage
1. Vào https://t.me/BotFather để tạo Bot telegram
    sau đó lấy được access_token của con bot có dạng là xxxxxxx:xxxxx-xxxxxxxxxxxxx
    Rồi tiếp theo, thêm con bot vừa tạo vào một group chat 
    Lấy id group chat tại https://api.telegram.org/bot{token}/getUpdates lấy giá trị message_id nhé. sẽ có dạng kiểu -100034534523 


2. Tạo CTFd token của Admin : có chức năng truy cập API để lấy kết quả các challenge nhé

3. Cập nhật `config.py`:
    - HOST : địa chỉ trang CTFd của bạn (nhớ là có cả port nếu có)
    - API_TOKEN : token ctd vừa tạo ở bước 2. có dạng "ctfd_dsfasfsdfklasfkjldsf"
    - Sửa lại đoạn thông báo nếu cần
    - ANNOUNCE_ALL_SOLVES = True để thông báo tất cả các solves của user


4. Có thể chạy bằng để tự tạo docker và chạy
    ```
    make run
    ```
    Hoặc bạn có thể dùng tmux để treo lệnh
    ```
    python3 main.py
    ```

    - Trước khi chạy nhớ tạo thư mục data trong thư mục ./ctfd-first-blood-tele
    - Khi cần reset hay xóa file .db trong thư mục data
    - À mà đầu tiên nhớ ```pip install -r requirement.txt```


Cảm ơn và xin một start nhé !!