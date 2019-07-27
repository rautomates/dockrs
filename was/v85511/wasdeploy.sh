#!/bin/bash
# script to run was-resources.py
# Maintainer: SriKrishna Prakash
# v1.0

CREATERESOURCES='/opt/IBM/WebSphere/AppServer/bin/was-resources.py'
PASS=`cat /tmp/PASSWORD`
echo $PASS
cd /opt/IBM/WebSphere/AppServer/bin/;
./wsadmin.sh -lang jython -user wsadmin -password $PASS -f $CREATERESOURCES