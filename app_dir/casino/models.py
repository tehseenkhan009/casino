from django.db import models
from django.utils.translation import pgettext_lazy
from django.utils.timezone import now
from tinymce.models import HTMLField


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
        pgettext_lazy('Logo + Background', 'Logo + Background'),
        upload_to='backgrounds',
        null=True,
        blank=True
    )
    description = HTMLField(
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


class Country(models.Model):
    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name

    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=4, unique=True)
    name = models.CharField(max_length=255, unique=True)


class CountryUrl(models.Model):
    def __str__(self):
        return self.country.code + ' | ' + self.casino.name + ' | URL: ' + self.url[:30]

    class Meta:
        verbose_name = 'Casino Country'
        verbose_name_plural = 'Casino Countries'

    country = models.ForeignKey(
        Country,
        on_delete=None,
        null=True
    )
    casino = models.ForeignKey(
        Casino,
        on_delete=None,
        null=True
    )
    url = models.CharField(max_length=255, unique=True)


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
    counter = models.IntegerField(
        pgettext_lazy('Clicks', 'Clicks'),
        blank=True,
        null=True
    )
    rating_number = models.FloatField(
        pgettext_lazy('Rating', 'Rating'),
        blank=True,
        null=True,
        help_text='1.0 to 5.0'
    )
    bonus = models.ForeignKey(
        Bonus,
        on_delete=None,
        null=True
    )
    deal_url = models.CharField(
        pgettext_lazy('Deal Url', 'Deal Url'),
        max_length=600,
        null=True
    )
    url_country = models.ManyToManyField(CountryUrl, verbose_name='Countries', blank=True)
    free_spins = models.IntegerField(
        pgettext_lazy('Free Spins', 'Spins'),
        blank=True,
        null=True
    )
    wager = models.IntegerField(
        pgettext_lazy('Wager', 'Wager'),
        blank=True,
        null=True
    )
    deal_message = models.TextField(
        pgettext_lazy('Message', 'Message'),
        blank=True,
        null=True
    )
    deal_disclaimer = HTMLField(
        pgettext_lazy('Disclaimer', 'Disclaimer'),
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

    class Meta:
        verbose_name_plural = 'Deals'
