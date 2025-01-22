# Auto forward message from Channel A to Channel B Telegram

## Bước 1: Tạo Telegram Bot
- Mở Telegram và search BotFather
- Gõ command `/newbot` để tạo bot mới và theo hướng dẫn
- Lưu API Token được cung cấp bởi BotFather

## Bước 2: Set up các quyền cần thiết
- Add bot vô Channel A như là member với quyền read messages.
- Add bot vô Channel B như là admin với quyền send messages.

## Bước 3: Cài đặt Python và thư viện cần thiết

Link download:
- https://www.python.org/downloads/

Cài đặt thư viện:
```sh
pip install python-telegram-bot
```

## Bước 4: Clone source về
```sh
git clone https://github.com/CuongDuong2710/auto_forward_telegram.git
```

## Bước 5: Truyền giá trị cho BOT Token lưu ở bước 1 và channel ID
```sh
BOT_TOKEN = xxx
CHANNEL_A_ID = xxx
CHANNEL_B_ID = xxx
```

## Bước 6:  Chạy lệnh run
```sh
python telegram_bot.py
```

### Cách lấy CHANNEL_ID của một channel
- Bỏ comment đoạn code

```sh
application.add_handler(MessageHandler(filters.ALL, log_message))
```

- Add bot vô channel (bước số 2), chạy lại lệnh run (bước 6). Khi channel có tin nhắn mới nhất, bot sẽ log ra thông tin có CHANNEL_ID

```sh
Update(channel_post=Message(channel_chat_created=False, chat=Chat(id=-100xxxxxxx, title='xxxx', type=<ChatType.CHANNEL>, username='xxxxx'), ...)

id=-100xxxxxxx => CHANNEL_ID
```