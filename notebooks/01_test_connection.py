import os
from dotenv import load_dotenv
from databricks.sdk import WorkspaceClient

# Load .env from parent directory
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

# Get credentials
host = os.getenv("DATABRICKS_HOST")
token = os.getenv("DATABRICKS_TOKEN")

print(f"🔍 Loaded credentials:")
print(f"  Host: {host}")
print(f"  Token: {token[:20]}..." if token else "  Token: NOT FOUND")

if not host or not token:
    print("❌ Missing DATABRICKS_HOST or DATABRICKS_TOKEN in .env")
    exit(1)

# Create client with correct auth
client = WorkspaceClient(
    host=host,
    token=token
)

print("\n✅ Connection successful!")

# Test by listing workspace root
try:
    workspace_info = client.workspace.list(path="/")
    print(f"✅ Workspace contents: {workspace_info}")
except Exception as e:
    print(f"⚠️ Connected but error: {e}")