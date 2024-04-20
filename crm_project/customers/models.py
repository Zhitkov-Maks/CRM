from django.db import models
from django.db.models import ForeignKey, OneToOneField

from leads.models import Leads
from contracts.models import Contracts


class Customers(models.Model):
    """
    Модель для представления активных клиентов. В данном варианте
    у нас у одного клиента может быть несколько контрактов. Но контракт
    может использоваться единожды.
    """

    lead: ForeignKey = models.ForeignKey(
        Leads, on_delete=models.CASCADE, related_name="leads"
    )
    contract: OneToOneField = models.OneToOneField(
        Contracts,
        on_delete=models.CASCADE,
        related_name="contracts",
        default=0
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
