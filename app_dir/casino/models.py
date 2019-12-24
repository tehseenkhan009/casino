from django.db import models
from django.utils.translation import pgettext_lazy
from django.utils.timezone import now


class Casino(models.Model):
    name = models.CharField(
        pgettext_lazy('Casino field', 'name'),
        unique=True,
        max_length=128
    )
    description = models.TextField(
        pgettext_lazy('Casino Description', 'description'),
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        pgettext_lazy('Casino Created', 'created at'),
        default=now,
        editable=False
    )
    updated_at = models.DateTimeField(
        pgettext_lazy('Casino Updated', 'updated at'),
        default=now
    )

    class Meta:
        app_label = 'casino'

    def __str__(self):
        return self.name
