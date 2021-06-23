from django import forms
from home.models import Person

class NameForm(forms.ModelForm):
	class Meta:
		model = Person
		fields = '__all__'