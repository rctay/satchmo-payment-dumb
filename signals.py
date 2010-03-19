import django.dispatch

"""
Sent when the user confirms a order (step 3) - but no payment has been made yet.
"""
pending_order_confirmed = django.dispatch.Signal()
