from django import forms

Priority_choices = (
    ('', 'Please select:'),
    ('high', 'High'),
    ('medium', 'Medium'),
    ('low', 'Low'),
)

Type_choices=(
  ('private','Private'),
  ('public','Organization')
)

#for to edit the contact
class deleteEvent(forms.Form):
    event_title = forms.CharField(max_length=15, label='Event Title', widget=forms.TextInput(attrs={'class':'form-control'}))

#form for Calender
class calendarForm(forms.Form):
    
    event_title  = forms.CharField(max_length=15, label='Event Title', widget=forms.TextInput(attrs={'class':'form-control'}))
    description  = forms.CharField(max_length=140, label='Event Description', widget=forms.TextInput(attrs={'class':'form-control'}))
    priority     = forms.ChoiceField(choices=Priority_choices, label='Event Priority')


    
#form for login
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='Username', widget=forms.TextInput(attrs={'class':'form-control'}))    
    password = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'class':'form-control'}), label='Password')


#member form 
class MemberForm(forms.Form):
    full_name = forms.CharField(max_length=100, label='Full Name', widget=forms.TextInput(attrs={'class':'form-control'})) 
    username = forms.CharField(max_length=100, label='Username', widget=forms.TextInput(attrs={'class':'form-control'}))    
    contact = forms.CharField(label='Contact', widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'class':'form-control'}), label='Password')
    position = forms.CharField(max_length=100, label='Position', widget=forms.TextInput(attrs={'class':'form-control'}))


#form for sending multiple
class SendForm(forms.Form):
    name     = forms.CharField(max_length=15, label='Your Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    contacts = forms.CharField(label='Contacts(eg 2567xxxxxxxx, 2567xxxxxxx, ...)', widget=forms.TextInput(attrs={'class':'form-control'}))
    message  = forms.CharField(max_length=150, label='Message to send', widget=forms.Textarea(attrs={'class':'form-control'}))

#form for mail
class MailForm(forms.Form):
    subject    = forms.CharField(max_length=20, label='Subject', widget=forms.TextInput(attrs={'class':'form-control'}))
    email      = forms.EmailField(label='Your Email', widget=forms.TextInput(attrs={'class':'form-control'}))
    message    = forms.CharField(max_length=190, label='Message to send', widget=forms.Textarea(attrs={'class':'form-control'}))
    
#form for searching a phone Number
class TextSearchForm(forms.Form):
    query = forms.CharField(max_length=15, label='By name', widget=forms.TextInput(attrs={'class':'form-control'}))

#form class for credititng an account
class CreditForm(forms.Form):
    username    = forms.CharField(max_length=12, label='Account\'s Username', widget=forms.TextInput(attrs={'class':'form-control'}))
    amount_paid = forms.CharField(label="Amount Paid", widget=forms.TextInput(attrs={'class':'form-control'}))
  


#view for delete a phone number
class DeleteForm(forms.Form):
    name = forms.CharField(max_length=15, label='Username', widget=forms.TextInput(attrs={'class':'form-control'}))


#view for ContactForm
class PhoneBookForm(forms.Form):
    message = forms.CharField(max_length=150, label='Message', widget=forms.Textarea(attrs={'class':'form-control'}))
    

#form for phonebook
class BookForm(forms.Form):
    name    = forms.CharField(max_length=15, label='Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    contact = forms.CharField(label='Number(eg 2567xxxxxxxx)', widget=forms.TextInput(attrs={'class':'form-control'})) 
    group   = forms.CharField(label='Group', max_length=12, widget=forms.TextInput(attrs={'class':'form-control'}))

    
