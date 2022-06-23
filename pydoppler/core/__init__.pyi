class API:
    ROOT_URL = 'https://api.doppler.io/v3'

    @classmethod
    def workspace(cls) -> str:...
    
    @classmethod
    def activity_logs(cls, page: int, per_page: int) -> list[str, dict[str, int]]:...    
    
    @classmethod
    def activity_logs_retrieve(cls, log_id: str) -> list[str, dict[str, str]]:...
