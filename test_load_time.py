import os
import sys
import time
import django

# Setup django environment
sys.path.append('d:/User/Downloads/My_kuda-to_ne_tyda_swernyli-main/My_kuda-to_ne_tyda_swernyli-main')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ttm_project.settings')
django.setup()

from django.test import Client
from django.contrib.auth.models import User

client = Client()
user = User.objects.first()
client.force_login(user)

start_time = time.time()
response = client.get('/tasks/create/')
end_time = time.time()

print(f"Status code: {response.status_code}")
print(f"Time taken: {end_time - start_time} seconds")
