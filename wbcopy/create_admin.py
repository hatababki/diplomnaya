import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wbcopy.settings')
django.setup()

from django.contrib.auth.models import User
from wbchina.models import User as CustomUser

def create_admin():
    username = input('Введите имя пользователя: ')
    email = input('Введите email: ')
    password = input('Введите пароль: ')
    
    try:
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True
        )
        
        custom_user = CustomUser.objects.create(
            user_ptr=user,
            role='admin',
            phone='',
            address=''
        )
        
        print(f'Администратор {username} успешно создан!')
    except Exception as e:
        print(f'Ошибка при создании администратора: {e}')

if __name__ == '__main__':
    create_admin() 