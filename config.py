import os
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


api_key = os.environ.get('API_KEY')
group_id = os.environ.get('GROUP_ID')

