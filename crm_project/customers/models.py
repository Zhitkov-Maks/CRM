from django.db import models
from django.db.models import OneToOneField

from leads.models import Leads
from contracts.models import Contracts


class Customers(models.Model):
    """Модель для представления активных клиентов."""

    lead: OneToOneField = models.OneToOneField(
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
