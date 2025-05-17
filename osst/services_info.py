import subprocess

def get_active_services():
    """
    Returns a list of active (running) systemd services on the system.
    """
    # We blacklist some common services
    blacklist = {
        'systemd-journald.service',
        'systemd-logind.service',
        'systemd-networkd.service',
        'systemd-resolved.service',
        'systemd-timesyncd.service',
        'systemd-udevd.service',
        'rsyslog.service',
        'dbus.service',
        'polkit.service',
        'packagekit.service',
        'snapd.service',
    }
    try:
        # We call systemctl to get only active (running) services in short format
        result = subprocess.run(
            ["systemctl", "list-units", "--type=service", "--state=running", "--no-pager", "--no-legend"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        services = []
        for line in result.stdout.strip().split('\n'):
            if line:
                # The first column is the name of the service, e.g. ssh.service
                service_name = line.split()[0]
                if service_name not in blacklist:
                    services.append(service_name)
        return services
    except Exception as e:
        # In case of error, return an empty list or you can log the error
        return []
