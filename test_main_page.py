import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_add_to_basket_exist(browser):
    browser.get(link)
    time.sleep(3) #for testing
    #we cannot use the element search using 'value' because the language can change
    button_add_to_basket = browser.find_element_by_class_name('btn-add-to-basket')
    assert button_add_to_basket.is_displayed(), "There isn't button for adding goods to basket"