from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


def validate_slug(value):
    if not value.isalnum() or '-' in value:
        raise ValidationError(
            'Slug can only contain alphanumeric characters and hyphens.',
            code='invalid_slug'
        )
