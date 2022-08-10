from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
from tenant_users.tenants.models import TenantBase


class Client(TenantBase):
    name = models.CharField(max_length=100)
    description = models.TextField()

    auto_create_schema = True


class Domain(DomainMixin):
    pass
