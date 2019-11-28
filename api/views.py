from django.shortcuts import render
from .forms import BookingForm
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
	if request.method == 'POST':
		form = BookingForm(request.POST)
		if form.is_valid():
			departure = form.cleaned_data['departure']
			arrival = form.cleaned_data['arrival']
			departure_date = form.cleaned_data['departure_date']
			adult = form.cleaned_data['adultcount']

			q = Flight.objects.filter(departure=departure)
			q = q.filter(arrival=arrival)
			q = q.filter(date_of_departure=departure_date)
			print("====================================")
			print(departure)
			print(arrival)
			print(q)
			return render(request, 'api/flight-results-1 - Copy.html', {'flights':q})

	else:
		form = BookingForm()
	flights = Flight.objects.all
	temp = 'api/index2.html'
	ct = {'form':form, 'flights':flights}
	return render(request, temp, ct)

def flight_list(request):
	pass