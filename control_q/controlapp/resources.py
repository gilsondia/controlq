from import_export import resources
from controlapp.models import Control


class ControlResource(resources.ModelResource):
    """
    Resource for the Control model, which will help the import and export CSV files

    """

    class Meta:
        model = Control
        import_id_field = 'uuid'
        # import_id_fields = ('uuid',)
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
        # skip_unchanged = True
        report_skipped = True

    # def skip_row(self, instance, original):
    #     original_id_value = getattr(original, self._meta.import_id_field)
    #     instance_id_value = getattr(instance, self._meta.import_id_field)
    #     if original_id_value != instance_id_value:
    #         return True
    #     if not self._meta.skip_unchanged:
    #         return False
    #     for field in self.get_fields():
    #         try:
    #             if list(field.get_value(instance).all()) != list(field.get_value(original).all()):
    #                 return False
    #         except AttributeError:
    #             if field.get_value(instance) != field.get_value(original):
    #                 return False
    #     return True
