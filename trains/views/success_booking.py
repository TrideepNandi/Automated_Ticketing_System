from urllib import request
from django.shortcuts import render, HttpResponse
from trains.models import TicketReservation
from django.views import View

class success_booking(View):
    def get (self, request, pnr_no):
        try:
            ticket = TicketReservation.objects.get(PNR_no=pnr_no)
            return render(request, 'trains/success_booking.html', {'ticket': ticket})
        
        except TicketReservation.DoesNotExist:
            return HttpResponse('Ticket not found.')  # Handle the case where the PNR is not found