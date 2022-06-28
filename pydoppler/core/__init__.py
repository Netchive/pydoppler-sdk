import httpx

class APIObject:
    ROOT_URL = 'https://api.doppler.io/v3'

    @classmethod
    def workspace(cls) -> str:
        """
        Get the workspace URL.

        :return: The workspace URL.
        """
        return f"{cls.ROOT_URL}/workspace"
    
    @classmethod
    def workspace_update(cls, workspace_name: str, billing_email: str) -> list[str | dict[str, str]]:
        """
        Update workspace url and payload.

        :param workspace_name: The workspace name.
        :param billing_email: The billing email.
        :return: The workspace URL.
        """
        return [f"{cls.workspace()}", {"name": workspace_name, "billing_email": billing_email}]
    
    @classmethod
    def activity_logs(cls, page: int, per_page: int) -> list[str | dict[str, int]]:
        """
        Get the activity logs with pagination.

        :param page: The page number.
        :param per_page: The number of items per page.
        :return: fist element is the url, second element is the pagination parameters.
        """
        return [f"{cls.ROOT_URL}/logs", {'page': page, 'per_page': per_page}]
    
    @classmethod
    def activity_logs_retrieve(cls, log_id: str) -> list[str | dict[str, str]]:
        """
        retrieve an activity log.

        :param log_id: The log id.
        :return: first element is the url, second element is parameters.
        """
        return [f"{cls.ROOT_URL}/logs/log", {"log": log_id}]
    
    @classmethod
    async def projects(cls, page: int, per_page: int) -> list[str | dict[str, int]]:
        """
        Get the projects with pagination.

        :param page: The page number.
        :param per_page: The number of items per page.
        :return: fist element is the url, second element is the pagination parameters.
        """
        return [f"{cls.ROOT_URL}/projects", {'page': page, 'per_page': per_page}]
    
    @classmethod
    def projects_create(cls, name: str, description: str) -> list[str | dict[str, str]]:
        """
        Create a project.

        :param name: The project name.
        :param description: The project description.
        :return: fist element is the url, second element is body parameters.
        """
        return [f"{cls.ROOT_URL}/projects", {"name": name, "description": description}]

    @classmethod
    def projects_retrieve(cls, project_name: str) -> list[str | dict[str, str]]:
        """
        Retrieve a project.

        :param project_name: The project name.
        :return: fist element is the url, second element is parameters.
        """
        return [f"{cls.ROOT_URL}/projects/project", {"project": project_name}]
    
    @classmethod
    def projects_update(cls, project_name: str, project_new_name: str, description: str) -> list[str |  dict[str, str]]:
        """
        Update a project.

        :param project_name: The project name.
        :param project_new_name: The project new name.
        :param description: The project description.
        :return: fist element is the url, second element is body parameters.
        """

        return [f"{cls.ROOT_URL}/projects", {"project": project_name, "name": project_new_name, "description": description}]

    @classmethod
    def projects_delete(cls, project_name: str) -> list[str | dict[str, str]]:
        """
        Delete a project.

        :param project_name: The project name.
        :return: fist element is the url, second element is body parameters.
        """
        return [f"{cls.ROOT_URL}/projects/project", {"project": project_name}]
    
    @classmethod
    def environments(cls, project_name: str) -> list[str | dict[str, str]]:
        """
        Get all environments.

        :param project_name: The project name.
        :return: fist element is the url, second element is query parameters.
        """
        return [f"{cls.ROOT_URL}/environments", {"project": project_name}]
    
    @classmethod
    def environments_retrieve(cls, project_name: str, environment: str) -> list[str | dict[str, str]]:
        """
        Retrieve a specific environment.

        :param project_name: The project name.
        :param environment: The environment's slug.

        :return: fist element is the url, second element is query parameters.
        """
        return [f"{cls.ROOT_URL}/environments/environment", {"project": project_name, "environment": environment}]
    
    @classmethod
    def environments_create(cls, project_name: str, name: str, slug: str) -> list[str | dict[str, str] | dict[str, str]]:
        """
        Create a new environment.

        :param project_name: The project name.
        :param name: The name of the environment.
        :param slug: Desired slug.
        :return: fist element is the url, second element is body parameters, third element is body parameters.
        """
        return [f"{cls.ROOT_URL}/environments", {"project": project_name}, {"name": name, "slug": slug}]

    @classmethod
    def environments_delete(cls, project_name: str, environment: str) -> list[str | dict[str, str]]:
        """
        Delete a specific environment.

        :param project_name: The project name.
        :param environment: The environment's slug.
        :return: first element is the url, second element is query parameters.
        """
        return [f"{cls.ROOT_URL}/environments/environment", {"project": project_name, "environment": environment}]

    @classmethod
    def environments_rename(cls, project_name: str, environment: str, name: str, slug: str) -> list[str | dict[str, str] | dict[str, str]]:
        """
        Rename a specific environment.

        :param project_name: The project name.
        :param environment: The environment's slug.
        :param name: The name of the environment.
        :param slug: Desired slug.
        :return: first element is the url, second element is query parameters, third element is body parameters.
        """
        return [f"{cls.ROOT_URL}/environments/environment", {"project": project_name, "environment": environment}, {"name": name, "slug": slug}]
    
    @classmethod
    def configs(cls, project_name: str, page: int, per_page: int) -> list[str | dict[str, str | int]]:
        """
        Fetch all configs.

        :param project_name: The project name.
        :param page: The page number
        :param per_page: The number of items to fetch per page.
        :return: fist element is the url, second element is query parameters.
        """
        return [f"{cls.ROOT_URL}/configs", {"project": project_name, "page": page, "per_page": per_page}]
    
    @classmethod
    def configs_create(cls, project_name: str, environment: str, config_name: str) -> list[str | dict[str, str]]:
        """
        Create a new branch config.

        :param project_name: Unique identifier for the project object.
        :param environment: Identifier for the environment object.
        :param config_name: Name of the new branch config.
        :return: fist element is the url, second element is body parameters.
        """
        return [f"{cls.ROOT_URL}/configs", {"project": project_name, "environment": environment, "name": config_name}]
    
    @classmethod
    def configs_retrieve(cls, project_name: str, config_name: str) -> list[str | dict[str, str]]:
        """
        Fetch a config's details.

        :param project_name: Unique identifier for the project object.
        :param config_name: Name of the config object.
        :return: fist element is the url, second element is query parameters.
        """
        return [f"{cls.ROOT_URL}/configs/config", {"project": project_name, "name": config_name}]
    
    @classmethod
    def configs_update(cls, project_name: str, config_name: str, config_new_name: str) -> list[str | dict[str, str]]:
        """
        Modify an existing config.

        :param project_name: Unique identifier for the project object.
        :param config_name: Name of the config object.
        :param config_new_name: New name of the config.
        :return: fist element is the url, second element is body parameters.
        """
        return [f"{cls.ROOT_URL}/configs/config", {"project": project_name, "config": config_name, "name": config_new_name}]
    
    @classmethod
    def configs_delete(cls, project_name: str, config_name: str) -> list[str | dict[str, str]]:
        """
        Permanently delete the config.

        :param project_name: Unique identifier for the project object.
        :param config_name: Name of the config object.
        :return: fist element is the url, second element is body parameters.
        """
        return [f"{cls.ROOT_URL}/configs/config", {"project": project_name, "config": config_name}]
    
    @classmethod
    def configs_clone(cls, project_name: str, config_name: str, config_new_name: str) -> list[str | dict[str, str]]:
        """
        Create a new branch config by cloning another. This duplicates a branch config and all its secrets.

        :param project_name: Unique identifier for the project object.
        :param config_name: Name of the config object.
        :param config_new_name: New name of the config.
        :return: fist element is the url, second element is body parameters.
        """
        return [f"{cls.ROOT_URL}/configs/config/clone", {"project": project_name, "config": config_name, "name": config_new_name}]
    
    @classmethod
    def configs_lock(cls, project_name: str, config_name: str) -> list[str | dict[str, str]]:
        """
        Prevent the config from being renamed or deleted.

        :param project_name: Unique identifier for the project object.
        :param config_name: Name of the config object.
        :return: fist element is the url, second element is body parameters.
        """
        return [f"{cls.ROOT_URL}/configs/config/lock", {"project": project_name, "config": config_name}]
    
    @classmethod
    def configs_unlock(cls, project_name: str, config_name: str) -> list[str | dict[str, str]]:
        """
        Allow the config to be renamed and/or deleted.

        :param project_name: Unique identifier for the project object.
        :param config_name: Name of the config object.
        :return: fist element is the url, second element is body parameters.
        """
        return [f"{cls.ROOT_URL}/configs/config/unlock", {"project": project_name, "config": config_name}]
    
    @classmethod
    def configs_logs(cls, project_name: str, config_name: str, page: int, per_page: int) -> list[str | dict[str, str | int]]:
        """
        Config Logs.

        :param project_name: Unique identifier for the project object.
        :param config_name: Name of the config object.
        :param page: Page number.
        :param per_page: Number of results to return per page.
        :return: fist element is the url, second element is query parameters.
        """
        return [f"{cls.ROOT_URL}/configs/config/logs", {"project": project_name, "config": config_name, "page": page, "per_page": per_page}]
    
    @classmethod
    def configs_logs_retrieve(cls, project_name: str, config_name: str, log_id: str) -> list[str | dict[str, str]]:
        """
        Config Log.

        :param project_name: Unique identifier for the project object.
        :param config_name: Name of the config object.
        :param log_id: Unique identifier for the log object.
        :return: fist element is the url, second element is query parameters.
        """
        return [f"{cls.ROOT_URL}/configs/config/logs", {"project": project_name, "config": config_name, "log": log_id}]
    
    @classmethod
    def configs_logs_rollback(cls, project_name: str, config_name: str, log_id: str) -> list[str | dict[str, str]]:
        """
        Config Log.

        :param project_name: Unique identifier for the project object.
        :param config_name: Name of the config object.
        :param log_id: Unique identifier for the log object.
        :return: fist element is the url, second element is query parameters.
        """
        return [f"{cls.ROOT_URL}/configs/config/logs/log/rollback", {"project": project_name, "config": config_name, "log": log_id}]

    
class API(APIObject):
    def __init__(self, api_key: str | None = None, user_name: str | None = None, password: str | None = None) -> None:
        self.api_key = api_key
        self.user_name = user_name
        self.password = password
    
    def cred_exception_checker(self) -> dict[str, str]:
        """
        Callback for errors.
        """

        # TODO: 나중에 사용자 정의 Exception class 만들어서 처리하도록 하자.
        if self.user_name:
            user_name = self.user_name
        else:
            raise Exception("User name is not set.")

        if self.password:
            password = self.password
        else: 
            raise Exception("Password is not set.")
        
        return {
            "user_name": user_name,
            "password": password
        }
        
    
    def get_retrieve_workspace(self):
        cred = self.cred_exception_checker()
        resp = httpx.get(
            url=self.workspace(),
            auth=httpx.BasicAuth(
                username=cred["user_name"],
                password=cred["password"],
            )
        )
        if resp.status_code != 200:
            # TODO: 나중에 사용자 정의 Exception class 만들어서 처리하도록 하자.
            raise Exception(f"{resp.status_code} {resp.reason}")
        return resp.json()
    
    def post_update_workspace(self, workspace_name: str, billing_email: str):
        cred = self.cred_exception_checker()
        resp = httpx.post(
            url=self.workspace(),
            auth=httpx.BasicAuth(
                username=cred['user_name'],
                password=cred['password'],
            ),
            json={"name": workspace_name, "billing_email": billing_email}
        )
        if resp.status_code != 200:
            # TODO: 나중에 사용자 정의 Exception class 만들어서 처리하도록 하자.
            raise Exception(f"{resp.status_code}")
        return resp.json()
        