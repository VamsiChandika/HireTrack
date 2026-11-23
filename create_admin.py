import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = os.getenv("ADMIN_USERNAME")
email = ""
password = os.getenv("ADMIN_PASSWORD")

if not all([username, password]):
    raise ValueError("Admin environment variables are missing.")

if User.objects.filter(username=username).exists():
    print("Admin username already exists.")
else:
    admin = User.objects.create_superuser(
        username=username,
        email=email,
        password=password
    )
    admin.role = "ADMIN"
    admin.save()
    print("Admin account created successfully.")