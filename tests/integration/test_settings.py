from django.test import TestCase
from django.template import loader, TemplateDoesNotExist

import izi


class TestIZICoreAppsList(TestCase):

    def test_includes_izi_itself(self):
        core_apps = izi.IZI_CORE_APPS
        self.assertTrue('izi' in core_apps)

    def test_can_be_retrieved_through_fn(self):
        core_apps = izi.get_core_apps()
        self.assertTrue('izi' in core_apps)

    def test_can_be_retrieved_with_overrides(self):
        apps = izi.get_core_apps(overrides=['apps.shipping'])
        self.assertTrue('apps.shipping' in apps)
        self.assertTrue('izi.apps.shipping' not in apps)

    def test_raises_exception_for_string_arg(self):
        with self.assertRaises(ValueError):
            izi.get_core_apps('forks.catalogue')


class TestIZITemplateSettings(TestCase):
    """
    IZI's IZI_MAIN_TEMPLATE_DIR setting
    """
    def test_allows_a_template_to_be_accessed_via_two_paths(self):
        paths = ['base.html', 'izi/base.html']
        for path in paths:
            try:
                loader.get_template(path)
            except TemplateDoesNotExist:
                self.fail("Template %s should exist" % path)

    def test_allows_a_template_to_be_customized(self):
        path = 'base.html'
        template = loader.get_template(path)
        rendered_template = template.render({})
        self.assertIn('IZI Test Shop', rendered_template)

    def test_default_izi_templates_are_accessible(self):
        path = 'izi/base.html'
        template = loader.get_template(path)
        rendered_template = template.render({})
        self.assertNotIn('IZI Test Shop', rendered_template)
