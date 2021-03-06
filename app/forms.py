from django import forms
from .models import Item


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('sex','name','yubin','address','tel','memo')
        # fields = ('tel')
            # ('addres')
        widgets = {
                    'name': forms.TextInput(attrs={'placeholder':'わだ　にゃん太郎'}),
                    'tel': forms.TextInput(attrs={'placeholder':'1234567890'}),
                    # 'addres': forms.TextInput(attrs={'placeholder': '記入例：大阪府豊中市蛍池〇〇番地'}),
                    'yubin': forms.TextInput(attrs={'placeholder': '郵便番号'}),
                    # 'age': forms.NumberInput(attrs={'min':1}),
                    'sex': forms.RadioSelect(),
                    'address': forms.Textarea(attrs={'rows': 2, 'placeholder': '大阪府門真市門真1006番地'}),
                    'memo': forms.Textarea(attrs={'rows':4, 'placeholder':'記入例：乾杯はみかんジュースで'}),
                  }
