from typing import Any

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django.db.models import Q, QuerySet, ProtectedError
from django.shortcuts import redirect, render
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
    CreateView,
)

from .models import Leads


class ListLeads(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """
    Класс для отображения списка Потенциальных клиентов. Доступен
    пользователям у которых присутствует разрешение 'view_leads'.
    """

    permission_required: str = "leads.view_leads"
    template_name: str = "leads/leads-list.html"
    model: Any = Leads
    context_object_name: str = "leads"


class ListLeadsSearch(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """
    Класс для поиска Лидов по введенной пользователем фамилии, без учета
    регистра. Доступно пользователям с разрешением "view_leads."
    """

    permission_required: str = "leads.view_leads"
    template_name: str = "leads/leads-list.html"
    model: Any = Leads
    context_object_name: str = "leads"

    def get_queryset(self) -> QuerySet:
        """Переопределяем метод для поиска клиента по фамилии"""
        query = self.request.GET.get("query")
        return Leads.objects.only(
            "id", "last_name", "first_name", "middle_name"
        ).filter(Q(last_name__iregex=query))

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        """
        Добавляет идентификатор для отображения ввода пользователя в шаблоне.
        """
        context = super().get_context_data()
        key = self.request.GET.get("query")
        context.update({"query": key})
        return context


class DetailLeads(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """
    Класс для отображения детальной информации о Лиде. Доступно пользователям с
    разрешением view_leads.
    """

    permission_required: str = "leads.view_leads"
    template_name: str = "leads/leads-detail.html"
    model: Any = Leads


class DeleteLeads(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):  # type: ignore
    """
    Класс для удаления Лида. Доступен пользователям с разрешением ''delete_leads.
    Комментарий type: ignore нужен для mypy, так как выдает ошибку
    'Definition of "object" in base class "DeletionMixin" is
    incompatible with definition in base class "BaseDetailView"'
    """

    permission_required: str = "leads.delete_leads"
    template_name: str = "leads/leads-delete.html"
    model: Any = Leads
    success_url: str = "/leads/"

    def post(self, request, *args, **kwargs):
        lead = self.get_object()
        try:
            lead.delete()
            redirect("/leads/")
        except ProtectedError:
            return render(request, 'leads/error.html', {"lead": lead})


class UpdateLeads(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """
    Класс для обновления данных Лида. Доступен пользователям с разрешением
    'change_leads'.
    """

    permission_required: str = "leads.change_leads"
    template_name: str = "leads/leads-edit.html"
    fields: tuple = (
        "first_name",
        "last_name",
        "middle_name",
        "email",
        "phone",
        "advertising"
    )
    model: Any = Leads
    success_url: str = "/leads/"


class CreateLeads(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """
    Класс для создания Лидов. Доступен пользователям с разрешением 'add_leads'.
    """

    permission_required: str = "leads.add_leads"
    template_name: str = "leads/leads-create.html"
    fields: tuple = (
        "first_name",
        "last_name",
        "middle_name",
        "email",
        "phone",
        "advertising",
    )
    success_url: str = "/leads/"
    model: Any = Leads
