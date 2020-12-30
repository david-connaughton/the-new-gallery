from django.test import TestCase
from tours.forms import TourForm


class TestTourForm(TestCase):

    def test_this_form(self):
        form = TourForm({'tour': 'Wild Atlantic Way',
                        'date_preference': 'July',
                         'analogue_or_digital': 'Analogue',
                         'skill_level': 'Beginner',
                         'dietary_requirements': 'None',
                         'any_comments': 'No Comment'
                         })
        self.assertTrue(form.is_valid())
