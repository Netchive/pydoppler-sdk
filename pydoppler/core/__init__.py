

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
