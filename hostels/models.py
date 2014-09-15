from django.contrib.gis.db import models
from django.utils import timezone
from autoslug import AutoSlugField
from easy_thumbnails.fields import ThumbnailerImageField

def image_upload_folder(instance, filename):
	return "hostels_images/%s" % (filename)

choices_name = (		
	('Sunrise', 'Sunrise'),
	('Muruguru', 'Muruguru'),
	('Greens', 'Greens'),
	('Kens', 'Kens'),
	('Catholic', 'Catholic'),
	('Alexandria', 'Alexandria'),
	('CongoBrazzaville', 'CongoBrazzaville'),
	('Whitehouse', 'Whitehouse'),
	('Shirikisho', 'Shirikisho'),
	('Mabatini', 'Mabatini'),
	('Phineas', 'Phineas'),
	('Ngamia', 'Ngamia'),
	('Legacy', 'Legacy'),
	('Mankan', 'Mankan'),
	('Verity', 'Verity'),
	('Mumford', 'Mumford'),

)

choices_type = (
	('Bed-sitter', 'Bed-sitter'),
	('Self-contained', 'Self-contained'),
	('Two-shairing', 'Two-shairing'),
	('Three-shairing', 'Three-shairing'),
	('Four-shairing', 'Four-shairing'),
	('Single', 'Single'),
	('Communal', 'CommunalRooms'),
	('Rentals', 'RentalsRooms'),
)

choices_price = (		
	('8500', 'Kshs.8500'),
	('7000', 'Kshs.7000'),
	('6000', 'Kshs.6000'),
	('5000', 'Kshs.5000'),
	('3500', 'Kshs.3500'),
	('2500', 'Kshs.2500'),
	('5000', 'DKUT'),
	('0000', 'Free'),
)


choice_place = (
	('Kimathi', 'Kimathi'),
	('NyeriView', 'NyeriView'),
	('Kamakwa', 'Kamakwa'),
	('Nyarifo', 'Nyarifo'),
	('Emabassy', 'Emabassy'),
	('NyeriTown', 'NyeriTown'),
	('Othaya', 'Othaya'),
	('Mweiga', 'Mweiga'),
	("King'ong'o", "King'ong'o"),			
)


class HostelsNY(models.Model):
	place = models.CharField("Place", max_length=50, choices =choice_place)
	name = models.CharField("Name of the Hostel", max_length=50, choices=choices_name)
	slug = AutoSlugField(populate_from='name', unique=True) 
	type = models.CharField("Type", max_length=70, choices=choices_type)
	price = models.CharField("Price per month [Kshs.]", max_length=25, choices=choices_price)
	wifi = models.BooleanField("WiFi", default=False)
	breakfast = models.BooleanField("Breakfast", default=False)
	description = models.TextField("Hostel Description", max_length= 5000)
	image = ThumbnailerImageField(upload_to=image_upload_folder, blank=True)
	geom = models.PointField(srid=4326)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Hostels in Nyeri"

