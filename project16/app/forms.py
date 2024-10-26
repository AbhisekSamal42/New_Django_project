from django import forms

g=[['MALE','male'],['FEMALE','female']]
c=[('PYTHON','python'),('DJANGO','django'),('SQL','sql')]

class StudentForm(forms.Form):
    name=forms.CharField()
    id=forms.IntegerField()
    email=forms.EmailField()
    url=forms.URLField()
    password=forms.CharField(widget=forms.PasswordInput)
    address=forms.CharField(widget=forms.Textarea)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    course=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple())