
import os
from dotenv import load_dotenv
from . import BASE_DIR
load_dotenv(os.path.join(BASE_DIR, '.env.sincehence'))
LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

IP_LOCATION_API = os.getenv('IP_LOCATION_API')

