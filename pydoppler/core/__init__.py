

class API:
    ROOT_URL = 'https://api.doppler.io/v3'

    @classmethod
    def workspace(cls) -> str:
        """
        Get the workspace URL.

        :return: The workspace URL.
        """
        return f"{cls.ROOT_URL}/workspace"
    
    @classmethod
    def activity_logs(cls, page: int, per_page: int) -> list[str, dict[str, int]]:
        """
        Get the activity logs with pagination.

        :param page: The page number.
        :param per_page: The number of items per page.
        :return: fist element is the url, second element is the pagination parameters.
        """
        return [f"{cls.ROOT_URL}/logs", {'page': page, 'per_page': per_page}]
    
    @classmethod
    def activity_logs_retrieve(cls, log_id: str) -> list[str, dict[str, str]]:
        """
        retrieve an activity log.

        :param log_id: The log id.
        :return: first element is the url, second element is parameters.
        """
        return [f"{cls.ROOT_URL}/logs/log", {"log": log_id}]
    
    @classmethod
    async def projects(cls, page: int, per_page: int) -> list[str, dict[str, int]]:
        """
        Get the projects with pagination.

        :param page: The page number.
        :param per_page: The number of items per page.
        :return: fist element is the url, second element is the pagination parameters.
        """
        return [f"{cls.ROOT_URL}/projects", {'page': page, 'per_page': per_page}]
    
    @classmethod
    def projects_create(cls, name: str, description: str) -> list[str, dict[str, str]]:
        """
        Create a project.

        :param name: The project name.
        :param description: The project description.
        :return: fist element is the url, second element is body parameters.
        """
        return [f"{cls.ROOT_URL}/projects", {"name": name, "description": description}]

    @classmethod
    def projects_retrieve(cls, project_name: str) -> list[str, dict[str, str]]:
        """
        Retrieve a project.

        :param project_name: The project name.
        :return: fist element is the url, second element is parameters.
        """
        return [f"{cls.ROOT_URL}/projects/project", {"project": project_name}]
    
    @classmethod
    def projects_update(cls, project_name: str, project_new_name: str, description: str) -> list[str, dict[str, str]]:
        """
        Update a project.

        :param project_name: The project name.
        :param project_new_name: The project new name.
        :param description: The project description.
        :return: fist element is the url, second element is body parameters.
        """

        return [f"{cls.ROOT_URL}/projects", {"project": project_name, "name": project_new_name, "description": description}]

    @classmethod
    def projects_delete(cls, project_name: str) -> list[str, dict[str, str]]:
        """
        Delete a project.

        :param project_name: The project name.
        :return: fist element is the url, second element is body parameters.
        """
        return [f"{cls.ROOT_URL}/projects/project", {"project": project_name}]