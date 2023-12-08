user_permissions = ['admin']

def check_permission(permission):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if permission in user_permissions:
                return func(*args, **kwargs)
            else:
                raise PermissionError(f"У пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}")
        return wrapper
    return decorator

@check_permission('admin')
def delete_site():
    print('Удаляем сайт')

@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')

delete_site()
add_comment()
