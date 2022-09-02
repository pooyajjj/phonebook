from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class phonenum(models.Model):
    name = models.CharField(max_length = 200)
    phone_num = models.CharField (
        max_length = 30,
        validators = [
            RegexValidator(
                regex = '(\+989|9|09)(12|19|35|36|37|38|39|32|90|91|92|93|21|94|11|12|13|14|15|16|17|18|30|33|35|36|37|38|39|01|02|03|04|05|20|21|22|32|31|34)\d{7}',
                code = 'invalid_number'
            ),
        ]
    )

def __str__(self):
    return self.name
