from django import forms


class AddVotingForm(forms.Form):
    question = forms.CharField(max_length=500,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Ваш опрос'}))


class AddCommentForm(forms.Form):
    comment = forms.CharField(max_length=500,
                              required=True,
                              widget=forms.Textarea(attrs={'placeholder': 'Ваш комментарий'}))
