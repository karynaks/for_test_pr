"""
URL configuration for currency_server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views

    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from currency_server.views import *


urlpatterns = [
    path('', index),
    path('exchanges/one-day-rate/<str:currency>/<str:date>/', one_day_rate),
    path('exchanges/maximum-and-minimum/<str:currency>/<int:number_quotations>/', maximum_and_minimum_rates),
    path('buy-and-sell-rates/<str:currency>/<int:number_quotations>/', buy_and_sell_rates),
]
