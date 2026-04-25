from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from blog.models import Post

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'categories']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Post title', 'class': 'form-input'}),
            'content': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Write your content...', 'class': 'form-input'}),
            'categories': forms.CheckboxSelectMultiple(),
        }