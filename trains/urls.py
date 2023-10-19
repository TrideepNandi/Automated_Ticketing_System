from django.urls import path
from django.conf import settings
from .views.BookSeat import BookSeatView
from .views.SearchTrain import SearchTrainView
from .views.CancelTicket import CancelTicketView
from .views.CheckPNR import CheckPNRStatusView
from .views.success_booking import success_booking
from .views.login import login
from .views.register import RegisterView
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static

urlpatterns = [
    # URL for the Search Train View
    path('search-train/', SearchTrainView.as_view(), name='search_train'),

    # URL for the Book Seat View (replace 'train_code' and 'class_code' with actual parameters)
    path('book-seat/<str:train_code>/<str:class_code>/', login_required(BookSeatView.as_view(), login_url='/login'), name='book_seat'),

    # URL for the Cancel Ticket View (replace 'pnr' with the actual parameter)
    path('cancel-ticket/<str:pnr>/', login_required(CancelTicketView.as_view(), login_url='/login'), name='cancel_ticket'),

    # URL for the Check PNR Status View (replace 'pnr' with the actual parameter)
    path('pnr-status/', CheckPNRStatusView.as_view(), name='pnr'),
    
    # URL for Registering an User
    path ('register/', RegisterView.as_view(), name = 'register'),

    #URL for Successful Booking Page
    path('success-booking/<str:pnr_no>', success_booking.as_view(), name='success_booking'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
