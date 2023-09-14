from django.db import models


class carManager(models.Manager):
    """Manager for car data card"""
    
    def createCar (self, carBrand, carModel):
        """Create new car data card"""
        carProfile = self.model (carBrand=carBrand, carModel=carModel)
        
        carProfile.save(using=self._db)
        
        return carProfile


class carProfile(models.Model):
    """Database model for cars in the dealership"""
    carBrand = models.CharField(max_length=255)
    carModel = models.CharField(max_length=255)
    
    objects = carManager()
    
    REQUIRED_FIELDS = ['carBrand', 'carModel']
        
    def __str__(self):
        return self.carBrand
    
    