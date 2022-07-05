class Endpoints:
    ROOT_URL = "https://api.doppler.com/v3"

    @classmethod
    def workspace(cls) -> str:
        """
        Endpoint: /v3/workspaces

        :return: https://api.doppler.io/v3/workspaces
        """
        return f"{cls.ROOT_URL}/workspace"

    @classmethod
    def activity_logs(cls) -> str:
        """
        Endpoint: /v3/logs

        :return: https://api.doppler.io/v3/logs
        """
        return f"{cls.ROOT_URL}/logs"

    @classmethod
    def activity_log(cls) -> str:
        """
        Endpoint: /v3/logs/log

        :return: https://api.doppler.io/v3/logs/log
        """
        return f"{cls.activity_logs()}/log"

    @classmethod
    def projects(cls) -> str:
        """
        Endpoint: /v3/projects

        :return: https://api.doppler.io/v3/projects
        """
        return f"{cls.ROOT_URL}/projects"

    @classmethod
    def project(cls) -> str:
        """
        Endpoint: /v3/projects/project

        :return: https://api.doppler.io/v3/projects/project
        """
        return f"{cls.projects()}/project"

    @classmethod
    def environments(cls) -> str:
        """
        Endpoint: /v3/environments

        :return: https://api.doppler.io/v3/environments
        """
        return f"{cls.ROOT_URL}/environments"

    @classmethod
    def environment(cls) -> str:
        """
        Endpoint: /v3/environments/environment

        :return: https://api.doppler.io/v3/environments/environment
        """
        return f"{cls.environments()}/environment"

    @classmethod
    def configs(cls) -> str:
        """
        Endpoint: /v3/configs

        :return: https://api.doppler.io/v3/configs
        """
        return f"{cls.ROOT_URL}/configs"

    @classmethod
    def config(cls) -> str:
        """
        Endpoint: /v3/configs

        :return: https://api.doppler.io/v3/configs/config
        """
        return f"{cls.configs()}/config"

    @classmethod
    def config_clone(cls) -> str:
        """
        Endpoint: /v3/configs/config/clone

        :return: https://api.doppler.io/v3/configs/config/clone
        """
        return f"{cls.config()}/clone"

    @classmethod
    def config_lock(cls) -> str:
        """
        Endpoint: /v3/configs/config/lock

        :return: https://api.doppler.io/v3/configs/config/lock
        """
        return f"{cls.config()}/lock"

    @classmethod
    def config_unlock(cls) -> str:
        """
        Endpoint: /v3/configs/config/unlock

        :return: https://api.doppler.io/v3/configs/config/unlock
        """
        return f"{cls.config()}/unlock"

    @classmethod
    def config_logs(cls) -> str:
        """
        Endpoint: /v3/configs/config/logs

        :return: https://api.doppler.io/v3/configs/config/logs
        """
        return f"{cls.config()}/logs"

    @classmethod
    def configs_log_rollback(cls) -> str:
        """
        Endpoint: /v3/configs/config/logs/log/rollback

        :return: https://api.doppler.io/v3/configs/config/logs/log/rollback
        """
        return f"{cls.config_logs()}/log/rollback"
