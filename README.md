# Блогикум (1 часть).
## Блогикум (1 часть) <- этот репозиторий;
## Блогикум (2 часть) <- https://github.com/k0vvalski/blogicum-2pt;
## Блогикум (3 часть) <- https://github.com/k0vvalski/blogicum-3pt;
## Другие проекты (Яндекс Backend):
### CRUD для Yatube <- https://github.com/k0vvalski/api_yatube-module6;
### API для Yatube <- https://github.com/k0vvalski/api_final_yatube-module7.
## Технологии:
```
Python 3.11.0
Django 3.2.16
```
## Установка (macOS):
### 1. Клонирование репозитория
Откройте терминал и выполните команду: 
```
  git clone https://github.com/k0vvalski/blogicum-1pt.git
```
### 2. Переход в директорию проекта:
После клонирования перейдите в директорию проекта: 
```
  cd blogicum-1pt
```
### 3. Создание и активация виртуального окружения:
```
  python3.11 -m venv venv  
  source venv/bin/activate
```
### 4. Обновите pip:  
```
  python3.11 -m pip install --upgrade pip
```
### 5. Установка зависимостей:
```
  pip install -r requirements.txt
```
### 6. Перейти в папку проекта и запустить его:
```
  ./manage.py migrate  
  ./manage.py runserver
```
### 7. Перейти на локальный сервер:
```
  http://127.0.0.1:8000/
```
### 8. Перейти в панель администратора:
```
  http://127.0.0.1:8000/admin/  
```
