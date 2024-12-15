# TikTok Message Sender

Этот проект — Python скрипт, который автоматически отправляет сообщение списку друзей на TikTok каждое 24 часа.

## Требования

- Python 3.x
- [TikTokApi](https://github.com/davidteather/TikTok-Api)

Установите зависимость командой:

```bash
pip install TikTokApi
```

## Настройка

1. Создайте файл `config.py` и укажите свои данные для входа и список друзей:

   ```python
   username = 'your_username'
   password = 'your_password'

   friends = ['friend_user_id_1', 'friend_user_id_2']
   ```

2. Запустите скрипт:

   ```bash
   python main.py
   ```

Скрипт будет отправлять сообщение каждый день.

## Примечания

- Скрипт работает бесконечно, отправляя сообщение раз в 24 часа.
- Для повышения безопасности не храните данные в публичных репозиториях.

