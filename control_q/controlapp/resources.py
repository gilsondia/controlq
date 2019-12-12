from import_export import resources
from import_export.results import RowResult
from controlapp.models import Control
from django.core.exceptions import ValidationError
from django.db.transaction import TransactionManagementError
from copy import deepcopy
import logging
import traceback


logger = logging.getLogger(__name__)
# Set default logging handler to avoid "No handler found" warnings.
logger.addHandler(logging.NullHandler())


class ControlResource(resources.ModelResource):
    """
    Resource for the Control model, which will help the import and export CSV files

    """

    class Meta:
        model = Control
        import_id_field = 'uuid'
        export_order = (
            "uuid",
            "name",
            "type",
            "rabi_rate",
            "polar_angle",
        )
        fields = (
            "uuid",
            "name",
            "type",
            "rabi_rate",
            "polar_angle",
        )
        report_skipped = True

