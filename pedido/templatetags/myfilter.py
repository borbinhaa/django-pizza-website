from django import template

register = template.Library()


@register.filter(name='money')
def money(num):
    return f'R$ {num:.2f}'.replace('.', ',')


print(round(2.132312, 2))
