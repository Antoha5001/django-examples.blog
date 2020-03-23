from django import forms

class EmailSharePost(forms.Form):
	name = forms.CharField(max_length=50)
	email = forms.EmailField()
	# to = forms.EmailField()
	# content = forms.CharField(widget=forms.Textarea)