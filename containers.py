"""Containers module."""

from dependency_injector import containers, providers
from github import Github

class Container(containers.DeclarativeContainer):
	config = providers.Configuration()

	github_client = providers.Factory(
		Github,
		login_or_token=config.github.auth_token,
		timeout=config.github.request_timeout,
	)
	
