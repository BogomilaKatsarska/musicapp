from django.core.exceptions import ValidationError


def contains_only_letters_numbers_and_underscore(value):
    for ch in value:
        if not ch.isalnum() and ch != '_':
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")