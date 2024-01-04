from django import forms
g=[['Female','Female'],['Male','Male']]
c=[['Python','Python'],['Django','Django'],('SQL','SQL'),['Java','Java']]
class NameForm(forms.Form):
    Sname = forms.CharField()
    Sage = forms.IntegerField()
    #password = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)
    address = forms.CharField(widget = forms.Textarea(attrs= {'cols':10,'rows':5}))
    #gender = forms.ChoiceField(choices=g)#It will come in the form of dropdown list
    gender = forms.ChoiceField(choices=g,widget = forms.RadioSelect)#It will come in the form of radio buttons
    #course = forms.MultipleChoiceField(choices=c)#It will come in the form of dropdown list
    course = forms.MultipleChoiceField(choices=c,widget = forms.CheckboxSelectMultiple)



