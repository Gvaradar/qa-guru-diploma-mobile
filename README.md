# Дипломный проект. Мобильная автоматизация

## 🚀 Проект: Тестирование мобильного приложения Wikipedia

Автотесты для мобильного приложения **Wikipedia**. Реализованы на **Python** с использованием **Appium** и **Pytest**.

Поддерживается локальный запуск на эмуляторе и удаленный запуск через **BrowserStack**.

## 🛠️ Используемый стек

- **Python** — язык написания тестов
- **Pytest** — фреймворк для запуска тестов
- **Appium** — автоматизация мобильных приложений
- **Allure** — отчеты (скриншоты, видео, логи)
- **BrowserStack** — облачный сервер для удаленного запуска


## 📁 Структура проекта
qa-guru-diploma-mobile/

├── config/ 

├── tests/ 

├── utils/ 

├── .env.local 

├── .env.browserstack 

├── .env.example 

├── requirements.txt 

└── README.md


## ⚙️ Установка и запуск
### Локальный запуск
1. Клонировать репозиторий:
   
   git clone https://github.com/Gvaradar/qa-guru-diploma-mobile.git
   cd qa-guru-diploma-mobile

2. Создать виртуальное окружение:
   
   python -m venv venv

   source venv/bin/activate  # для Linux/Mac
 
   venv\Scripts\activate     # для Windows

3. Установить зависимости:
   
   pip install -r requirements.txt

4. Запустить тесты:
  
   pytest tests/ -v --alluredir=allure_results


### Удаленный запуск (BrowserStack)

Для запуска через BrowserStack выполните:
   
   CONTEXT=browserstack pytest tests/ -v --alluredir=allure_results
   
## Allure отчет

Для просмотра отчета выполните:
   
   allure serve allure_results
   
## Тесты

- **test_search_article** — поиск статьи по запросу
- **test_open_settings** — открытие настроек приложения
- **test_save_article_to_bookmarks** — сохранение статьи в закладки

## Требования диплома
- ✅ Не менее 3 тестов
- ✅ 2 конфига (локальный и BrowserStack) через pydantic
- ✅ Файлы .env.local и .env.browserstack
- ✅ conftest.py с настройкой драйвера и вложениями
- ✅ Allure отчеты (скриншоты, HTML, видео)
- ✅ Закрытие сессии driver.quit()

