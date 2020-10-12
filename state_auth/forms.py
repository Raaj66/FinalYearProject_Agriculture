from django import forms

class Auth_Form(forms.Form):
    email = forms.EmailField(max_length=60, widget=forms.TextInput(attrs={'placeholder': 'Enter your Email' ,'class':'input'}))
    password = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder': 'Enter your Pass','id':'form21' ,'class':'input'}))
    username = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={'placeholder': 'Enter your Username', 'id': 'form21', 'class': 'input'}))
    authid = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Enter your authid', 'id': 'form21', 'class': 'input'}))
    department = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Enter your Dept', 'id': 'form21', 'class': 'input'}))
    Pancard = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Enter your Gender', 'id': 'form21', 'class': 'input'}))
    crop = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Enter your Crop', 'id': 'form21', 'class': 'input'}))
    Address = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Enter your Adress', 'id': 'form21', 'class': 'input'}))
    Gender = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Enter your Gender', 'id': 'form21', 'class': 'input'}))
    phone = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Enter your Gender', 'id': 'form21', 'class': 'input'}))


class Auth_LoginForm(forms.Form):
    email = forms.EmailField(max_length=60, widget=forms.TextInput(attrs={'placeholder': 'Enter your Email' ,'class':'input'}))
    password = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder': 'Enter your Pass','id':'form21' ,'class':'input'}))


class First_Form(forms.Form):
    State = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'placeholder': 'Enter your State' ,'class':'input'}))
    District = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder': 'Enter your District','id':'form21' ,'class':'input'}))
    Crop = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={'placeholder': 'Enter your Crop', 'id': 'form21', 'class': 'input'}))
    Org=forms.FloatField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter Org_Value'}))
    Pred=forms.FloatField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter Predicted_Mean '}))


class Second_Form(forms.Form):
    Crop = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={'placeholder': 'Enter your Crop', 'id': 'form21', 'class': 'input'}))
    Gross_Production_Value_constant_2004_2006_1000_dollar=forms.FloatField(widget=forms.TextInput(
        attrs={'placeholder': 'Gross_Production_Value_constant_2004_2006_1000_dollar'}))
    Net_Production_Value_constant_2004_2006_1000_dollar=forms.FloatField(widget=forms.TextInput(
        attrs={'placeholder': 'Net_Production_Value_constant_2004_2006_1000_dollar'}))
    Gross_Production_Value_current_million_SLC=forms.FloatField(widget=forms.TextInput(
        attrs={'placeholder': 'Gross_Production_Value_current_million_SLC'}))
    Gross_Production_Value_constant_2004_2006_million_SLC = forms.FloatField(widget=forms.TextInput(
        attrs={'placeholder': 'Gross_Production_Value_constant_2004_2006_million_SLC'}))
    Gross_Production_Value_current_million_US_dollar = forms.FloatField(widget=forms.TextInput(
        attrs={'placeholder': 'Gross_Production_Value_current_million_US_dollar'}))




class Third_Form(forms.Form):
    crop = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={'placeholder': 'Enter your Crop', 'id': 'form21', 'class': 'input'}))
    production = forms.FloatField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter column prod'}))
    imports = forms.FloatField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter column export'}))
    exports = forms.FloatField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter column import'}))





