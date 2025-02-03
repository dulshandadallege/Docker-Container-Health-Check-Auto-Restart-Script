import subprocess

def get_stopped_containers():
    """Retrieve a list of stopped Docker containers."""
    result = subprocess.run(["docker", "ps", "-a", "--filter", "status=exited", "--format", "{{.ID}}"], capture_output=True, text=True)
    containers = result.stdout.strip().split("\n")
    return [c for c in containers if c]  # Filter out empty strings

def restart_containers(containers):
    """Restart the given list of stopped containers."""
    for container_id in containers:
        print(f"🔄 Restarting container {container_id}...")
        subprocess.run(["docker", "start", container_id])
        print(f"✅ Container {container_id} restarted.")

if __name__ == "__main__":
    stopped_containers = get_stopped_containers()

    if not stopped_containers:
        print("✅ All containers are running.")
    else:
        print(f"⚠️ Found {len(stopped_containers)} stopped containers.")
        restart_containers(stopped_containers)
