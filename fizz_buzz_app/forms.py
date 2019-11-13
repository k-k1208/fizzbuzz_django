from django import forms

class NumForm(forms.Form):
    num = forms.IntegerField(
        label='数値入力してな'#labelが効かない
    )
    comment = forms.CharField(
        label='コメント入力してな',
        max_length=200
    )
