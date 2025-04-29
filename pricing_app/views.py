from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import PricingConfig
from datetime import datetime

@csrf_exempt
def calculate_price(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            distance = float(data.get('distance', 0))
            time_hours = float(data.get('time_hours', 0))
            waiting_minutes = int(data.get('waiting_minutes', 0))
            day_of_week = data.get('day_of_week', datetime.now().strftime('%A'))

            try:
                config = PricingConfig.objects.get(day_of_week=day_of_week, is_active=True)
            except PricingConfig.DoesNotExist:
                return JsonResponse({'error': 'No active pricing config found for this day.'}, status=404)

            extra_distance = max(0, distance - config.distance_limit_km)
            distance_price = config.base_price + (extra_distance * config.additional_price_per_km)

            multipliers = config.time_multipliers or {}
            if time_hours <= 1:
                time_multiplier = multipliers.get('upto_1hr', 1)
            elif time_hours <= 2:
                time_multiplier = multipliers.get('1_to_2hr', 1)
            elif time_hours <= 3:
                time_multiplier = multipliers.get('2_to_3hr', 1)
            else:
                time_multiplier = multipliers.get('2_to_3hr', 1)

            time_price = time_hours * time_multiplier

            extra_waiting = max(0, waiting_minutes - config.waiting_time_free_minutes)
            waiting_units = extra_waiting / config.waiting_charge_unit_minutes
            waiting_charge = waiting_units * config.waiting_charge_per_unit

            total_price = distance_price + time_price + waiting_charge

            return JsonResponse({
                'distance_price': round(distance_price, 2),
                'time_price': round(time_price, 2),
                'waiting_charge': round(waiting_charge, 2),
                'total_price': round(total_price, 2)
            })

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Only POST method allowed.'}, status=405)
