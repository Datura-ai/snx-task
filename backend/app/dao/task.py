from .base import BaseDao


class TaskDao(BaseDao):
    """DAO class for Task Model."""
    
    def create(self):
        """Create a Task."""
        print('TaskDao->create', self.session)
