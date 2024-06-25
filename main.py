import requests as rq
import logging
from requests.exceptions import RequestException, Timeout

# Настройка логирования для каждого файла
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

success_logger = logging.getLogger('success_logger')
success_handler = logging.FileHandler('success_responses.log')
success_handler.setLevel(logging.INFO)
success_handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
success_logger.addHandler(success_handler)
success_logger.propagate = False

bad_logger = logging.getLogger('bad_logger')
bad_handler = logging.FileHandler('bad_responses.log')
bad_handler.setLevel(logging.WARNING)
bad_handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
bad_logger.addHandler(bad_handler)
bad_logger.propagate = False

blocked_logger = logging.getLogger('blocked_logger')
blocked_handler = logging.FileHandler('blocked_responses.log')
blocked_handler.setLevel(logging.ERROR)
blocked_handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
blocked_logger.addHandler(blocked_handler)
blocked_logger.propagate = False

sites = ['https://www.youtube.com/', 'https://instagram.com', 'https://wikipedia.org', 'https://yahoo.com',
         'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com', 'https://amazon.com', 'https://tiktok.com',
         'https://www.ozon.ru']

for site in sites:
    try:
        response = rq.get(site, timeout=3)
        status_code = response.status_code
        if status_code == 200:
            success_logger.info(f"'{site}', response - {status_code}")
        elif 400 <= status_code < 600:
            bad_logger.warning(f"'{site}', response - {status_code}")
    except (RequestException, Timeout):
        blocked_logger.error(f"'{site}', NO CONNECTION")

print("Logging completed.")
