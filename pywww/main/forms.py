from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, HTML, ButtonHolder
from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    send_to_me = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'contact_us'
        self.helper.add_input(Submit('submit', 'Wyślij'))

        # self.helper.layout = Layout(
        #     Fieldset('Dane kontaktowe', 'email'),
        #     Fieldset('Zawartość', 'title', 'content'),
        #     Fieldset('Dodatkowe',HTML("Zaznacz jeśli chcesz by wysłać kopię wiadomości do Ciebie"),'send_to_me',),
        #     ButtonHolder(Submit('submit', 'Wyślij', css_class='btn btn-primary'),css_class="d-flex justify-content-end")
        # )

