class Endpoints:
    ROOT_URL = "https://api.doppler.com/v3"
    V1_ROOT_URL = "https://api.doppler.com/v1"

    @classmethod
    def workspace(cls) -> str: ...
    @classmethod
    def activity_logs(cls) -> str: ...
    @classmethod
    def activity_log(cls) -> str: ...
    @classmethod
    def projects(cls) -> str: ...
    @classmethod
    def project(cls) -> str: ...
    @classmethod
    def environments(cls) -> str: ...
    @classmethod
    def environment(cls) -> str: ...
    @classmethod
    def configs(cls) -> str: ...
    @classmethod
    def config(cls) -> str: ...
    @classmethod
    def config_clone(cls) -> str: ...
    @classmethod
    def config_lock(cls) -> str: ...
    @classmethod
    def config_unlock(cls) -> str: ...
    @classmethod
    def config_logs(cls) -> str: ...
    @classmethod
    def config_log(cls) -> str: ...
    @classmethod
    def configs_log_rollback(cls) -> str: ...
    @classmethod
    def secrets_url(cls) -> str: ...
    @classmethod
    def secret_url(cls) -> str: ...
    @classmethod
    def secrets_download(cls) -> str: ...
    @classmethod
    def dynamic_secret_leases(cls) -> str: ...
    @classmethod
    def dynamic_secret_lease(cls) -> str: ...
    @classmethod
    def service_tokens(cls) -> str: ...
    @classmethod
    def service_token(cls) -> str: ...
    @classmethod
    def audit_workspace(cls) -> str: ...
    @classmethod
    def audit_workspace_users(cls) -> str: ...
    @classmethod
    def audit_workspace_user(cls, workplace_user_id: str) -> str: ...
    @classmethod
    def share_plain_text(cls) -> str: ...
    @classmethod
    def share_e2e_encrypted(cls) -> str: ...
