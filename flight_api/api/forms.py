from django import forms

Tavel_Class_Options = [
    ('First', 'First'),
    ('Economy', 'Economy'),
    ('Premium', 'Premium'),
    ('Business', 'Business'),
]

Trip_Type_Options = [
    ('roundtrip', "roundtrip"),
    ('oneway', "oneway"),
]

Count_Options = [
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10),
]
Adult_Count_Options = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10),
]
Departure_Option = [
	("label", "City or airport"),
	("Abuja", "Abuja (ABV)"),
    ("Accra", "Accra (ACC)"),
    ("Ahmedabad", "Ahmedabad (AMD)"),
    ("Akure", "Akure (AKR)"),
    ("Almaty", "Almaty (ALA)"),
    ("Amman", "Amman (AMM)"),
    ("Asaba", "Asaba (ABB)"),
    ("Baku", "Baku (GYD)"),
    ("Bangalore", "Bangalore (BLR)"),
    ("Banjul", "Banjul (BJL)"),
    ("Beirut", "Beirut (BEY)"),
    ("Benin", "Benin (BNI)"),
    ("Enugu", "Enugu (ENU)"),
    ("Kaduna", "Kaduna (KAD)"),
    ("Kano", "Kano (KAN)"),
    ("Lagos", "Lagos (LOS)"),
    ("Owerri", "Owerri (QOW)"),
    ("Port Harcourt", "Port Harcourt (PHC)"),
    ("Uyo", "Uyo (QUO)"),
    ("Warri", "Warri (QRW)"),
    ("YOL", "Yola (YOL)"),
]

Arrival_Option = [
	("label", "Flyning to"),
]


class BookingForm(forms.Form):
    trip_type = forms.CharField(label='Enter Trip Type', widget=forms.Select(choices=Trip_Type_Options, attrs={'class':'off'} ))
    departure = forms.CharField(label='Enter Departure Location', widget=forms.Select(choices=Departure_Option, attrs={"class":"form-control"} ))
    arrival = forms.CharField(label='Enter Arrival Location', widget=forms.Select(choices=Arrival_Option, attrs={"class":"form-control"} ))
    departure_date = forms.DateField(widget=forms.DateInput(format='%m/%d/%Y', attrs={'class': 'form-control'}),input_formats=('%d/%m/%Y', ))
    return_date = forms.DateField(widget=forms.DateInput(format='%m/%d/%Y', attrs={'class': 'form-control'}),input_formats=('%d/%m/%Y', ), required=False)
    adultcount = forms.IntegerField(label='Enter Adult Count', widget=forms.Select(choices=Adult_Count_Options, attrs={"class":"form-control"} ))
    child_count = forms.IntegerField(label='Enter Child Count', widget=forms.Select(choices=Count_Options, attrs={"class":"form-control"} ))
    infant_count = forms.IntegerField(label='Enter Infant Count', widget=forms.Select(choices=Count_Options, attrs={"class":"form-control"} ))
    travel_class = forms.CharField(label='Enter Travel Class', widget=forms.Select(choices=Tavel_Class_Options, attrs={"class":"form-control"} ))

    def clean_departure(self):
    	data = self.cleaned_data['departure']
    	if(data == "label"):
    		raise forms.ValidationError('You have to select departure')
    	return data

    def clean_arrival(self):
    	data = self.cleaned_data['arrival']
    	if(data == "label"):
    		raise forms.ValidationError('You have to select arrival')
    	return data

    def clean_return_date(self):
    	data = self.cleaned_data
    	trip_type_data = self.cleaned_data['trip_type']
    	if(trip_type_data == "roundtrip" and not data['return_date']):
    		raise forms.ValidationError('You have to select return date for a round trip')
    	return data
