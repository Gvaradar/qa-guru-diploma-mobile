import allure
from pages.main_page import MainPage


@allure.epic('Mobile тестирование')
@allure.feature('Wikipedia Android')
class TestWikipedia:

    @allure.story('Поиск')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Поиск статьи по запросу')
    def test_search_article(self, driver):
        main_page = MainPage(driver)
        main_page.click_search()
        main_page.enter_search_text('Python')
        main_page.assert_search_results_exist()

    @allure.story('Навигация')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Открытие настроек')
    def test_open_settings(self, driver):
        main_page = MainPage(driver)
        main_page.open_menu()
        main_page.open_settings()
        main_page.assert_settings_opened()

    @allure.story('Сохранение')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('Сохранение статьи в закладки')
    def test_save_article_to_bookmarks(self, driver):
        main_page = MainPage(driver)
        main_page.search_article('Python')
        main_page.open_article_menu()
        main_page.add_to_bookmarks()
        main_page.create_bookmark_folder('My Favorites')
        main_page.confirm_save_bookmark()
        main_page.open_bookmarks()
        main_page.assert_article_saved('Python')