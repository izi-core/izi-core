from http import client as http_client

from django.conf import settings
from django.urls import reverse
from django.utils.translation import gettext

from izi.apps.catalogue.models import Category
from izi.test.factories import create_product
from izi.test.testcases import WebTestCase


class TestProductDetailView(WebTestCase):

    def test_enforces_canonical_url(self):
        p = create_product()
        kwargs = {'product_slug': '1_wrong-but-valid-slug_1',
                  'pk': p.id}
        wrong_url = reverse('catalogue:detail', kwargs=kwargs)

        response = self.app.get(wrong_url)
        self.assertEqual(http_client.MOVED_PERMANENTLY, response.status_code)
        self.assertTrue(p.get_absolute_url() in response.location)

    def test_child_to_parent_redirect(self):
        """
        We test against separate view in order to isolate tested product
        detail view, since default value of `ProductDetailView.enforce_parent`
        property has changed. Thus, by default the view should not redirect
        to the parent page, but we need to make sure that original solution
        works well.
        """
        parent_product = create_product(structure='parent')
        kwargs = {'product_slug': parent_product.slug,
                  'pk': parent_product.id}
        parent_product_url = reverse('catalogue:parent_detail', kwargs=kwargs)

        child = create_product(
            title="Variant 1", structure='child', parent=parent_product)
        kwargs = {'product_slug': child.slug,
                  'pk': child.id}
        child_url = reverse('catalogue:parent_detail', kwargs=kwargs)

        response = self.app.get(parent_product_url)
        self.assertEqual(http_client.OK, response.status_code, response.location)

        response = self.app.get(child_url)
        self.assertEqual(http_client.MOVED_PERMANENTLY, response.status_code)


class TestProductListView(WebTestCase):

    def test_shows_add_to_basket_button_for_available_product(self):
        product = create_product(num_in_stock=1)
        page = self.app.get(reverse('catalogue:index'))
        self.assertContains(page, product.title)
        self.assertContains(page, gettext("Add to basket"))

    def test_shows_not_available_for_out_of_stock_product(self):
        product = create_product(num_in_stock=0)

        page = self.app.get(reverse('catalogue:index'))

        self.assertContains(page, product.title)
        self.assertContains(page, "Unavailable")

    def test_shows_pagination_navigation_for_multiple_pages(self):
        per_page = settings.IZI_PRODUCTS_PER_PAGE
        title = "Product #%d"
        for idx in range(0, int(1.5 * per_page)):
            create_product(title=title % idx)

        page = self.app.get(reverse('catalogue:index'))

        self.assertContains(page, "Page 1 of 2")


class TestProductCategoryView(WebTestCase):

    def setUp(self):
        self.category = Category.add_root(name="Products")

    def test_browsing_works(self):
        correct_url = self.category.get_absolute_url()
        response = self.app.get(correct_url)
        self.assertEqual(http_client.OK, response.status_code)

    def test_enforces_canonical_url(self):
        kwargs = {'category_slug': '1_wrong-but-valid-slug_1',
                  'pk': self.category.pk}
        wrong_url = reverse('catalogue:category', kwargs=kwargs)

        response = self.app.get(wrong_url)
        self.assertEqual(http_client.MOVED_PERMANENTLY, response.status_code)
        self.assertTrue(self.category.get_absolute_url() in response.location)