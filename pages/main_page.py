from appium.webdriver.common.appiumby import AppiumBy
import allure


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    SEARCH_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')
    SEARCH_INPUT = (AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')
    RESULT_TITLE = (AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')
    MENU_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'Open navigation drawer')
    SETTINGS_OPTION = (AppiumBy.XPATH, '//*[@text="Settings"]')
    SETTINGS_TITLE = (AppiumBy.XPATH, '//*[@text="Settings"]')
    MORE_OPTIONS = (AppiumBy.ACCESSIBILITY_ID, 'More options')
    ADD_TO_BOOKMARKS = (AppiumBy.XPATH, '//*[@text="Add to bookmarks"]')
    CREATE_BOOKMARK_BUTTON = (AppiumBy.ID, 'org.wikipedia.alpha:id/create_bookmark_button')
    TEXT_INPUT = (AppiumBy.ID, 'org.wikipedia.alpha:id/text_input')
    OK_BUTTON = (AppiumBy.ID, 'android:id/button1')
    SNACKBAR_ACTION = (AppiumBy.ID, 'org.wikipedia.alpha:id/snackbar_action')
    MY_LISTS_OPTION = (AppiumBy.XPATH, '//*[@text="My lists"]')
    FAVORITES_FOLDER = (AppiumBy.XPATH, '//*[@text="My Favorites"]')

    @allure.step("Нажать на поле поиска")
    def click_search(self):
        self.driver.find_element(*self.SEARCH_BUTTON).click()
        return self

    @allure.step("Ввести текст для поиска: {text}")
    def enter_search_text(self, text):
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(text)
        return self

    @allure.step("Поиск (без автоматического клика): {text}")
    def search_for(self, text):
        self.click_search()
        self.enter_search_text(text)
        return self

    @allure.step("Проверить, что результаты поиска отображаются")
    def search_results_should_exist(self):
        results = self.driver.find_elements(*self.RESULT_TITLE)
        assert len(results) > 0
        return self

    @allure.step("Открыть меню")
    def open_menu(self):
        self.driver.find_element(*self.MENU_BUTTON).click()
        return self

    @allure.step("Выбрать настройки")
    def open_settings(self):
        self.driver.find_element(*self.SETTINGS_OPTION).click()
        return self

    @allure.step("Проверить, что открылась страница настроек")
    def settings_should_be_opened(self):
        assert self.driver.find_element(*self.SETTINGS_TITLE).is_displayed()
        return self

    @allure.step("Найти статью и открыть её: {text}")
    def search_article(self, text):
        self.click_search()
        self.enter_search_text(text)
        self.driver.find_element(*self.RESULT_TITLE).click()
        return self

    @allure.step("Открыть меню статьи")
    def open_article_menu(self):
        self.driver.find_element(*self.MORE_OPTIONS).click()
        return self

    @allure.step("Выбрать 'Add to bookmarks'")
    def add_to_bookmarks(self):
        self.driver.find_element(*self.ADD_TO_BOOKMARKS).click()
        return self

    @allure.step("Создать новую папку для закладок: {folder_name}")
    def create_bookmark_folder(self, folder_name):
        self.driver.find_element(*self.CREATE_BOOKMARK_BUTTON).click()
        self.driver.find_element(*self.TEXT_INPUT).send_keys(folder_name)
        self.driver.find_element(*self.OK_BUTTON).click()
        return self

    @allure.step("Подтвердить сохранение")
    def confirm_save_bookmark(self):
        self.driver.find_element(*self.SNACKBAR_ACTION).click()
        return self

    @allure.step("Открыть закладки")
    def open_bookmarks(self):
        self.open_menu()
        self.driver.find_element(*self.MY_LISTS_OPTION).click()
        self.driver.find_element(*self.FAVORITES_FOLDER).click()
        return self

    @allure.step("Проверить, что статья '{expected_title}' сохранена")
    def article_should_be_saved(self, expected_title):
        saved_article = self.driver.find_element(*self.RESULT_TITLE)
        assert saved_article.text == expected_title
        return self