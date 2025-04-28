from django import forms
from .models import PricingConfig

class PricingConfigForm(forms.ModelForm):
    class Meta:
        model = PricingConfig
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()

        base_price = cleaned_data.get('base_price')
        additional_price_per_km = cleaned_data.get('additional_price_per_km')
        multiplier_upto_1hr = cleaned_data.get('multiplier_upto_1hr')
        multiplier_1_to_2hr = cleaned_data.get('multiplier_1_to_2hr')
        multiplier_2_to_3hr = cleaned_data.get('multiplier_2_to_3hr')
        waiting_charge_per_unit = cleaned_data.get('waiting_charge_per_unit')

        errors = {}

        if base_price is not None and base_price < 0:
            errors['base_price'] = 'Base price must be positive.'

        if additional_price_per_km is not None and additional_price_per_km < 0:
            errors['additional_price_per_km'] = 'Additional price must be positive.'

        if multiplier_upto_1hr is not None and multiplier_upto_1hr <= 0:
            errors['multiplier_upto_1hr'] = 'Multiplier must be greater than 0.'

        if multiplier_1_to_2hr is not None and multiplier_1_to_2hr <= 0:
            errors['multiplier_1_to_2hr'] = 'Multiplier must be greater than 0.'

        if multiplier_2_to_3hr is not None and multiplier_2_to_3hr <= 0:
            errors['multiplier_2_to_3hr'] = 'Multiplier must be greater than 0.'

        if waiting_charge_per_unit is not None and waiting_charge_per_unit < 0:
            errors['waiting_charge_per_unit'] = 'Waiting charge must be positive.'

        if errors:
            raise forms.ValidationError(errors)

        return cleaned_data
