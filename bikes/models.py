from django.db import models

# Create your models here.
class Bike(models.Model):
    name=models.CharField(max_length=100)
    tagline=models.CharField(max_length=200,default="Pure Motorcycling")
    engine_cc=models.IntegerField()
    power_hp=models.DecimalField(max_digits=5,decimal_places=2)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image_url=models.URLField(max_length=500)
    description=models.TextField()

    def __str__(self):
        return self.name

class TextRiderBooking(models.Model):
    bike=models.ForeignKey(Bike,on_delete=models.CASCADE)
    full_name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    preferred_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name}-{self.name}"

class BikeVariant(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE, related_name='variants')
    color_name = models.CharField(max_length=50) # उदा. Stealth Black, Fireball Red
    color_code = models.CharField(max_length=20, default="#000000") # HTML Color Code
    price_addition = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) # रंगाची अतिरिक्त किंमत (जर असेल तर)
    variant_image_url = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.bike.name} - {self.color_name}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"

