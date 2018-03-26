from django import forms
DRINKS = ((None,'Please select a drink type'),(1,'Mocha'),(2,'Espresso'),(3,'Latte'))
SIZES = ((None,'Please select a drink size'),('s','Small'),('m','Medium'),('l','Large'))

class DrinkForm(forms.Form):
    name = forms.ChoiceField(choices=DRINKS,initial=0)
    size = forms.ChoiceField(choices=SIZES,initial=0)
    aount = forms.ChoiceField(choices=[(None,'Amount of drinks')]+[(i, i) for i in range(1,10)])

