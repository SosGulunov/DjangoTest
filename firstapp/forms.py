from django import forms


#class UserForm(forms.Form):
#    name = forms.CharField(label="Имя", initial="напиши имя дружище", max_length=20)
#    basket = forms.BooleanField(label="Ты лох?", required=False)
#    vyb = forms.NullBooleanField(label="Ты лох?")
#    age = forms.IntegerField(label="Введи возраст лошка")
#    email = forms.EmailField(label="Почта", initial="Loshped123@gmail.com")
#    ip = forms.GenericIPAddressField(label="IP адрес")
#    reg_text = forms.SlugField(label="Расскажи насколько ты лох")
#    url = forms.URLField(label="Твой сайт")
#    uuid_text = forms.UUIDField(label="Твой UUID")
#    file = forms.FileField(label="Выбери файл")
#    img = forms.ImageField(label="Загрузи фотку")
#    date = forms.DateField(label="Введи дату становления лошка лошком")
#    time = forms.TimeField(label="Введи время становления лошка лошком")
#    #date = forms.DateTimeField(label="Теперь все вместе")
#    choice = forms.ChoiceField(label="Выбери любимого героя в доте",choices=((1,"SF"),(2,"СФ"),(3,"shadow fiend")))

class UserForm(forms.Form):
    name = forms.CharField(label="Имя", initial="ФИО")
    age = forms.IntegerField(label="Возраст")
    required_css_class = "field"
    error_css_class = "error"
    





