import django_tables2 as tables

from files.models import File


class FileTable(tables.Table):
    preview = tables.TemplateColumn('<img src="{{record.file.url}}" class="img-fluid" height="25" width="25">')

    class Meta:
        model = File
        orderable = False
