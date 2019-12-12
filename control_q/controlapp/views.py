from django.shortcuts import render
from rest_framework import viewsets
from controlapp.serializers import ControlSerializer
from controlapp.models import Control
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from django.http import HttpResponse
import csv
from controlapp.resources import ControlResource
from rest_framework.response import Response
from rest_framework import status
from tablib import Dataset


class LookupUuidView(object):
    """
        Set the lookup_url_kwarg, lookup_field, and lookup_value_regex
        to reasonable defaults for uuid enabled models
    """

    lookup_url_kwarg = "uuid"
    lookup_field = "uuid"
    lookup_value_regex = ("[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}")


class ControlViewSet(LookupUuidView, viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Control instances.

    """
    pagination_class = LimitOffsetPagination
    serializer_class = ControlSerializer
    queryset = Control.objects.all()

    @action(
        detail=False,
        methods=["post"],
        url_path="import",
        url_name="import",
        parser_classes=(MultiPartParser,),
    )
    def control_import(self, request, *args, **kwargs):
        """
        /import/

        end-point to import the controls file, the binary csf file parameter that is expecting if 'file'

        the end-point /template can provide a example of the CSV filet that this end-point is expecting.

        This import does not update items, and the column uuid needs to be empty in order to import safely.
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        control_resource = ControlResource()
        dataset = Dataset(headers=["uuid", "name", "type", "rabi_rate", "polar_angle"])
        new_controls = request.data.get("file")
        print("file={}".format(new_controls))
        # print("file_read={}".format(new_controls.read()))

        imported_data = dataset.load(new_controls.read().decode('utf-8'), format="csv")
        # dry run is the test of the import
        result = control_resource.import_data(dataset, dry_run=True)

        if result.has_errors():
            return Response(status=status.HTTP_400_BAD_REQUEST, data="CSV file cannot be imported")
        else:
            # no error, let's import them then
            control_resource.import_data(dataset, dry_run=False)
            return Response(status=status.HTTP_201_CREATED)

    @action(detail=False, methods=["get"], url_path="export", url_name="export")
    def control_export(self, request, *args, **kwargs):
        """
        /export/

        end-point to export the whole list of controls.
        im case of long list with more than 65000(or a bit more) rows, microsoft excell cannot open it.

        :param request:
        :param args:
        :param kwargs:
        :return: CSV file with all controls.
        """

        control_resource = ControlResource()
        dataset = control_resource.export()
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="controls.csv"'
        return response

    @action(detail=False, methods=["get"], url_path="template", url_name="template")
    def get_cvs_template(self, request, *args, **kwargs):
        """
        /template

        end-point that return an CSV template file with headers and 10 blank rows.
        :param request:
        :param args:
        :param kwargs:
        :return: CSV file
        """
        response = HttpResponse(content_type='text/csv')

        csv_file_name = "template_controls.csv"
        response["Content-Disposition"] = 'attachment; filename="{}"'.format(csv_file_name)
        writer = csv.writer(response)
        writer.writerow(["id", "uuid", "name", "type", "rabi_rate", "polar_angle"])
        for _ in range(10):
            writer.writerow(["", "", "", "", "", ""])
        return response

