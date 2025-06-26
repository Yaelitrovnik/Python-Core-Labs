# -------------------------------
# Part 1: Your Task
# -------------------------------

# 1. Server class
class Server:
    instance_count = 0  # class variable

    def __init__(self, name, ip):
        self._name = name
        self._ip = ip
        Server.instance_count += 1

    def ping(self):
        print(f"Pinging {self._name} at {self._ip}... Success.")

    @staticmethod
    def validate_ip(ip):
        import re
        return re.match(r"^\d{1,3}(\.\d{1,3}){3}$", ip) is not None

    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, value):
        if Server.validate_ip(value):
            self._ip = value
        else:
            raise ValueError("Invalid IP format.")

# 2. Instantiate a Server
s = Server("MainServer", "192.168.0.1")
s.ping()

# 3. DatabaseServer class inherits from Server
class DatabaseServer(Server):
    def __init__(self, name, ip, engine):
        super().__init__(name, ip)
        self.engine = engine

    def backup(self):
        print(f"Backing up database on {self._name} using {self.engine} engine... Done.")

    # Override ping method
    def ping(self):
        print(f"DB Server {self._name} at {self._ip}: Secure ping... Success.")

# 4. Instantiate a DatabaseServer
db = DatabaseServer("DBServer1", "10.0.0.2", "PostgreSQL")
db.ping()    # overridden
db.backup()

# 5. Extra Challenge: WebServer class
class WebServer(Server):
    def deploy(self):
        print(f"Deploying web app on {self._name}... Done.")

    def restart(self):
        print(f"Restarting web server {self._name}... Done.")

    def info(self):  # optional override
        print(f"WebServer: {self._name} | IP: {self._ip}")

# Instantiate WebServer and demonstrate polymorphism
ws = WebServer("WebServer1", "10.0.0.3")
ws.deploy()
ws.restart()
ws.ping()

# Polymorphism demonstration
print("\nPolymorphism in action:")
servers = [s, db, ws]
for server in servers:
    server.ping()

# -------------------------------
# Part 2: Extension Tasks
# -------------------------------

from abc import ABC, abstractmethod
import functools

# Abstract Base Class
class CloudResource(ABC):
    @abstractmethod
    def info(self):
        pass

# Logging Decorator
def log_methods(cls):
    for attr_name in dir(cls):
        attr = getattr(cls, attr_name)
        if callable(attr) and not attr_name.startswith("__"):
            @functools.wraps(attr)
            def wrapper(self, *args, _attr=attr, **kwargs):
                print(f"[LOG] Calling: {cls.__name__}.{_attr.__name__}")
                return _attr(self, *args, **kwargs)
            setattr(cls, attr_name, wrapper)
    return cls

# Apply decorator and inherit abstract base class
@log_methods
class Server(CloudResource):
    instance_count = 0

    def __init__(self, name, ip):
        self._name = name
        self._ip = ip
        Server.instance_count += 1

    def ping(self):
        print(f"Pinging {self._name} at {self._ip}... Success.")

    def info(self):
        print(f"Server: {self._name} | IP: {self._ip}")

    @staticmethod
    def validate_ip(ip):
        import re
        return re.match(r"^\d{1,3}(\.\d{1,3}){3}$", ip) is not None

    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, value):
        if Server.validate_ip(value):
            self._ip = value
        else:
            raise ValueError("Invalid IP format.")

class DatabaseServer(Server):
    def __init__(self, name, ip, engine):
        super().__init__(name, ip)
        self.engine = engine

    def backup(self):
        print(f"Backing up database on {self._name} using {self.engine} engine... Done.")

    def ping(self):
        print(f"DB Server {self._name} at {self._ip}: Secure ping... Success.")

# Multiple Inheritance
class Monitor:
    def monitor(self):
        print("Monitoring server performance... All systems go.")

class MonitoredDatabaseServer(DatabaseServer, Monitor):
    def __init__(self, name, ip, engine):
        super().__init__(name, ip, engine)

# Composition
class Logger:
    def log(self, msg):
        print(f"[LOG]: {msg}")

class ComposedServer:
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip
        self.logger = Logger()

    def ping(self):
        self.logger.log(f"Pinging composed server {self.name} at {self.ip}...")

# Demonstration
if __name__ == "__main__":
    print("\nExtension Demo Starts")

    mds = MonitoredDatabaseServer("MonitoredDB", "10.0.0.4", "MySQL")
    mds.ping()
    mds.backup()
    mds.monitor()

    composed = ComposedServer("Composed1", "10.0.1.1")
    composed.ping()

    print(f"\nTotal Server Instances: {Server.instance_count}")

