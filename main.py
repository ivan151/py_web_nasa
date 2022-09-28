from pywebio import input, start_server
from pywebio import output
from funcs import translate_to_rus, get_earth_img, get_apod, get_items


def test():
    confirm = input.actions('Confirm to delete file?', ['confirm', 'cancel'],
                            help_text='Unrecoverable after file deletion')


def menu():
    choice = input.actions('МЕНЮ', [
        {'label': 'Поиск объектов', 'value': 'search'},
        {'label': 'Фото земли по дате', 'value': 'earth'},
        {'label': 'Обьект дня', 'value': 'apod'}
        # {'label': 'Cancel', 'type': 'cancel', 'color': 'danger'},
    ], help_text='Выбери, что ты хочешь посмотреть')

    if choice == "search":
        search()
    elif choice == "earth":
        earth()
    elif choice == "apod":
        apod()
    # action = info["action"]
    # if action == "apod":
    #     apod()
    # elif action == "earth":
    #     earth()
    # elif action == "search":
    #     search()

    # put_code('info = ' + json.dumps(info, indent=4))
    # if info is not None:
    #     save_user(info['username'], info['password'])
    #     if info['action'] == 'save_and_continue':
    #         add_next()


def earth():  # PyWebIO application function
    # Password input
    date = input.input("Введи дату", type=DATE)
    image = get_earth_img(date)
    #
    # # Drop-down selection
    # gift = input.select('Which gift you want?', ['keyboard', 'ipad'])
    #
    # # Checkbox
    # agree = input.checkbox("User Term", options=['I agree to terms and conditions'])
    #
    # # Single choice
    # answer = input.radio("Choose one", options=['A', 'B', 'C', 'D'])
    #
    # # Multi-line text input
    # text = input.textarea('Text Area', rows=3, placeholder='Some text')
    #
    # # File Upload
    # img = input.file_upload("Select a image:", accept="image/*")
    # output.put_text("hello", str(res))
    output.put_image(src=image, height="50%", width="50%")

    menu()


def search():
    search = input.input("Введи название космического обьекта")
    items = get_items(search_text=search)
    res = [[output.put_image(item.img)] for item in items]
    output.put_grid(res, cell_width='300px', cell_height='300px')

    menu()


def apod():
    data = get_apod()
    apod_desc = translate_to_rus(data["explanation"])
    apod_src = data["url"]
    output.put_image(src=apod_src)
    output.put_text(apod_desc)

    menu()


start_server(menu, host='0.0.0.0', port=8080, debug=True)
