from django import forms


class LoginForm(forms.Form):
    
    username = forms.CharField(
        label='Username', max_length=150, required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'oroz...'})
    )
    
    password = forms.CharField(
        max_length=150, required=True, label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'your password' })
    )
    
