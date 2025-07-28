from django.shortcuts import render
import calendar 
from calendar import HTMLCalendar
from datetime import datetime

def home(request, year=datetime.now().year, month=datetime.now().strftime('%b')):
    name = "Ivan"
    month = month.capitalize()
    
    if month in calendar.month_name:
        month_number = list(calendar.month_name).index(month)
    elif month in calendar.month_abbr:
        month_number = list(calendar.month_abbr).index(month)
    #month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    cal = HTMLCalendar().formatmonth(year, month_number)

    now = datetime.now()
    current_year = now.year

    time = now.strftime('%I:%M %p')

    return render(request, 
        'myapp/home.html', {
        "name": name,
        "year": year,
        "month": month,
        "month_number": month_number,
        "cal": cal,
        "current_year": current_year,
        "time": time,
        })