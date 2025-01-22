Bước 1: Tạo Telegram Bot
- Mở Telegram và search BotFather
- Gõ command /newbot để tạo bot mới và theo hướng dẫn
- Lưu API Token được cung cấp bởi BotFather

Bước 2: Set up các quyền cần thiết
- Add bot vô Channel A như là member với quyền read messages.
- Add bot vô Channel B như là admin với quyền send messages.

Bước3: Cài đặt Python và thư viện cần thiết
https://www.python.org/downloads/

```sh```
pip install python-telegram-bot
```sh```

or

```sh```
py-m pip install python-telegram-bot
```sh```

Bước  4: Clone source về
```sh```
git clone
```sh```

Bước 5: Truyền giá trị cho BOT Token lưu ở bước 1 và channel ID
```sh```
BOT_TOKEN = xxx
CHANNEL_A_ID = xxx
CHANNEL_B_ID = xxx
```sh```

Bước 6:  Chạy lệnh run
```sh```
python telegram_bot.py
```sh```

```sh```
py-m python telegram_bot.py
```sh```