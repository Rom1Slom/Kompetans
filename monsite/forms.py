from django import forms
from .models import Client

class ContactForm(forms.ModelForm):
     USER_CHOICES = [
        ('artisan', 'Artisan'),
        ('charge_affaires', 'Chargé d\'affaires'),
        ('bureau_etudes', 'En bureau d\'études'),
        # Ajoutez d'autres choix ici
    ]

     user_type = forms.MultipleChoiceField(
        choices=USER_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        required=False,
        label="Je suis",
    )

     class Meta:
        model = Client
        fields = ['nom', 'entreprise', 'email', 'telephone', 'message']
        widgets = {
            'nom': forms.TextInput(attrs={'id': 'nom', 'class': 'form-control', 'placeholder': 'Dupont'}),
            'entreprise': forms.TextInput(attrs={'id': 'entreprise','class':'form-control','placeholder': 'Ex : Renault'}),
            'email': forms.EmailInput(attrs={'id': 'email','class': 'form-control', 'placeholder': 'exemple@email.com'}),
            'telephone': forms.TextInput(attrs={'id': 'telephone','class': 'form-control', 'placeholder': '0601020304'}),
            'message': forms.Textarea(attrs={'id': 'message','class': 'form-control', 'rows': 4, 'placeholder': 'Votre message ici...'}),
            
              }
     def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        telephone = cleaned_data.get("telephone")

        if (not email) and (not telephone):
            raise forms.ValidationError("Veuillez renseigner au moins un moyen de contact (email ou téléphone).")

        return cleaned_data