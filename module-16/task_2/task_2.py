callbacks = {}

def callback(route):
    def decorator(func):
        callbacks[route] = func
        return func
    return decorator

@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'

def app_get(route):
    return callbacks.get(route)

route = app_get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
