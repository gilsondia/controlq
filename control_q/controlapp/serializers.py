from rest_framework import serializers
from controlapp.models import Control


class ControlSerializer(serializers.ModelSerializer):
    """
   Serializer for Control model
   """

    class Meta:
        """Meta"""

        model = Control
        fields = (
            "uuid",
            "name",
            "type",
            "rabi_rate",
            "polar_angle",
        )
