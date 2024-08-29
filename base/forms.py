from  .models import Item,Budget_title
from django.forms import ModelForm

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = (['title','item_name','quantity','price_per_item'])
        
class titleForm(ModelForm):
    
    class Meta:
        model = Budget_title
        fields = ("__all__") 
        

        
