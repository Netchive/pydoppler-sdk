class Endpoints:
    ROOT_URL = "https://api.doppler.com/v3"
    V1_ROOT_URL = "https://api.doppler.com/v1"

    @classmethod
    def workspace(cls) -> str:
        """
        Endpoint: /v3/workspaces

        :return: https://api.doppler.com/v3/workspaces
        """
        return f"{cls.ROOT_URL}/workspace"

    @classmethod
    def activity_logs(cls) -> str:
        """
        Endpoint: /v3/logs

        :return: https://api.doppler.com/v3/logs
        """
        return f"{cls.ROOT_URL}/logs"

    @classmethod
    def activity_log(cls) -> str:
        """
        Endpoint: /v3/logs/log

        :return: https://api.doppler.com/v3/logs/log
        """
        return f"{cls.activity_logs()}/log"

    @classmethod
    def projects(cls) -> str:
        """
        Endpoint: /v3/projects

        :return: https://api.doppler.com/v3/projects
        """
        return f"{cls.ROOT_URL}/projects"

    @classmethod
    def project(cls) -> str:
        """
        Endpoint: /v3/projects/project

        :return: https://api.doppler.com/v3/projects/project
        """
        return f"{cls.projects()}/project"

    @classmethod
    def environments(cls) -> str:
        """
        Endpoint: /v3/environments

        :return: https://api.doppler.com/v3/environments
        """
        return f"{cls.ROOT_URL}/environments"

    @classmethod
    def environment(cls) -> str:
        """
        Endpoint: /v3/environments/environment

        :return: https://api.doppler.com/v3/environments/environment
        """
        return f"{cls.environments()}/environment"

    @classmethod
    def configs(cls) -> str:
        """
        Endpoint: /v3/configs

        :return: https://api.doppler.com/v3/configs
        """
        return f"{cls.ROOT_URL}/configs"

    @classmethod
    def config(cls) -> str:
        """
        Endpoint: /v3/configs

        :return: https://api.doppler.com/v3/configs/config
        """
        return f"{cls.configs()}/config"

    @classmethod
    def config_clone(cls) -> str:
        """
        Endpoint: /v3/configs/config/clone

        :return: https://api.doppler.com/v3/configs/config/clone
        """
        return f"{cls.config()}/clone"

    @classmethod
    def config_lock(cls) -> str:
        """
        Endpoint: /v3/configs/config/lock

        :return: https://api.doppler.com/v3/configs/config/lock
        """
        return f"{cls.config()}/lock"

    @classmethod
    def config_unlock(cls) -> str:
        """
        Endpoint: /v3/configs/config/unlock

        :return: https://api.doppler.com/v3/configs/config/unlock
        """
        return f"{cls.config()}/unlock"

    @classmethod
    def config_logs(cls) -> str:
        """
        Endpoint: /v3/configs/config/logs

        :return: https://api.doppler.com/v3/configs/config/logs
        """
        return f"{cls.config()}/logs"

    @classmethod
    def config_log(cls) -> str:
        """
        Endpoint: /v3/configs/config/logs/log

        :return: https://api.doppler.com/v3/configs/config/logs/log
        """
        return f"{cls.config_logs()}/log"

    @classmethod
    def configs_log_rollback(cls) -> str:
        """
        Endpoint: /v3/configs/config/logs/log/rollback

        :return: https://api.doppler.com/v3/configs/config/logs/log/rollback
        """
        return f"{cls.config_logs()}/log/rollback"

    @classmethod
    def secrets_url(cls) -> str:
        """
        Endpoint: /v3/configs/config/secrets

        :return: https://api.doppler.com/v3/configs/config/secrets
        """
        return f"{cls.config()}/secrets"

    @classmethod
    def secret_url(cls) -> str:
        """
        Endpoint: /v3/configs/config/secret

        :return: https://api.doppler.com/v3/configs/config/secret
        """
        return f"{cls.config()}/secret"

    @classmethod
    def secrets_download(cls) -> str:
        """
        Endpoint: /v3/configs/config/secrets/download

        :return: https://api.doppler.com/v3/configs/config/secrets/download
        """
        return f"{cls.secrets_url()}/download"

    @classmethod
    def dynamic_secret_leases(cls) -> str:
        """
        Endpoint: /v3/configs/config/dynamic_secrets/dynamic_secret/leases

        :return: https://api.doppler.com/v3/configs/config/dynamic_secrets/dynamic_secret/leases
        """
        return f"{cls.config()}/dynamic_secrets/dynamic_secret/leases"

    @classmethod
    def dynamic_secret_lease(cls) -> str:
        """
        Endpoint: /v3/configs/config/dynamic_secrets/dynamic_secret/leases/lease

        :return: https://api.doppler.com/v3/configs/config/dynamic_secrets/dynamic_secret/leases/lease
        """
        return f"{cls.config()}/dynamic_secrets/dynamic_secret/leases/lease"

    @classmethod
    def service_tokens(cls) -> str:
        """
        Endpoint: /v3/configs/config/tokens

        :return: https://api.doppler.com/v3/configs/config/tokens
        """
        return f"{cls.config()}/tokens"

    @classmethod
    def service_token(cls) -> str:
        """
        Endpoint: /v3/configs/config/tokens/token

        :return: https://api.doppler.com/v3/configs/config/tokens/token
        """
        return f"{cls.config()}/tokens/token"

    @classmethod
    def audit_workspace(cls) -> str:
        """
        Endpoint: /v3/workplace

        :return: https://api.doppler.com/v3/workplace
        """
        return f"{cls.ROOT_URL}/workplace"

    @classmethod
    def audit_workspace_users(cls) -> str:
        """
        Endpoint: /v3/workplace/users

        :return: https://api.doppler.com/v3/workplace/users
        """
        return f"{cls.ROOT_URL}/workplace/users"

    @classmethod
    def audit_workspace_user(cls, workplace_user_id: str) -> str:
        """
        Endpoint: /v3/workplace/users

        :return: https://api.doppler.com/v3/workplace/users/{workplace_user_id}
        """
        return f"{cls.ROOT_URL}/workplace/users/{workplace_user_id}"

    @classmethod
    def share_plain_text(cls) -> str:
        """
        Endpoint: /v1/share/secrets/plain

        :return:  https://api.doppler.com/v1/share/secrets/plain
        """
        return f"{cls.V1_ROOT_URL}/share/secrets/plain"

    @classmethod
    def share_e2e_encrypted(cls) -> str:
        """
        Endpoint: /v1/share/secrets/encrypted

        :return: https://api.doppler.com/v1/share/secrets/encrypted
        """
        return f"{cls.V1_ROOT_URL}/share/secrets/encrypted"
