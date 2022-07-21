from pydoppler.auth.validator import check_audit_token
from pydoppler.core import HTTP
from pydoppler.core.endpoint import Endpoints


class InvalidAuditToken(TypeError):
    """Exception raised when an invalid audit token is provided"""


class Doppler(HTTP):
    def __init__(self, token: str):
        """Doppler API wrapper

        :param token: doppler api token
        """
        super().__init__(token)

    def retrieve_workspace(self) -> dict:
        """Retrieve Workspace"""
        res = self._get(endpoint=Endpoints.workspace())
        return res

    def update_workspace(self, name: str, billing_email: str) -> dict:
        """Update Workspace

        :param name: workspace name
        :param billing_email: Billing email
        :return: status json data
        """
        res = self._post(
            endpoint=Endpoints.workspace(),
            json_data=dict(
                name=name,
                billing_email=billing_email,
            ),
        )
        return res

    def fetch_activity_logs(self, page: int = 1, per_page: int = 20) -> dict:
        """activity logs

        :param page: Page number
        :param per_page: Items per page
        :return:activity logs
        """

        res = self._get(
            endpoint=Endpoints.activity_logs(),
            params=dict(page=page, per_page=per_page),
        )
        return res

    def retrieve_activity_log(self, log: str) -> dict:
        """Activity Log

        :param log: Unique identifier for the log object.
        :return: activity log
        """

        res = self._get(endpoint=Endpoints.activity_log(), params=dict(log=log))
        return res

    def fetch_projects(self, page: int = 1, per_page: int = 20) -> dict:
        """fetch doppler project list

        :param page: page number
        :param per_page: items per page
        :return: project list
        """
        res = self._get(
            endpoint=Endpoints.projects(), params=dict(page=page, per_page=per_page)
        )
        return res

    def create_project(self, name: str, description: str):
        """Create Project

        :param name: name of project
        :param description: description pf project
        :return: Project Metadata
        """

        res = self._post(
            endpoint=Endpoints.projects(),
            json_data=dict(name=name, description=description),
        )
        return res

    def retrieve_project(self, project: str):
        """Retrieve project

        :param project: unique identifier for the project object.
        :return: project metadata
        """

        res = self._get(endpoint=Endpoints.project(), params=dict(project=project))
        return res

    def update_project(self, project: str, name: str, description: str | None = None):
        """Update Project

        :param project: unique identifier for the project object.
        :param name: name of project
        :param description: description pf project
        :return: project metadata`
        """
        res = self._post(
            endpoint=Endpoints.projects(),
            json_data=dict(name=name, description=description),
        )
        return res

    def delete_project(self, project: str):
        """Delete Project

        :param project: unique identifier for the project object.
        :return: status
        """

        res = self._delete(endpoint=Endpoints.projects(), params=dict(project=project))
        return res

    def fetch_environments(self, project: str):
        """fetch environments

        :param project: project's name
        :return: environments list
        """

        res = self._get(endpoint=Endpoints.environments(), params=dict(project=project))
        return res

    def retrieve_environment(self, project: str, environment: str):
        """Retrieve environment

        :param project: project's name
        :param environment: environment's slug
        :return: environment metadata
        """

        res = self._get(
            endpoint=Endpoints.environment(),
            params=dict(project=project, environment=environment),
        )
        return res

    def create_environment(self, project: str, name: str, slug: str):
        """Create Environment

        :param project: project's name
        :param name: name of the environment
        :param slug: slug of the environment
        :return: status metadata
        """

        res = self._post(
            endpoint=Endpoints.environments(),
            params=dict(project=project),
            json_data=dict(name=name, slug=slug),
        )
        return res

    def delete_environment(self, project: str, environment: str):
        """Delete environment

        :param project: project's name'
        :param environment: environment's slug
        :return: status
        """

        res = self._delete(
            endpoint=Endpoints.environment(),
            params=dict(project=project, environment=environment),
        )
        return res

    def rename_environment(
        self,
        project: str,
        environment: str,
        name: str | None = None,
        slug: str | None = None,
    ):
        """Rename environment

        :param project: project's name
        :param environment:  environment's slug
        :param name: desired name
        :param slug: desired slug
        :return: renamed environment metadata
        """

        res = self._put(
            endpoint=Endpoints.environment(),
            params=dict(project=project, environment=environment),
            json_data=dict(name=name, slug=slug),
        )
        return res

    def fetch_configs(self, project: str, page: int = 1, per_page: int = 20):
        """Fetch all configs.

        :param project: project's name
        :param page: page number
        :param per_page: items per page
        :return: config
        """

        res = self._get(
            endpoint=Endpoints.configs(),
            params=dict(project=project, page=page, per_page=per_page),
        )
        return res

    def create_config(self, project: str, environment: str, name: str):
        """Create a new branch config

        :param project: unique identifier for the object
        :param environment: identifier for environment object
        :param name: name of the new branch config
        :return: created config
        """

        res = self._post(
            endpoint=Endpoints.configs(),
            json_data=dict(project=project, environment=environment, name=name),
        )
        return res

    def retrieve_config(self, project: str, config: str):
        """Fetch config's details

        :param project: unique identifier for the project object.
        :param config: name of the config object.
        :return: config
        """

        res = self._get(
            endpoint=Endpoints.config(), params=dict(project=project, config=config)
        )
        return res

    def update_config(self, project: str, config: str, name: str):
        """Modify an exiting config

        :param project: Unique identifier for the project object.
        :param config: Name of the config object.
        :param name: The new name of config.
        :return: status
        """

        res = self._post(
            endpoint=Endpoints.config(),
            json_data=dict(project=project, config=config, name=name),
        )
        return res

    def delete_config(self, project: str, config: str):
        """Permanently delete the config.

        :param project: unique identifier for the project object.
        :param config: name of the config object.
        :return: status
        """

        res = self._delete(
            endpoint=Endpoints.config(), params=dict(project=project, config=config)
        )
        return res

    def clone_config(self, project: str, config: str, name: str):
        """Create a new branch config by cloning another.

        This duplicates a branch config and all its secrets.

        :param project: Unique identifier for the project object.
        :param config: Name of the branch config being cloned.
        :param name: Name of the new branch config.
        :return: config metadata
        """

        res = self._post(
            endpoint=Endpoints.config_clone(),
            json_data=dict(project=project, config=config, name=name),
        )
        return res

    def lock_config(self, project: str, name: str):
        """Prevent the config from being renamed or deleted.

        :param project: Unique identifier for the project object.
        :param name: Name of the config.
        :return: status
        """

        res = self._post(
            endpoint=Endpoints.config_lock(), json_data=dict(project=project, name=name)
        )
        return res

    def unlock_config(self, project: str, name: str):
        """Allow the config to be renamed and/or deleted.

        :param project: Unique identifier for the project object.
        :param name: Name of the config.
        :return: status
        """

        res = self._post(
            endpoint=Endpoints.config_unlock(),
            json_data=dict(project=project, name=name),
        )
        return res

    def fetch_config_logs(
        self, project: str, config: str, page: int = 1, per_page: int = 20
    ):
        """Config Logs

        :param project: Unique identifier for the project object.
        :param config: Name of the config object.
        :param page: Page number
        :param per_page: Items per page
        :return: list config
        """

        res = self._get(
            endpoint=Endpoints.config_logs(),
            params=dict(project=project, config=config, page=page, per_page=per_page),
        )
        return res

    def retrieve_config_log(self, project: str, config: str, log: str):
        """Config Log

        :param project: Unique identifier for the project object
        :param config: Name of the config object
        :param log: Unique identifier for the log object
        :return: config log
        """

        res = self._get(
            endpoint=Endpoints.config_log(),
            params=dict(project=project, config=config, log=log),
        )
        return res

    def rollback_config_log(self, project: str, config: str, log: str):
        """rollback config log

        :param project: project name
        :param config: config name
        :param log: log id
        :return: config log
        """

        res = self._post(
            endpoint=Endpoints.configs_log_rollback(),
            params=dict(project=project, config=config, log=log),
        )
        return res

    def fetch_secrets(
        self,
        project_name: str,
        config_name: str,
        include_dynamic_secrets: bool = False,
        dynamic_secrets_ttl_sec: int = 1800,
        accepts: str = "application/json",
    ):
        """
        List all secrets

        :param project_name: project name
        :param config_name: config name
        :param include_dynamic_secrets: Whether to issue leases and include dynamic secret values for the config
        :param dynamic_secrets_ttl_sec: The number of seconds until dynamic leases expire.
        Must be used with include_dynamic_secrets. Defaults to 1800 (30 minutes).
        :param accepts: Available options are: application/json, text/plain
        :return: secrets
        """
        res = self._get(
            endpoint=Endpoints.secrets_url(),
            params=dict(
                project=project_name,
                config=config_name,
                include_dynamic_secrets=include_dynamic_secrets,
                dynamic_secrets_ttl_sec=dynamic_secrets_ttl_sec,
            ),
            headers=dict(accepts=accepts),
        )
        return res

    def retrieve_secret(
        self, project_name: str, config_name: str, secret_name: str
    ) -> dict:
        """retrieve secret.

        :param project_name: project name:
        :param config_name: config name
        :param secret_name: secret name
        :return: secret
        """
        res = self._get(
            endpoint=Endpoints.secret_url(),
            params=dict(project=project_name, config=config_name, name=secret_name),
        )
        return res

    def update_secrets(
        self, project_name: str, config_name: str, secrets: dict
    ) -> dict:
        """Update secrets.

        :param project_name: project name
        :param config_name: config name
        :param secrets: Object of secrets you would like to save to the config.
        :return: secret
        """
        res = self._post(
            endpoint=Endpoints.secrets_url(),
            json_data=dict(project=project_name, config=config_name, secrets=secrets),
        )
        return res

    def download_secrets(
        self,
        project_name: str,
        config_name: str,
        name_transformer: str = "upper-snake",
        include_dynamic_secrets: bool = False,
        dynamic_secrets_ttl_sec: int = 1800,
    ) -> dict:
        """Download secrets.

        :param project_name: project name
        :param config_name: config name
        :param name_transformer: Transform secret names to a different case
        :param include_dynamic_secrets: Whether or not to issue leases and include dynamic secret values for the config
        :param dynamic_secrets_ttl_sec: The number of seconds until dynamic leases expire.
        Must be used with include_dynamic_secrets. Defaults to 1800 (30 minutes).
        :return: secrets
        """
        res = self._get(
            endpoint=Endpoints.secrets_download(),
            params=dict(
                project=project_name,
                config=config_name,
                name_transformer=name_transformer,
                include_dynamic_secrets=include_dynamic_secrets,
                dynamic_secrets_ttl_sec=dynamic_secrets_ttl_sec,
            ),
        )
        return res

    def dynamic_secrets_issue_lease(
        self, project_name: str, config_name: str, dynamic_secret: str, ttl_sec: int
    ):
        """Issue leases.

        :param project_name: project name
        :param config_name: config name
        :param dynamic_secret: Dynamic secret value
        :param ttl_sec: TTL
        :return: response
        """
        res = self._post(
            endpoint=Endpoints.dynamic_secret_leases(),
            json_data=dict(
                project=project_name,
                config=config_name,
                dynamic_secret=dynamic_secret,
                ttl_sec=ttl_sec,
            ),
        )
        return res

    def dynamic_secret_revoke_lease(
        self, project_name: str, config_name: str, dynamic_secret: str, slug: str
    ):
        """Revoke leases.

        :param project_name: project name
        :param config_name: config name
        :param dynamic_secret: Dynamic secret value
        :param slug: slug of the lease to revoke
        :return: response
        """
        res = self._delete(
            endpoint=Endpoints.dynamic_secret_lease(),
            params=dict(
                project=project_name,
                config=config_name,
                dynamic_secret=dynamic_secret,
                slug=slug,
            ),
        )
        return res

    def service_tokens(self, project_name: str, config_name: str):
        """List service tokens.

        :param project_name: project name
        :param config_name: config name
        :return: response
        """
        res = self._get(
            endpoint=Endpoints.service_tokens(),
            params=dict(project=project_name, config=config_name),
        )
        return res

    def create_service_token(
        self,
        project_name: str,
        config_name: str,
        name: str,
        expire_at: str | None = None,
        access: str = "read",
    ):
        """Create service token
        :param project_name: project name
        :param config_name: config name
        :param name: name of the service token
        :param expire_at: expiration time of the token
        :param access: access level of the token
        :return: response
        """
        res = self._post(
            endpoint=Endpoints.service_tokens(),
            json_data=dict(
                project=project_name,
                config=config_name,
                name=name,
                expire_at=expire_at,
                access=access,
            ),
        )
        return res

    def delete_service_token(self, project_name: str, config_name: str, slug: str):
        """Delete service token.

        :param project_name: project name
        :param config_name: config name
        :param slug: slug of the service token
        :return: response
        """
        res = self._delete(
            endpoint=Endpoints.service_token(),
            params=dict(project=project_name, config=config_name, slug=slug),
        )
        return res

    def share_plain_text(
        self, secret: str, expire_views: int = 1, expire_days: int = 1
    ):
        """Generate a Doppler Share link by sending a plain text secret.
        This endpoint is not end-to-end encrypted as you are sending the secret in plain text.
        At no point do we store the plain text secret or the password in our systems.
        The receive flow the user goes through will be end-to-end encrypted
        where the encrypted secret will be decrypted on the browser.

        :param secret: Plain text secret to share.
        :param expire_views: Number of views before the link expires. Valid ranges: 1 to 50. -1 for unlimited.
        :param expire_days: Number of days before the link expires. Valid range: 1 to 90.
        :return: response
        """
        res = self._post(
            endpoint=Endpoints.share_plain_text(),
            json_data=dict(
                secret=secret, expire_views=expire_views, expire_days=expire_days
            ),
        )
        return res

    def share_e2e_encrypted(
        self,
        encrypted_secret: str,
        hashed_password: str,
        expire_views: int = 1,
        expire_days: int = 1,
        encryption_kdf: str = "pbkdf2",
        encryption_salt_rounds: int = 100000,
    ):
        """

        :param encrypted_secret: Ecrypted secret using AES-GCM with a symmetric key derived from a cryptographically
        random 64 character passphrase using PBKDF2.
        100,000 salt rounds required. Then base64 encode the encrypted secret.
        :param hashed_password: SHA256 hash of the password. This is NOT the hash of the derived encryption key.
        :param expire_views: Number of views before the link expires. Valid ranges: 1 to 50. -1 for unlimited.
        :param expire_days: Number of days before the link expires. Valid range: 1 to 90.
        :param encryption_kdf: The key derivation function used. Must by "pbkdf2".
        :param encryption_salt_rounds: Number of salt rounds used by KDF. Must be "100000".
        :return: response
        """
        res = self._post(
            endpoint=Endpoints.share_e2e_encrypted(),
            json_data=dict(
                encrypted_secret=encrypted_secret,
                hashed_password=hashed_password,
                expire_views=expire_views,
                expire_days=expire_days,
                encryption_kdf=encryption_kdf,
                encryption_salt_rounds=encryption_salt_rounds,
            ),
        )
        return res


class DopplerAudit(HTTP):
    def __init__(self, token: str):
        if check_audit_token(token):
            super(HTTP, self).__init__(token)
        else:
            raise InvalidAuditToken()

    def workplace(self, settings: bool = False):
        """Get information about the specific workplace.

        :param settings: If true, the api will return more information if the workplace has e.g.
        SAML enabled and SCIM enabled
        :return: response
        """
        res = self._get(
            endpoint=Endpoints.audit_workspace(), params=dict(settings=settings)
        )
        return res

    def workplace_users(self, settings: bool = False):
        """Get all users of a workplace.

        :param settings: If true, the api will return more information if users have e.g.
        SAML enabled and/or Multi-Factor Auth enabled
        :return: response
        """
        res = self._get(
            endpoint=Endpoints.audit_workspace_users(), params=dict(settings=settings)
        )
        return res

    def workplace_user(self, workplace_user_id: str, settings: bool = False):
        """Get a specific user in a workplace.

        :param workplace_user_id: The ID of the workplace user
        :param settings: If true, the api will return more information if the user has e.g.
        SAML enabled and/or Multi-Factor Auth enabled
        :return: response
        """
        res = self._get(
            endpoint=Endpoints.audit_workspace_user(
                workplace_user_id=workplace_user_id
            ),
            params=dict(settings=settings),
        )
        return res
