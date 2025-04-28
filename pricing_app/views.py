from django.http import JsonResponse
from .models import PricingConfig
from datetime import datetime

def calculate_price(request):
    if request.method == 'GET':
        distance = float(request.GET.get('distance', 0))  
        time_hours = float(request.GET.get('time_hours', 0))  
        waiting_minutes = int(request.GET.get('waiting_minutes', 0))  
        day_of_week = request.GET.get('day_of_week', datetime.now().strftime('%A')) 

        try:
            config = PricingConfig.objects.get(day_of_week=day_of_week, is_active=True)
        except PricingConfig.DoesNotExist:
            return JsonResponse({'error': 'No active pricing config found for this day.'}, status=404)

        # Calculate extra distance
        extra_distance = max(0, distance - config.distance_limit_km)
        distance_price = config.base_price + (extra_distance * config.additional_price_per_km)

        # Calculate time multiplier
        if time_hours <= 1:
            time_multiplier = config.multiplier_upto_1hr
        elif time_hours <= 2:
            time_multiplier = config.multiplier_1_to_2hr
        elif time_hours <= 3:
            time_multiplier = config.multiplier_2_to_3hr
        else:
            time_multiplier = config.multiplier_2_to_3hr  # After 3hr use same

        time_price = time_hours * time_multiplier

        # Calculate waiting charge
        extra_waiting = max(0, waiting_minutes - config.waiting_time_free_minutes)
        waiting_units = extra_waiting / config.waiting_charge_unit_minutes
        waiting_charge = waiting_units * config.waiting_charge_per_unit

        # Final price
        final_price = distance_price + time_price + waiting_charge

        return JsonResponse({
            'distance_price': round(distance_price, 2),
            'time_price': round(time_price, 2),
            'waiting_charge': round(waiting_charge, 2),
            'total_price': round(final_price, 2),
        })

    else:
        return JsonResponse({'error': 'Only GET method allowed.'}, status=400)
