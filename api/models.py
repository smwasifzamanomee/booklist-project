from django.db import models

class category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class product(models.Model):
    category = models.ManyToManyField(category, related_name='category', blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    type = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class productLine(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    attributeValue = models.ManyToManyField('attributeValue', related_name='attributeValue', blank=True)
    price = models.DecimalField( max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=200)
    stock_quantity = models.IntegerField()
    
    def __str__(self):
        return self.sku

class productImage(models.Model):
    productLine = models.ForeignKey(productLine, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    alternative_text = models.CharField(max_length=200)
    url = models.ImageField(upload_to='products/')
    
    def __str__(self):
        return self.name

class attribute(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class attributeValue(models.Model):
    attribute = models.ForeignKey(attribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=200)
    
    def __str__(self):
        return self.value
    