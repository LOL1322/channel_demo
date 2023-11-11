from database.db_manager import db_manager
import settings

print(db_manager.create_base(scripts=(f'{settings.SCRIPTS_DIR}/tables.sql', f'{settings.SCRIPTS_DIR}/data.sql')))