# ✅ What it does:
* Checks the status of all running Docker containers.
* Restarts stopped containers automatically.
* Logs actions for better monitoring.

# How to Use:
1. Ensure Docker is installed and running on your system.
2. Save the script as docker_health_check.py.
3. Make the script executable (optional):
```
chmod +x docker_health_check.py
```
4. Run the script:
```
python docker_health_check.py
```
5. Automate it with a cron job (check every 5 minutes):
```
*/5 * * * * /usr/bin/python3 /path/to/docker_health_check.py
```
# Why is this Useful for DevOps?
* Ensures high availability by automatically restarting failed containers.
* Prevents downtime in containerized applications.
* Can be extended to send alerts (email, Slack, Prometheus, etc.).