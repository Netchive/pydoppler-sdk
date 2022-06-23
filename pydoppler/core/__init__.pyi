from calendar import c


class API:
    ROOT_URL = 'https://api.doppler.io/v3'

    @classmethod
    def workspace(cls) -> str:...
    
    @classmethod
    def activity_logs(cls, page: int, per_page: int) -> list[str, dict[str, int]]:...    

    @classmethod
    def activity_logs_retrieve(cls, log_id: str) -> list[str, dict[str, str]]:...

    @classmethod
    def projects(cls) -> list[str, dict[str, int]]:...

    @classmethod
    def projects_create(cls, name: str, description: str) -> list[str, dict[str, str]]:...

    @classmethod
    def projects_retrieve(cls, project_name: str) -> list[str, dict[str, str]]:...

    @classmethod
    def projects_update(cls, project_name: str, project_new_name: str, description: str) -> list[str, dict[str, str]]:...

    @classmethod
    def projects_delete(cls, project_name: str) -> list[str, dict[str, str]]:...