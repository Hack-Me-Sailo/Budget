from django.db import models

# Create your models here.
def get_total_price(a,b):
    return a*b

class Budget_title(models.Model):
    name = models.CharField(max_length=200,verbose_name='Budget Title')
    created= models.DateTimeField(auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now=True,null=True)
    def __str__(self) -> str:
        return self.name


class Item(models.Model):
    item_name = models.CharField(max_length=200)
    title = models.ForeignKey(Budget_title, on_delete=models.CASCADE,null=True)
    quantity = models.IntegerField()
    price_per_item = models.IntegerField()
    total_price = models.IntegerField(blank=True,null=True)
    created= models.DateTimeField(auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now=True,null=True)
    
    def save(self, *args, **kwargs):
        if not self.total_price:
            self.total_price = get_total_price(self.quantity,self.price_per_item)
        
        super().save(*args, **kwargs)
    def __str__(self) -> str:
        return f"{self.item_name}"
    