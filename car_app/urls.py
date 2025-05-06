from django.urls import path

from car_app import views, customer_views, owner_views, admin_views

urlpatterns = [
    path('',views.landing,name="landing"),
    path('admin_dashboard', views.admin_dashboard, name="admin_dashboard"),
    path('customer_dashboard',customer_views.customer_dashboard, name="customer_dashboard"),
    path('owner_dashboard', owner_views.owner_dashboard, name="owner_dashboard"),
    path("log_form",views.log_form,name="log_form"),
    path("owner_add", views.owner_add, name="owner_add"),
    path("customer_add", views.customer_add, name="customer_add"),
    path("login_view", views.login_view, name="login_view"),
    path("add_vehicle", owner_views.add_vehicle, name="add_vehicle"),
    path("vehicle_details", owner_views.vehicle_details, name="vehicle_details"),
    path("vehicle_view", customer_views.vehicle_view, name="vehicle_view"),
    path("book_vehicle/<int:id>/",customer_views.book_vehicle,name="book_vehicle"),
    path("update_vehicle/<int:id>/", owner_views.update_vehicle, name="update_vehicle"),
    path("delete_vehicle/<int:id>/",owner_views.delete_vehicle,name="delete_vehicle"),
    path("pay_now/<int:id>/", customer_views.pay_now, name="pay_now"),
    path('payment_view', customer_views.payment_view, name="payment_view"),
    path("booking_summary", customer_views.booking_summary, name="booking_summary"),
    path("cancel_booking/<int:id>/", customer_views.cancel_booking, name="cancel_booking"),
    path("my_booking", customer_views.my_booking, name="my_booking"),
    path("payment_tracking", customer_views.payment_tracking, name="payment_tracking"),
    path("invoice_view/<int:id>/", customer_views.invoice_view, name="invoice_view"),
    path('logout_view', views.logout_view, name="logout_view"),
    path("owner_booking_management", owner_views.owner_booking_management, name="owner_booking_management"),
    path('customer_details', admin_views.customer_details, name="customer_details"),
    path('owner_details', admin_views.owner_details, name="owner_details"),
    path('view_vehicle', admin_views.view_vehicle, name="view_vehicle"),
    path("delete_customer/<int:id>/",admin_views.delete_customer,name="delete_customer"),
    path("delete_owner/<int:id>/", admin_views.delete_owner, name="delete_owner"),
    path('payment_history', admin_views.payment_history, name="payment_history"),
    path("edit_customer_profile", customer_views.edit_customer_profile, name="edit_customer_profile"),
    path("customer_profile", customer_views.customer_profile, name="customer_profile"),
    path('invoice/<int:id>/download/', customer_views.download_invoice_pdf, name='download_invoice_pdf'),

]