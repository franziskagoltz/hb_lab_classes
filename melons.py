import random

"""This file should have our order classes in it."""

class AbstractMelonOrder(object):
    """Parent melon order class"""
    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.tax = 0
        self.order_type = None
        self.shipped = False
        self.country_code = "US"


    def get_base_price(self):
        return random.choice(range(5,10))


    def get_total(self):
        """Calculate price."""

        base_price = self.get_base_price()

        if self.species == "christmasmelon":
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""
        super(DomesticMelonOrder, self).__init__(species, qty, tax=0.08, order_type="domestic")


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""
        super(InternationalMelonOrder, self).__init__(species, qty, tax=0.17, order_type="international")
        self.country_code = country_code

    def get_total(self):
        total = super(InternationalMelonOrder, self).get_total()
        
        if self.qty < 10:
            total += 3
        return total

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """Initializing a GovernmentMelonOrder that has no tax and needs to pass an inspection"""

    passed_inspection = False
    order_type = "government"

    def mark_inspection(self, passed):
        """Updates passed_inspection attribute based on inspection outcome"""

        self.passed_inspection = passed


