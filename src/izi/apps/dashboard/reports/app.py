from django.conf.urls import url

from izi.core.application import DashboardApplication
from izi.core.loading import get_class


class ReportsApplication(DashboardApplication):
    name = None
    default_permissions = ['is_staff', ]

    index_view = get_class('dashboard.reports.views', 'IndexView')

    def get_urls(self):
        urls = [
            url(r'^$', self.index_view.as_view(), name='reports-index'),
        ]
        return self.post_process_urls(urls)


application = ReportsApplication()
