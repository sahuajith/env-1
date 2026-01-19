import os
import sys
if "DB_PASSWORD" not in os.environ:
    print("Error")
    sys.exit(1)
else:
    print("Present")
    sys.exit(0)

