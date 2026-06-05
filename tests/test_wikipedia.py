import allure
import pytest

from pages.main_page import MainPage


@allure.epic('Mobile тестирование')
@allure.feature('Wikipedia Android')
class TestWikipedia:

    @allure.story('Поиск')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Поиск статьи по запросу')
    @pytest.mark.parametrize('query', ['Python', 'Java', 'JavaScript'])
    def test_search_article(self, driver, query):
        main_page = MainPage(driver)
        main_page.search_for(query)
        main_page.search_results_should_exist()

    @allure.story('Навигация')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Открытие настроек')
    def test_open_settings(self, driver):
        main_page = MainPage(driver)
        main_page.open_menu()
        main_page.open_settings()
        main_page.settings_should_be_opened()

    @allure.story('Сохранение')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Сохранение статьи в закладки')
    @pytest.mark.parametrize('query', ['Python', 'Java'])
    def test_save_article_to_bookmarks(self, driver, query):
        main_page = MainPage(driver)
        main_page.search_article(query)
        main_page.open_article_menu()
        main_page.add_to_bookmarks()
        main_page.create_bookmark_folder('My Favorites')
        main_page.confirm_save_bookmark()
        main_page.open_bookmarks()
        main_page.article_should_be_saved(query)
