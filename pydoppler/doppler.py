from pydoppler.core import HTTP
from pydoppler.core.endpoint import Endpoints


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
        """
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
