from django.core.exceptions import ValidationError


def percentage(value):
    if not 0 <= value <= 100:
        raise ValidationError(f'{value} must be in [0,100].')