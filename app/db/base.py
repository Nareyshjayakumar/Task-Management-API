from app.db.base_class import Base

# Import all models so Alembic can detect them
from app.db.models import user, task, project, task_comment
