from pages.main_page import MainPage

def test_guest_can_see_login_page_elements(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    main_page = MainPage(browser, link)
    main_page.open()

    # переходим по ссылке — получаем Page Object LoginPage
    login_page = main_page.go_to_login_page()

    # красный тест → сначала специально ломаешь селектор (например, меняешь id),
    # запускаешь pytest, убеждаешься, что сообщение понятное,
    # затем возвращаешь правильный селектор. Ниже уже «зелёный» вариант:
    login_page.should_be_login_page()
