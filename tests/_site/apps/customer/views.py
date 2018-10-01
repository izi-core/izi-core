from izi.apps.customer.views import AccountSummaryView as IZIAccountSummaryView


class AccountSummaryView(IZIAccountSummaryView):
    # just here to test import in loading_tests:ClassLoadingWithLocalOverrideTests
    pass
