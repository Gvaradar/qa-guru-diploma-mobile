import allure
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import load_config


@allure.epic('Mobile тестирование')
@allure.feature('Wikipedia Android')
class TestWikipedia:

    @allure.story('Поиск')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Поиск статьи по запросу')
    def test_search_article(self, driver):
        with allure.step('Нажать на поле поиска'):
            driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia').click()

        with allure.step('Ввести текст для поиска'):
            search_input = driver.find_element(AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')
            search_input.send_keys('Python')

        with allure.step('Проверить, что результаты поиска отображаются'):
            results = driver.find_elements(AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')
            assert len(results) > 0

    @allure.story('Навигация')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Открытие настроек')
    def test_open_settings(self, driver):
        with allure.step('Открыть меню'):
            driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Open navigation drawer').click()

        with allure.step('Выбрать настройки'):
            driver.find_element(AppiumBy.XPATH, '//*[@text="Settings"]').click()

        with allure.step('Проверить, что открылась страница настроек'):
            assert driver.find_element(AppiumBy.XPATH, '//*[@text="Settings"]').is_displayed()

    @allure.story('Сохранение')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Сохранение статьи в закладки')
    def test_save_article_to_bookmarks(self, driver):
        with allure.step('Найти статью'):
            driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia').click()
            driver.find_element(AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text').send_keys('Python')
            driver.find_element(AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title').click()

        with allure.step('Открыть меню статьи'):
            driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'More options').click()

        with allure.step('Выбрать "Add to bookmarks"'):
            driver.find_element(AppiumBy.XPATH, '//*[@text="Add to bookmarks"]').click()

        with allure.step('Создать новую папку'):
            driver.find_element(AppiumBy.ID, 'org.wikipedia.alpha:id/create_bookmark_button').click()
            driver.find_element(AppiumBy.ID, 'org.wikipedia.alpha:id/text_input').send_keys('My Favorites')
            driver.find_element(AppiumBy.ID, 'android:id/button1').click()

        with allure.step('Подтвердить сохранение'):
            driver.find_element(AppiumBy.ID, 'org.wikipedia.alpha:id/snackbar_action').click()

        with allure.step('Проверить, что статья сохранена'):
            driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Open navigation drawer').click()
            driver.find_element(AppiumBy.XPATH, '//*[@text="My lists"]').click()
            driver.find_element(AppiumBy.XPATH, '//*[@text="My Favorites"]').click()
            saved_article = driver.find_element(AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')
            assert saved_article.text == 'Python'