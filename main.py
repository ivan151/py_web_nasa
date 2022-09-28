from pywebio import input, start_server
from pywebio import output
from funcs import translate_to_rus, get_earth_img, get_apod, get_items


def test():
    confirm = input.actions('Confirm to delete file?', ['confirm', 'cancel'],
                            help_text='Unrecoverable after file deletion')


def background():
    html = """<html>
<head>
<style>
body {
  background-image: url('https://images.unsplash.com/photo-1608754482805-6f630357358b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=387&q=80');
}
</style>
</head>
<body>

<h2>Background Image</h2>

</body>
</html>
"""
    output.put_html(html)


def menu():
    # background()
    output.put_buttons([
        {'label': 'Поиск объектов', 'value': 'search'},
        {'label': 'Фото земли по дате', 'value': 'earth'},
        {'label': 'Обьект дня', 'value': 'apod'}
        # {'label': 'Cancel', 'type': 'cancel', 'color': 'danger'},
    ], onclick=click_res)


def click_res(action):
    if action == "apod":
        apod()
    elif action == "earth":
        earth()
    elif action == "search":
        search()


def earth():  # PyWebIO application function
    # Password input
    date = input.input("Введи дату", type=input.DATE)
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

def search():
    search = input.input("Введи название космического обьекта")
    items = get_items(search_text=search)
    res = [[output.put_image(item.img)] for item in items]
    output.put_grid(res, cell_width='300px', cell_height='300px')


def apod():
    data = get_apod()
    apod_desc = translate_to_rus(data["explanation"])
    apod_src = data["url"]
    output.put_image(src=apod_src)
    output.put_text(apod_desc)


start_server(menu, host='0.0.0.0', port=8080, debug=True)
