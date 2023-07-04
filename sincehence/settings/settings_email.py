import os
from dotenv import load_dotenv
from . import BASE_DIR
load_dotenv(os.path.join(BASE_DIR, '.env.sincehence'))
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT= os.getenv('EMAIL_PORT')
EMAIL_HOST_USER=os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD=os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS=False
EMAIL_USE_SSL=True
