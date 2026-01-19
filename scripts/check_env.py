import os
import sys
if "DB_PASSWORD" in os.environ:
    print("Error")
    sys.exit(1)
else:
    print("Present")
    sys.exit(0)
