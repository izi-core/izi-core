import factory

from izi.core.loading import get_class, get_model

Selector = get_class('partner.strategy', 'Selector')


__all__ = [
    'BasketFactory', 'BasketLineAttributeFactory'
]


class BasketFactory(factory.DjangoModelFactory):

    @factory.post_generation
    def set_strategy(self, create, extracted, **kwargs):
        # Load default strategy (without a user/request)
        self.strategy = Selector().strategy()

    class Meta:
        model = get_model('basket', 'Basket')


class BasketLineAttributeFactory(factory.DjangoModelFactory):
    option = factory.SubFactory('izi.test.factories.OptionFactory')

    class Meta:
        model = get_model('basket', 'LineAttribute')
