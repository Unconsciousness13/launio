from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy


def validate_min_notes(value):
    if value <= 0:
        raise ValidationError(
            gettext_lazy('%(value)La nota minima es 0'),
            params={'value': value},
        )
