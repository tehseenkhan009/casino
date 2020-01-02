from django.db import models
from django.utils.translation import pgettext_lazy
from django.utils.timezone import now


class Casino(models.Model):
    name = models.CharField(
        pgettext_lazy('Casino field', 'name'),
        unique=True,
        max_length=128
    )
    is_disabled = models.BooleanField(blank=True, choices=((False, 'No'), (True, 'Yes')), default=False)
    is_recommended = models.BooleanField(blank=True, choices=((False, 'No'), (True, 'Yes')), default=False)
    logo = models.FileField(
        pgettext_lazy('Casino Logo', 'Logo'),
        upload_to='casinos',
        null=True,
        blank=True
    )
    url_casino = models.URLField(max_length=500, null=True, blank=True, default='https://')
    background = models.FileField(
        pgettext_lazy('Background', 'Background'),
        upload_to='backgrounds',
        null=True,
        blank=True
    )
    logo_background = models.FileField(
        pgettext_lazy('Logo+Background', 'LOGO + Background'),
        upload_to='backgrounds',
        null=True,
        blank=True
    )
    description = models.TextField(
        pgettext_lazy('Casino Description', 'description'),
        blank=True,
        null=True,
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

    def casino_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
        return 'user_{0}/{1}'.format(instance.user.id, filename)


class Bonus(models.Model):
    name = models.CharField(
        pgettext_lazy('Bonus name', 'name'),
        unique=True,
        max_length=128
    )
    percent = models.IntegerField(
        pgettext_lazy('Percent', 'percent'),
        null=True
    )
    price = models.IntegerField(
        pgettext_lazy('Price', 'Price'),
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        pgettext_lazy('Created', 'created at'),
        default=now,
        editable=False
    )
    updated_at = models.DateTimeField(
        pgettext_lazy('Updated', 'updated at'),
        default=now
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Bonuses'


class Deals(models.Model):
    def __str__(self):
        return self.casino.name + ' | Bonus: ' + self.bonus.name[:50]

    name = models.CharField(
        pgettext_lazy('Bonus name', 'name'),
        unique=True,
        max_length=128
    )
    is_disabled = models.BooleanField(blank=True, choices=((False, 'No'), (True, 'Yes')), default=False)
    casino = models.ForeignKey(
        Casino,
        on_delete=None,
        null=True
    )
    bonus = models.ForeignKey(
        Bonus,
        on_delete=None,
        null=True
    )
    created_at = models.DateTimeField(
        pgettext_lazy('Created', 'created at'),
        default=now,
        editable=False
    )
    updated_at = models.DateTimeField(
        pgettext_lazy('Updated', 'updated at'),
        default=now
    )

    order_id = models.IntegerField(
        pgettext_lazy('order_id', 'Order Id'),
        null=True,
        blank=True
    )

    class Meta:
        verbose_name_plural = 'Deals'
