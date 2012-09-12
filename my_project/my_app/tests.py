from django.core import management
from django.test import TestCase
from django.utils.unittest.case import expectedFailure
from haystack.inputs import Exact
from haystack.query import SearchQuerySet


class MyAppTestCase(TestCase):
    def setUp(self):
        management.call_command('rebuild_index', interactive=False, verbosity=0)

    @expectedFailure
    def test_exact_search(self):
        sqs = SearchQuerySet().filter(field=Exact('abc'))
        self.assertTrue('abc-de' not in [i.object.field for i in sqs])

    @expectedFailure
    def test_order_by(self):
        sqs1 = SearchQuerySet()
        sqs2 = sqs1.order_by('name')

        self.assertEqual(len(sqs1), len(sqs2))
