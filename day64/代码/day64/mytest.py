import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "day64.settings")
    import django
    django.setup()
    from app01 import models

    models.User.objects.all()