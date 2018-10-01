from decimal import Decimal as D

from django.core.exceptions import ValidationError
from django.test import TestCase
from izi.apps.dashboard.offers import forms
from izi.apps.offer.custom import create_benefit
from izi.apps.offer.models import Range, Benefit
from izi.test.factories import create_product

from tests._site.model_tests_app.models import CustomBenefitModel


class TestBenefitForm(TestCase):

    def setUp(self):
        self.range = Range.objects.create(
            name="All products", includes_all_products=True)
        self.prod = create_product()

    def test_init_without_custom_benefit(self):
        """
        If no custom benefit exists, the type field should be required.
        """
        form = forms.BenefitForm()
        self.assertTrue(form.fields['type'].required)

    def test_init_with_custom_benefit(self):
        """
        If a custom benefit exists, the type field should not be required.
        """
        create_benefit(CustomBenefitModel)
        form = forms.BenefitForm()
        self.assertFalse(form.fields['type'].required)
        self.assertEqual(form.fields['custom_benefit'].initial, None)

    def test_init_with_custom_benefit_with_instance(self):
        """
        If a custom benefit exists and the kwargs instance is passed to init, the initial value for the custom_benefit
        should be the instance.
        """
        benefit = create_benefit(CustomBenefitModel)
        form = forms.BenefitForm(instance=benefit)
        self.assertFalse(form.fields['type'].required)
        self.assertEqual(form.fields['custom_benefit'].initial, benefit.id)

    def test_is_valid_no_data(self):
        """
        If not data is supplied, is_valid should evaluate to false
        """
        form = forms.BenefitForm()
        self.assertFalse(form.is_valid())

    def test_clean_no_value_data(self):
        """
        If data is supplied without any values, the form should evaluate to not valid +
        and the clean method should throw a ValidationError
        """
        form = forms.BenefitForm(data={
            'range': '',
            'type': '',
            'value': '',
            'custom_benefit': ''
        })
        self.assertFalse(form.is_valid())
        self.assertRaises(ValidationError, form.clean)

    def test_clean_new_incentive(self):
        """
        If a range, type and value is supplied, the clean method should return the cleaned data without errors.
        """
        form = forms.BenefitForm(data={
            'range': self.range.id,
            'type': Benefit.FIXED,
            'value': 5,
            'custom_benefit': ''
        })

        self.assertTrue(form.is_valid())
        self.assertEqual({
            'range': self.range,
            'type': Benefit.FIXED,
            'value': D('5'),
            'custom_benefit': '',
            'max_affected_items': None
        }, form.clean())

    def test_clean_new_incentive_only_range(self):
        """
        If only a range is supplied, the clean method should throw a ValidationError.
        """
        form = forms.BenefitForm(data={
            'range': self.range.id,
            'type': '',
            'value': '',
            'custom_benefit': ''
        })
        self.assertFalse(form.is_valid())
        self.assertRaises(ValidationError, form.clean)

    def test_clean_validation_with_custom_benefit(self):
        """
        If a custom benefit is selected, the form should be valid.
        """
        benefit = create_benefit(CustomBenefitModel)

        form = forms.BenefitForm(data={
            'range': '',
            'type': '',
            'value': '',
            'custom_benefit': benefit.id
        })

        self.assertTrue(form.is_valid())
        self.assertEqual({
            'range': None,
            'type': '',
            'value': None,
            'custom_benefit': str(benefit.id),
            'max_affected_items': None
        }, form.clean())

    def test_clean_only_range_custom_exists(self):
        """
        If a custom benefit exists, the type field is not required. Still, the clean method should throw a
        ValidationError, if only the range is supplied.
        """
        create_benefit(CustomBenefitModel)

        form = forms.BenefitForm(data={
            'range': self.range,
            'type': '',
            'value': '',
            'custom_benefit': ''
        })

        self.assertFalse(form.is_valid())
        self.assertRaises(ValidationError, form.clean)

    def test_clean_validation_custom_exists(self):
        """
        If a custom benefit exists, and the data for range, type and value is supplied, the form should validate.
        Clean should return the cleaned data.
        """

        create_benefit(CustomBenefitModel)

        form = forms.BenefitForm(data={
            'range': self.range.id,
            'type': Benefit.FIXED,
            'value': 5,
            'custom_benefit': ''
        })

        self.assertTrue(form.is_valid())
        self.assertEqual({
            'range': self.range,
            'type': Benefit.FIXED,
            'value': D('5'),
            'custom_benefit': '',
            'max_affected_items': None
        }, form.clean())
