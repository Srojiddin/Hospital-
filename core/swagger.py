from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


docs = get_schema_view(
    openapi.Info(
        title=" HOSPITAL MANAGEMENT REST API",
        default_version='v1',
        description="HOSPITAL MANAGEMENT REST API представляет собой интерфейс программирования приложений (API), разработанный для интеграции и взаимодействия с системой управления взаимоотношениями с клиентами (CRM). Этот API обеспечивает доступ к основным функциональным возможностям CRM-системы через стандартные протоколы передачи данных, такие как HTTP и HTTPS.",
        terms_of_service="CRM System REST API предназначен для интеграции с различными приложениями, сервисами и системами, такими как веб-приложения, мобильные приложения, системы управления контактами, системы автоматизации маркетинга и другие. Разработчики могут использовать этот API для создания собственных приложений, интеграции с существующими системами и автоматизации бизнес-процессов, связанных с управлением клиентскими отношениями.",
        contact=openapi.Contact(email="srojiddin4879@icloud.com"),
        license=openapi.License(name="MIT Lisence"),
    ),

    public=True,
    permission_classes=[permissions.AllowAny]
)