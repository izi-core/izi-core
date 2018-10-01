from izi.apps.catalogue.views import ProductDetailView as IZIProductDetailView


class ParentProductDetailView(IZIProductDetailView):
    enforce_parent = True
    enforce_paths = False
