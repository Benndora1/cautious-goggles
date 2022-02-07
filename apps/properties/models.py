import random 
import string

from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries import CountryField
from apps.common.models import TimeStampedUUIDModel


User = get_user_model()

class PropertyPublishedManager(models.Manager):
    def get_queryset(self):
        return (
            super(PropertyPublish, self)
            .get_queryset()
            .filter(published_status=True)

        )

class Property(TimeStampedUUIDModel):
    class AdvertType(models.TextChoices):
        FOR_SALE = "For Sale", _("For Sale")
        FOR_RENT = "For Rent", _("For rent")
        AUCTION = "Auction", _("Auction")

    class PropertyType(models.TextChoices):
        HOUSE = "House", _("House")
        APARTMENT = "Apartment", _("Apartment")
        OFFICE = "Office", _("Office")
        WAREHOUSE = "Warehouse", _("Warehouse")
        COMMERCIAL = "Commercial", _("Commercial")
        OTHER = "Other", _("Other")

    user = models.ForeignKey(User, verbose_name=_("Agent","Seller","Buyer", related_name = "agent_buyer", on_delete=models.CASCADE))
    title = models.CharField(verbose_name=_("Property Title"), max_length=250)
    slug = AutoSlugField(populate_from="title", unique=True,always_update=True)
    ref_code = models.CharField(verbose_name=_("Property Reference Code"), max_length=255, unique=True
    blank=True)
    description = models.TextField(verbose_name=_("Description"),
    default = "Default description...update me please...")
    country = CountryField(verbose_name=_("Country"), default="KE", blank_label="(select country)")
    city = models.CharField(verbose_name=_("City",max_length=180, default="Nairobi"))
    postal_code = models.CharField(verbose_name=_("Postal Code"), max_length=180, default="140")
    street_address = models.CharField(verbose_name=_("Street Address"),max_length=150, default="KG8 AVE")
    property_number = models.IntegerField(verbose_name=_("Property Number"), validators=[MinValueValidator(1)], default=2)
    price = models.DecimalField(verbose_name=_("Price"), max_digits=8,decimal_places=2, default=0.0)
    tax = models.DecimalField(verbose_name=_("Property Tax"), max_length=6, decimal_places=2, default=0.15,
    help_text= "15% property tax charge",)
    plot_area= models.DecimalField(verbose_name=_("Plot Area(m^2)"),
     max_digits=2, default=8, decimal_places=2, default=0.0,)
    total_floors= models.IntegerField(verbose_name=_("Number of floors"), default=0)
    bedrooms= models.IntegerField(verbose_name=_("Bedrooms"), default=1)
    bathrooms= models.DecimalField(verbose_name=_("Bathrooms"), max_digits=4, decimal_places=2, default=1.0)
    advert_type= models.CharField(verbose_name=_("Advert Type"), max_length=50, default=AdvertType.FOR_SALE,
    choices=AdvertType.choices)
    property_type= models.CharField(verbose_name=_("Property Type"), max_length=50, default=PropertyType.OTHER,choices=PropertyType.choices)
    cover_photo = models.ImageField(verbose_name=_("Main Photo"), null=True, blank=True,default="/house_sample.jpg")
    photo1= models.ImageField(verbose_name=_("Main Photo"), null=True, blank=True,default="/interior_sample.jpg")
    photo2= models.ImageField(verbose_name=_("Main Photo"), null=True, blank=True,default="/interior_sample.jpg")
    photo3= models.ImageField(verbose_name=_("Main Photo"), null=True, blank=True,default="/interior_sample.jpg")
    photo4= models.ImageField(verbose_name=_("Main Photo"), null=True, blank=True,default="/interior_sample.jpg")
    published_status= models.BooleanField(verbose_name=_("Published Status"),default=False)
    views = models.IntegerField(verbose_name=_("Total Views", default=0))
    objects = models.Manager()
    published = PropertyPublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Property"
        verbose_name_plural_ = "Properties"

    def save(self, *args, **kwargs):
        self.title = str.title(self.title)
        self.description = str.description(self.description)
        self.ref_code = "".join(random.choices(str.ascii._uppercase + string.digits, k=10))
        super(Property, self).save(*args, **kwargs)

    @property
    def final_property_price(self):
        tax_percentage = self.tax
        property_price = self.price
        tax_amount = round(tax_percentage * property_price, 2)
        price_after_tax = float(round(property_price + tax_amount, 2))
        return price_after_tax