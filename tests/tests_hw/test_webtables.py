import time
from pages.tables import Tables
from components.components import WebElement



def test_tables(browser):
    page_tables = Tables(browser)
    page_tables.visit()

    # Проверка кнопки Add
    assert page_tables.btn_add.exist()

    # Открытие диалога
    page_tables.btn_add.click()
    time.sleep(1)
    assert page_tables.modal.visible()

    # Попытка сохранить пустую форму
    page_tables.btn_submit.click_force()
    time.sleep(1)
    assert page_tables.modal.visible()

    # Заполнение и сохранение
    test_data = {
        'first_name': 'Вадим',
        'last_name': 'Мазеин',
        'email': 'vadim@mail.com',
        'age': '38',
        'salary': '5000',
        'department': 'QA'
    }

    page_tables.first_name.send_keys(test_data['first_name'])
    page_tables.last_name.send_keys(test_data['last_name'])
    page_tables.email.send_keys(test_data['email'])
    page_tables.age.send_keys(test_data['age'])
    page_tables.salary.send_keys(test_data['salary'])
    page_tables.department.send_keys(test_data['department'])

    page_tables.btn_submit.click_force()
    time.sleep(1)

    # Проверка закрытия диалога
    assert page_tables.modal.is_closed(), "Модальное окно не закрылось"
    time.sleep(1)

    # Проверка новой записи
    assert page_tables.rows.find_text_in_table(test_data['first_name']), "Имя не найдено в таблице"

    # Редактирование
    target_row = None
    for row in page_tables.rows.find_elements():
        if test_data['email'] in row.text:
            target_row = row
            break
    page_tables.edit_btn.click()
    time.sleep(1)

    # Обновление данных
    page_tables.first_name.clear()
    page_tables.first_name.send_keys('Алексей')
    time.sleep(1)
    page_tables.btn_submit.click_force()

    assert 'Алексей' in page_tables.rows.get_text()
    time.sleep(1)

    # Удаление
    page_tables.delete_btn.click()
    time.sleep(1)
    assert 'Алексей' not in page_tables.rows.get_text()

    #ЗАДАНИЕ СО ЗВЁЗДОЧКОЙ
    page_tables.visit()

    #Устанавливаем 5 строк на странице
    page_tables.select_rows.select_by_value('5')
    time.sleep(1)

    # Проверка кнопок
    assert page_tables.btn_next.get_dom_attribute('disabled'), "Кнопка Next не заблокирована"
    assert page_tables.btn_prev.get_dom_attribute('disabled'), "Кнопка Previous не заблокирована"

    # Добавляем 3 записи
    test_data = [
        {'first_name': 'User1', 'last_name': 'Test1', 'email': 'user1@mail.com', 'age': '25', 'salary': '5000', 'department': 'Test1'},
        {'first_name': 'User2', 'last_name': 'Test2', 'email': 'user2@mail.com', 'age': '30', 'salary': '5000', 'department': 'Test2'},
        {'first_name': 'User3', 'last_name': 'Test3', 'email': 'user3@mail.com', 'age': '35', 'salary': '5000', 'department': 'Test3'}
    ]

    for data in test_data:
        page_tables.btn_add.click()
        time.sleep(1)
        # Заполнение формы
        page_tables.first_name.send_keys(data['first_name'])
        page_tables.last_name.send_keys(data['last_name'])
        page_tables.email.send_keys(data['email'])
        page_tables.age.send_keys(data['age'])
        page_tables.salary.send_keys(data['salary'])
        page_tables.department.send_keys(data['department'])
        page_tables.btn_submit.click_force()
        time.sleep(1)


    # Проверка появления 2-й страницы
    total_pages = int(page_tables.total_pages.get_text())
    assert total_pages > 1, f"Ожидалось больше 1 страницы, получено: {total_pages}"

    # Проверка кнопки Next
    assert not page_tables.btn_next.get_dom_attribute('disabled'), "Кнопка Next не активна"
    # Переход на следующую страницу
    page_tables.btn_next.click()
    time.sleep(1)

    # Проверка перехода на другую страницу
    assert page_tables.page_info.get_dom_attribute('value') != '1', "Номер страницы не изменился"
    # Проверка кнопки Previous
    assert not page_tables.btn_prev.get_dom_attribute('disabled'), "Кнопка Previous не активна"
    # Возврат на предыдущую страницу
    page_tables.btn_prev.click()
    time.sleep(1)
    # Проверка перехода на другую страницу
    assert page_tables.page_info.get_dom_attribute('value') != '2', "Номер страницы не изменился"
