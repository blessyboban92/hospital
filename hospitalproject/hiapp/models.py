from django.db import models
class CategoryMaster(models.Model):
    categoryname = models.CharField(max_length=30)
    categorydescription = models.TextField()
    def __str__(self):
        return self.categoryname
class BrandMaster(models.Model):
    brandname = models.CharField(max_length=30)
    branddescription = models.TextField()
    def __str__(self):
        return self.brandname
class ItemMaster(models.Model):
    itemname=models.CharField(max_length=30)
    itemcode=models.CharField(max_length=10)
    category=models.ForeignKey(CategoryMaster,on_delete=models.CASCADE,null=True,default=None)
    salestax=models.IntegerField()
    mrp=models.IntegerField()
    barcode=models.CharField(max_length=10)
    hsncode=models.CharField(max_length=10)
    unit=models.CharField(max_length=15)
    brand = models.ForeignKey(BrandMaster, on_delete=models.CASCADE, null=True, default=None)
    purchasetax=models.IntegerField()
    def __str__(self):
        return self.itemname




