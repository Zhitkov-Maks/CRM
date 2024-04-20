from django.db import models
from django.db.models import OneToOneField, ForeignKey

from leads.models import Leads
from contracts.models import Contracts


class Customers(models.Model):
    """
    Модель для представления активных клиентов. В данном варианте
    у нас у одного клиента может быть несколько контрактов. Но контракт
    может использоваться лишь единожды.
    """

    lead: ForeignKey = models.ForeignKey(
        Leads, on_delete=models.PROTECT, related_name="leads"
    )
    contract: OneToOneField = models.OneToOneField(
        Contracts, on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{str(self.lead)}"

    class Meta:
        """
        Указываем сортировку и имена которые будут указываться в админ панели.
        """

        verbose_name: str = "активный клиент"
        verbose_name_plural: str = "активные клиенты"
        unique_together: tuple = ("lead", "contract")
