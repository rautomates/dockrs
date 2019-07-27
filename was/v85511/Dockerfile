FROM ibmcom/websphere-traditional:8.5.5.11-install
MAINTAINER SriKrishnaPrakash

WORKDIR /opt/IBM/WebSphere/AppServer/
ENV WORKDIR /opt/IBM/WebSphere/AppServer

USER root
ADD was-resources.py /opt/IBM/WebSphere/AppServer/bin/was-resources.py
ADD wasdeploy.sh /opt/IBM/WebSphere/AppServer/bin/wasdeploy.sh 
RUN chmod +x /opt/IBM/WebSphere/AppServer/bin/wasdeploy.sh

USER was
CMD ["/opt/IBM/WebSphere/AppServer/bin/wasdeploy.sh"]
ENTRYPOINT [" /opt/IBM/WebSphere/AppServer/bin/","startServer.sh"]
EXPOSE 9043 9943,1521,1415, 1414, 443, 3309, 5201