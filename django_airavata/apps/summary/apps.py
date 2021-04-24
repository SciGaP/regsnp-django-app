from django_airavata.app_config import AiravataAppConfig


class SummaryConfig(AiravataAppConfig):
    name = 'django_airavata.apps.summary'
    label = 'django_airavata_summary'
    verbose_name = 'Summary'
    app_order = 0
    url_home = 'django_airavata_summary:dashboard'
    fa_icon_class = 'fa-flask'
    app_description = """
        Launch applications and manage your experiments and projects.
    """
    nav = [
        {
            'label': 'Dashboard',
            'icon': 'fa fa-tachometer-alt',
            'url': 'django_airavata_summary:dashboard',
            'active_prefixes': ['applications', 'dashboard']
        },
        {
            'label': 'Experiments',
            'icon': 'fa fa-flask',
            'url': 'django_airavata_summary:experiments',
            'active_prefixes': ['experiments']
        },
        {
            'label': 'Projects',
            'icon': 'fa fa-box',
            'url': 'django_airavata_summary:projects',
            'active_prefixes': ['projects']
        },
        {
            'label': 'Storage',
            'icon': 'fa fa-folder-open',
            'url': 'django_airavata_summary:storage',
            'active_prefixes': ['storage']
        },
    ]

    def ready(self):
        import django_airavata.apps.summary.signals  # noqa
