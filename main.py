import math

from jinja2 import Environment, FileSystemLoader


def get_template_text(path):
    f_template = open(path, 'r', encoding='utf-8')
    html = f_template.read()
    f_template.close()
    return html


def write_static_from_template(path, tmp):
    f = open(path, 'w', encoding='utf-8')
    f.write(tmp)
    f.close()


def task_1():
    list_name = 'color'
    my_dict = {1: 'синий', 2: 'зеленый', 3: 'красный'}
    key = 2

    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('./template/test_template.html')

    result_html = template.render(name=list_name, my_dict=my_dict, key=key)

    write_static_from_template('./index.html', result_html)


def task_2(a_range, b_range, n):
    def f(x):
        return 5 * math.sin(x)

    def y(x):
        return 2 * math.cos(x)

    def generate_list(a, b):
        result = []
        for x in range(a, b + 1):
            result.append({"x": x, "f(x)": f(x), "y(x)": y(x)})
        return result

    def get_length(obj):
        return len(obj)

    def round_num(num):
        return math.floor(num)

    my_list = generate_list(a_range, b_range)

    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('./template/table_template.html')

    template.globals["get_length"] = get_length
    template.globals["round_num"] = round_num

    result_html = template.render(my_list=my_list, n=n)

    write_static_from_template('./index.html', result_html)


if __name__ == '__main__':
    # task_1()
    task_2(12, 30, 7)
