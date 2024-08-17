from django.core.exceptions import ValidationError
from pathlib import Path


class MaxZiseFileValidator:

    def __init__(self, max_file_size):
        self.max_file_size = max_file_size

    def __call__(self, value):
        size = value.size
        ext_file = Path(str(value)).suffix

        max_size = self.max_file_size * 1048576
        if size > max_size:
            raise ValidationError(
                f"El archivo debe ser menor a {self.max_file_size} MB"
            )

        if ext_file != ".pdf":
            raise ValidationError(
                f" Los archivos con extensiones {ext_file} no son válidos "
            )


class MaxZiseImageValidator:

    def __init__(self, max_img_size):
        self.max_img_size = max_img_size

    def __call__(self, valuee):
        size = valuee.size
        max_size = self.max_img_size * 1048576
        if size > max_size:
            raise ValidationError(f"El archivo debe ser menor a {self.max_img_size} MB")
