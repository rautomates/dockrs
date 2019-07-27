# This Jython script is to create JDBCProvider, Datasource, WorkManager, QueueConnectionFactory, MessageQueue and Deploy the application
# Maintainer: SriKrishna Prakash

#To set the Java Heap size for the WAS container
AdminTask.setJVMMaxHeapSize('-serverName server1 -nodeName wasnodename -maximumHeapSize 4168')
AdminConfig.save()
print("Java Heap size is set as 4 GB ...")

#Creating JAAS User
AdminTask.createAuthDataEntry('[-alias "mydbuser" -user "scott" -password "tiger"]')
AdminConfig.save()
print ("JAAS Users created successfully...")

#To create JDBC Provider
AdminTask.createJDBCProvider('[-scope Cell=wascellname -databaseType Oracle -providerType "Oracle JDBC Driver" -implementationType "XA data source" -name "Oracle JDBC Driver (XA)"  -description "Oracle JDBC Driver (XA)" -classpath /opt/drivers/ojdbc6.jar -implementationClassName "oracle.jdbc.xa.client.OracleXADataSource" ]')
AdminConfig.save()
print ("JDBCProviders created successfully...")

#Create Datasource using the JDBC Provider
prvdrOXA = AdminConfig.getid('/JDBCProvider:Oracle JDBC Driver (XA)/')
AdminTask.createDatasource(prvdrOXA, '[-name "MyDB-DS" -jndiName jndi/MyDB-DS -dataStoreHelperClassName com.ibm.websphere.rsadapter.Oracle11gDataStoreHelper  -componentManagedAuthenticationAlias  wascellname/mydbuser -xaRecoveryAuthAlias wasnodename/mydbuser  -configureResourceProperties  [[URL java.lang.String jdbc:oracle:thin:@10.10.10.10:1521:mydb]]     ]')
AdminConfig.save()
print ("Datasources created successfully...")

#Create WorkManager for scheduler
provider = AdminConfig.getid('/Cell:wascellname/WorkManagerProvider:WorkManagerProvider/')
AdminConfig.create('WorkManagerInfo', provider,[['category',''],['description', 'My Work Manager'],['isGrowable','true'],['jndiName', 'wm/myschedulerWM'],['maxThreads','30'],['minThreads','15'],['numAlarmThreads','1'],['threadPriority','10'],['name','Quartz Scheduler WM'],['serviceNames',''] ])
AdminConfig.save()
print ("Scheduler created successfully...")

#Create QueueConnectionFactory
AdminTask.createWMQConnectionFactory("wasnodename(cells/wascellname/nodes/wasnodename|node.xml#wasnodename)", ["-name myConnFactory  -jndiName 'mq/myConnFactory' -type CF -description 'Mydescription' -qmgrName myQueMgr -qmgrHostname 10.10.10.10 -qmgrPortNumber 1415 -qmgrSvrconnChannel SERVER.CONNECTION"]) 
AdminConfig.save()
print ("JMS ConnectionFactories created successfully...")

#Create Message Queue
AdminTask.createWMQQueue("wascellname(cells/wascellname|resources.xml#wascellname)",[" -name myappq -jndiName mq/myappq -queueName myappq -description mydescription -qmgr myQueMgr -persistence APP -priority APP -expiry APP -ccsid 1208 -useNativeEncoding true -integerEncoding Normal -decimalEncoding Normal -floatingPointEncoding IEEENormal -useRFH2 true -sendAsync QDEF -readAhead QDEF -readAheadClose DELIVERALL -mqmdReadEnabled false -mqmdWriteEnabled false -mqmdMessageContext DEFAULT -messageBody UNSPECIFIED -replyToStyle DEFAULT "])
AdminConfig.save()
print ("Queues created successfully...")

#Deploy the application and channge the class loader principle
AdminApp.install('/opt/myearapp-1.0.ear','[-node wasnodename -cell wascellname -server server1]')
AdminApplication.configureClassLoaderPolicyForAnApplication("myearappname", "SINGLE")
AdminApplication.configureWebModulesOfAnApplication("myearappname", "mywebappname", "0", "PARENT_LAST", "true")
AdminConfig.save()