from pydoppler.core import HTTP


class Doppler(HTTP):
    def __init__(self, token: str) -> None:...
    def retrieve_workspace(self) -> dict:...
    def update_workspace(self, name: str, billing_email: str) -> dict:...
    def fetch_activity_logs(self, page: int = 1, per_page: int = 20) -> dict:...
    def retrieve_activity_log(self, log: str) -> dict:...
    def fetch_projects(self, page: int = 1, per_page: int = 20) -> dict:...
    def create_project(self, name: str, description: str):...
    def retrieve_project(self, project: str) -> dict:...
    def update_project(self, project: str, name: str, description: str | None = None) -> dict:...
    def delete_project(self, project: str) -> dict:...
    def fetch_environments(self, project: str) -> dict:...
    def retrieve_environment(self, project: str, environment: str) -> dict:...
    def create_environment(self, project: str, name: str, slug: str) -> dict:...
    def delete_environment(self, project: str, environment: str) -> dict:...
    def rename_environment(self, project: str, environment: str, name: str | None = None, slug: str | None = None) -> dict:...
    def fetch_configs(self, project: str, page: int = 1, per_page: int = 20) -> dict:...
    def create_config(self, project: str, environment: str, name: str) -> dict:...
    def retrieve_config(self, project: str, config: str) -> dict:...
    def update_config(self, project: str, config: str, name: str) -> dict:...
    def delete_config(self, project: str, config: str) -> dict:...
    def clone_config(self, project: str, config: str, name: str) -> dict:...
    def lock_config(self, project: str, name: str) -> dict:...
    def unlock_config(self, project: str, name: str) -> dict:...
    def fetch_config_logs(self, project: str, config: str, page: int = 1, per_page: int = 20) -> dict:...
    def retrieve_config_log(self, project: str, config: str, log: str) -> dict:...
    def rollback_config_log(self, project: str, config: str, log: str) -> dict:...
    def fetch_secrets(self, project_name: str, config_name: str, include_dynamic_secrets: bool = False, dynamic_secrets_ttl_sec: int = 1800, accepts: str = "application/json") -> dict: ...
    def retrieve_secret(self, project_name: str, config_name: str, secret_name: str) -> dict: ...
    def update_secrets(self, project_name: str, config_name: str, secrets: dict) -> dict: ...
    def download_secrets(self, project_name: str, config_name: str, name_transformer: str = "upper-snake", include_dynamic_secrets: bool = False, dynamic_secrets_ttl_sec: int = 1800) -> dict: ...
