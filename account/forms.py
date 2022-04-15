from django import forms
from .models import User

class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(ProfileForm, self).__init__(*args, **kwargs)
        if  not user.is_superuser:
            self.fields['username'].disabled = True
            self.fields['username'].help_text = None
            self.fields['Is_Author'].disabled = True
            self.fields['Special_User'].disabled = True
            self.fields['email'].disabled = True


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'Is_Author', 'Special_User', 'email']
