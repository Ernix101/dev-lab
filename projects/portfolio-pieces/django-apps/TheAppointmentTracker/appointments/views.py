from django.shortcuts import render
from datetime import date, timedelta
from collections import defaultdict
from django.shortcuts import render, redirect
from .models import Appointment


# Create your views here.
# ! CALENDAR PAGE VIEW
def calendar_view(request):
    today = date.today()
    todays_appointments = Appointment.objects.filter(start_time__date=today)
    today_display = date.today()

    # Get data from query param, default to current week
    week_param = request.GET.get('week')
    if week_param:
        start_of_week = date.fromisoformat(week_param)
    else:
        today = date.today()
        start_of_week = today - timedelta(days=today.weekday())   # Monday

    end_of_week = start_of_week + timedelta(days=6)

    # * confirming which week is current to display in the calendar
    is_current_week = (start_of_week == today - timedelta(days=today.weekday()))

    appointments = Appointment.objects.filter(
        start_time__date__gte=start_of_week,
        start_time__date__lte=end_of_week,
    ).select_related('patient', 'provider')

    appointments_by_day = defaultdict(list)
    for appt in appointments:
        day = appt.start_time.date()
        appointments_by_day[day].append(appt)

    # * Adding a set of pre-made days ie. Monday to Sunday for the rendered final list
    week_days = [start_of_week + timedelta(days=i) for i in range(7)]
    schedule = [(day, appointments_by_day.get(day, [])) for day in week_days]

    stats = {
        'total': todays_appointments.count(),
        'completed': todays_appointments.filter(status='completed').count(),
        'upcoming': todays_appointments.filter(status='scheduled').count(),
        'no_show': todays_appointments.filter(status='no_show').count(),
    }

    context = {
        'active_page': 'calendar',
        'appointments': appointments,
        'start_of_week': start_of_week,
        'end_of_week': end_of_week,
        'prev_week': start_of_week - timedelta(days=7),
        'next_week': start_of_week + timedelta(days=7),
        'is_current_week': is_current_week,
        'week_days': week_days,
        'today_display': today_display,
        'schedule': schedule,
        'stats': stats,
    }
    return render(request, 'appointments/calendar.html', context)


# ! DASHBOARD PAGE VIEW
def dashboard_view(request):
    context = {
        'active_page': 'dashboard',
    }
    return render(request, 'appointments/dashboard.html', context)

# ! PATIENTS PAGE VIEW
def patients_view(request):
    context = {
            'active_page': 'patients',
        }
    return render(request, 'appointments/patients.html', context)

# ! PROVIDERS PAGE VIEW
def providers_view(request):
    context = {
            'active_page': 'providers',
        }
    return render(request, 'appointments/providers.html', context)

# ! ANALYTICS PAGE VIEW
def analytics_view(request):
    context = {
            'active_page': 'analytics',
        }
    return render(request, 'appointments/analytics.html', context)

# ! PROFILE PAGE VIEW
def profile_view(request):
    context = {
            'active_page': 'profile',
        }
    return render(request, 'appointments/profile.html', context)
