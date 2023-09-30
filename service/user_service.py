from service.session import session
from table.user_service import Service
from utils.logger import logger

def add_service(user, service_name, service_port):
    # first check if port allocated
    ports = session.query(Service).filter(Service.service_port == service_port).all()
    if len(ports) > 0:
        logger.warning(f"port {service_port} has already allocated")
        return
    service = Service(user=user, service_name=service_name, service_port=service_port)
    session.add(service)
    session.commit()
    logger.info(f"successfully add service {user}-{service_name}:{service_port}")

