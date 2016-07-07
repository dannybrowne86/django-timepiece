from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Report(models.Model):
    """
    Captures the different types of reports available, primarily
    allowing for detailed control of permissions for each report type.
    """
    name = models.TextField(unique=True,
        help_text='The name of the report displayed to the user.')
    slug = models.SlugField(unique=True,
        help_text='An abbreviated name for the report.  Currently unused.')
    url_name = models.CharField(max_length=64, unique=True,
        help_text='The url name, when using the reverse function, will '
            'provide the path to execute the report.')
    nav_option = models.BooleanField(default=True,
        help_text='Should this report be listed in the Nav Bar?')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        permissions = (('view_report', 'Can view report.'),)

    def get_url(self, *args):
        return reverse(self.url_name, args=args)
