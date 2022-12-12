from django import forms
from .models import NippoModel,ImageUpload
#from bootstrap_datepicker_plus import DatePickerInput
#from django.contrib.admin.widgets import AdminDateWidget

class NippoModelForm(forms.ModelForm):
    class Meta:
        model = NippoModel
        exclude = ["user"]
        fields = "__all__"
 
    def __init__(self, user=None, *args, **kwargs):
        for field in self.base_fields.values():
            field.widget.attrs["class"] = "form-control"
            print(user,"__init__")
        self.user = user
        super().__init__(*args, **kwargs)
'''
    def save(self, commit=True):
        print(self.user,"------------------------------")
        nippo_obj = super().save(commit=False)
        print(commit,"------------------------------")
        if self.user:
            nippo_obj.user = self.user
        if commit:
            nippo_obj.save()
        return nippo_obj
'''        
class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUpload
        fields = "__all__"
'''
class NippoModelForm(forms.ModelForm):
    date = forms.DateField(
        label="作成日",
        widget=DatePickerInput(format='%Y-%m-%d')
    )

#フィールド全て
fields = "__all__"
#フィールドの一部
fields = ["フィールド1", "フィールド2"]
#一部のフィールドを除く
exclude = "user"
'''