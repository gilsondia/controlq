from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid

class ControlType(object):
    CORPSE = "corpse"
    GAUSSIAN = "gaussian"
    CINBB = "cinbb"
    CINSK = "cinsk"


class Control(models.Model):
    """
    Controls that will control quantum computer input process

    This control documentation will explain how this model should be used

    """

    CONTROL_TYPE_CHOICES = (
        (ControlType.CORPSE, "CORPSE"),
        (ControlType.GAUSSIAN, "Gaussian"),
        (ControlType.CINBB, "CinBB"),
        (ControlType.CINSK, "CinSK"),
    )

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    name = models.CharField(
        max_length=32, help_text="The name of the control (e.g. “Single-Qubit Driven Control”)."
    )

    type = models.CharField(
        max_length=8,
        choices=CONTROL_TYPE_CHOICES,
        help_text="type of control "
    )

    rabi_rate = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        help_text="Integer in range between 0 and 100"
     )

    polar_angle = models.DecimalField(
        default=0,
        validators=[MaxValueValidator(1), MinValueValidator(0)],
        decimal_places=10,
        max_digits=11,
        help_text="Decimal Field in range between 0 and 1"
    )
