from django import template

register = template.Library()


@register.filter(name='num_celular')
def num_celular(num: str):
    return f'({num[:2]}){num[2:7]}-{num[7:]}'
