from .models import Post_request
from django import forms


class AddpostForm(forms.ModelForm):
    class Meta:
        model = Post_request
        fields = ('name', 'email', 'message')