from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.db import models

invalid_format = "Invalid Format for Grad Year (YY-YY)"
grad_year_validator_format = RegexValidator("^[0-9]{2}-[0-9]{2}$",
                                            invalid_format,
                                            code="gradYear")


def grad_year_validator(year):
    message = ("Second Year Must be Sequential From the First "
               "(i.e 19-20 or 21-22)")
    grad_year_validator_format(year)
    year1, year2 = year.split("-")
    if int(year2) != ((int(year1) + 1) % 100):
        raise ValidationError(message=message, code="gradYear")


class GraduationYear(models.Model):
    gradYear = models.CharField("Graduation Year",
                                max_length=5,
                                primary_key=True,
                                validators=[grad_year_validator])

    class Meta:
        verbose_name_plural = "Graduation Years"
        app_label = "cs28"

    def __str__(self):
        return self.gradYear
