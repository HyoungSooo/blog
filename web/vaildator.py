from django.core.exceptions import ValidationError


def check_the_code(value):
    check_code = '990418'
    if value != check_code:
        return ValidationError('코드가 일치하지않네요')
    return
