import os

# Database Configuration
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "mysql123!"),
    "database": os.getenv("DB_NAME", "restaurant_management_system")
}

# Global Constants
MAX_TRIALS = 3
CURRENCY = "Rs."
