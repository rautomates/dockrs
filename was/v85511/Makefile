# Makefile to implement Docker containers and automation
# SriKrishna Prakash 

IMAGE_NAME:= ibmcom/websphere-traditional:8.5.5.11-install
TIMESTAMP:= `date +%Y`-`date +%m`-`date +%d`-`date +%s`
CONTAINER_NAME:= mywas
PROFILE_NAME:= dev
CELL_NAME:= wascellname 
NODE_NAME:= wasnodename  
HOST_NAME:= docker-was
EAR_FILE:= myapp/myearapp-1.0.ear
WAS_BINPATH:= /opt/IBM/WebSphere/AppServer/bin/
JAR_PATH:= /opt/drivers/
WAS_EXEC:= /opt/IBM/WebSphere/AppServer/bin/wasdeploy.sh
VERSION:= develop

.PHONY: all run shell kill pass restart logs ear_deploy install 

all: build 

build: 
	docker build -t $(IMAGE_NAME):$(VERSION) --rm . 

build_latest: 
	docker build -t $(IMAGE_NAME):latest --rm . 

test: 
	@echo 'WAS SERVER 8.5.5.11 PROFILE $(VERSION) container'
	docker run --rm -ti --name test-was-$(VERSION) -P $(IMAGE_NAME):$(VERSION)
	install
	
tag_latest: 
	docker tag $(IMAGE_NAME:):$(VERSION) $(NAME):latest 

run_latest:
	@echo 'running the WAS SERVER 8.5.5.11 $(VERSION) container'
	docker run --name $(CONTAINER_NAME) -h $(HOST_NAME) --rm -e PROFILE_NAME=$(PROFILE_NAME) -e CELL_NAME=$(CELL_NAME) -e NODE_NAME=$(NODE_NAME) -e HOST_NAME=$(HOST_NAME) -e UPDATE_HOSTNAME=true -p 9080:9080 -p 9043:9043 -p 9443:9443 -p 1521:1521 -p 1414:1414 -p 1415:1415 $(IMAGE_NAME)  $(IMAGE_NAME):latest

make_dockerfile:
	@echo 'overwrite current Dockerfile with the development file contents'
	cat was85511-profile.Dockerfile > Dockerfile
	@echo 'now you just need to run make build' 	

run: 
	@echo 'running the WAS SERVER 8.5.5.11 $(VERSION) container'
	docker run --name $(CONTAINER_NAME) -h $(HOST_NAME) -m=4096m -e JAVA_OPTS='jaxws.runtime.legacyWebMethod=true -Xms4096m -Xmx512m' -e PROFILE_NAME=$(PROFILE_NAME) -e CELL_NAME=$(CELL_NAME) -e NODE_NAME=$(NODE_NAME) -e HOST_NAME=$(HOST_NAME) -p 9080:9080 -p 9043:9043 -p 9443:9443 -p 1521:1521 -p 1414:1414 -p 1415:1415 $(IMAGE_NAME) 

shell:
	 docker exec -ti --user root $(CONTAINER_NAME) /bin/bash 

kill:
	docker kill $(CONTAINER_NAME)
	docker rm -f $(CONTAINER_NAME)

showpass:
	docker exec $(CONTAINER_NAME) cat /tmp/PASSWORD

restart:
	docker restart $(CONTAINER_NAME)

logs:
	docker logs -f $(CONTAINER_NAME)

install: 
	chmod +x run-config.sh 
	chmod +x config.py
	docker cp $(EAR_FILE) 	$(CONTAINER_NAME):/opt
	docker cp run-config.sh $(CONTAINER_NAME):$(WAS_BINPATH)
	docker cp config.py 	$(CONTAINER_NAME):$(WAS_BINPATH)
	docker exec 			$(CONTAINER_NAME) mkdir -p $(JAR_PATH)
	docker cp ojdbc6.jar	$(CONTAINER_NAME):$(JAR_PATH)
	docker exec 			$(CONTAINER_NAME) sh -c $(WAS_BINPATH) $(PROFILE_NAME)

deploy: dockerfile build tag_latest push_latest run_latest installmanagementmanagement