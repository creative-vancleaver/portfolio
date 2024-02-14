from django import forms

class ContactForm(forms.Form):
    
    name = forms.CharField(
        label='Your Name',
        max_length=100,
        required = True,
        widget = forms.TextInput(attrs={
            'class': 'form-control mb-3',
            # 'placeholder': 'Enter Your Name',
        })
    )
    email = forms.EmailField(
        label = 'Your Email',
        required = True,
        widget = forms.EmailInput(attrs={
            'class': 'form-control mb-3',
            # 'placeholder': 'Enter Your Email',
        })
    )
    subject = forms.CharField(
        label = 'Subject',
        max_length=100,
        required = True,
        widget = forms.TextInput(attrs={
            'class': 'form-control mb-3',
            # 'placeholder': 'Subject',
        })
    )
    message = forms.CharField(
        label = 'Message',
        required = True,
        widget = forms.Textarea(attrs={
            'class': 'form-control mb-3',
            # 'placeholder': 'Message',
        })
    )
    
    def clean_subject(self):
        subject = self.cleaned_data['subject']
        if not subject:
            subject = 'No Subject'
        return subject
    
    