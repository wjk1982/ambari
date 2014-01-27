#!/usr/bin/env python

'''
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

from stacks.utils.RMFTestCase import *


class TestFalconServer(RMFTestCase):

  def test_start_default(self):
    self.executeScript("2.1.1/services/FALCON/package/scripts/falcon_server.py",
                       classname="FalconServer",
                       command="start",
                       config_file="default.json"
    )
    self.assertResourceCalled('Execute',
                              'cd /tmp; rm -f falcon-0.4.0.2.0.6.0-76.el6.noarch.rpm; wget http://public-repo-1.hortonworks.com/HDP-LABS/Projects/Falcon/2.0.6.0-76/rpm/falcon-0.4.0.2.0.6.0-76.el6.noarch.rpm; rpm -Uvh --nodeps falcon-0.4.0.2.0.6.0-76.el6.noarch.rpm',
                              not_if='yum list installed | grep falcon', )
    self.assertResourceCalled('Directory',
                              '/hadoop/falcon',
                              owner='falcon',
                              recursive=True, )
    self.assertResourceCalled('Directory', '/hadoop/falcon/activemq',
                              owner='falcon',
                              recursive=True, )
    self.assertResourceCalled('File', '/etc/falcon/conf/runtime.properties',
                              content=Template('runtime.properties.j2'),
                              mode=0644, )
    self.assertResourceCalled('File', '/etc/falcon/conf/startup.properties',
                              content=Template('startup.properties.j2'),
                              mode=0644, )
    self.assertResourceCalled('Execute',
                              'cd /tmp; rm -f falcon-0.4.0.2.0.6.0-76.el6.noarch.rpm; wget http://public-repo-1.hortonworks.com/HDP-LABS/Projects/Falcon/2.0.6.0-76/rpm/falcon-0.4.0.2.0.6.0-76.el6.noarch.rpm; rpm -Uvh --nodeps falcon-0.4.0.2.0.6.0-76.el6.noarch.rpm',
                              not_if='yum list installed | grep falcon', )
    self.assertResourceCalled('Execute',
                              'env JAVA_HOME=/usr/jdk64/jdk1.7.0_45 FALCON_LOG_DIR=/var/log/falcon FALCON_PID_DIR=/var/run/falcon FALCON_DATA_DIR=/hadoop/falcon/activemq /usr/lib/falcon/bin/falcon-start -port 15000',
                              user='falcon', )
    self.assertNoMoreResources()

  def test_stop_default(self):
    self.executeScript("2.1.1/services/FALCON/package/scripts/falcon_server.py",
                       classname="FalconServer",
                       command="stop",
                       config_file="default.json"
    )
    self.assertResourceCalled('Execute',
                          'cd /tmp; rm -f falcon-0.4.0.2.0.6.0-76.el6.noarch.rpm; wget http://public-repo-1.hortonworks.com/HDP-LABS/Projects/Falcon/2.0.6.0-76/rpm/falcon-0.4.0.2.0.6.0-76.el6.noarch.rpm; rpm -Uvh --nodeps falcon-0.4.0.2.0.6.0-76.el6.noarch.rpm',
                          not_if='yum list installed | grep falcon', )
    self.assertResourceCalled('Execute',
                          'env JAVA_HOME=/usr/jdk64/jdk1.7.0_45 FALCON_LOG_DIR=/var/log/falcon FALCON_PID_DIR=/var/run/falcon FALCON_DATA_DIR=/hadoop/falcon/activemq /usr/lib/falcon/bin/falcon-stop',
                          user='falcon', )
    self.assertNoMoreResources()

  def test_configure_default(self):
    self.executeScript("2.1.1/services/FALCON/package/scripts/falcon_server.py",
                       classname="FalconServer",
                       command="configure",
                       config_file="default.json"
    )
    self.assertResourceCalled('Execute',
                              'cd /tmp; rm -f falcon-0.4.0.2.0.6.0-76.el6.noarch.rpm; wget http://public-repo-1.hortonworks.com/HDP-LABS/Projects/Falcon/2.0.6.0-76/rpm/falcon-0.4.0.2.0.6.0-76.el6.noarch.rpm; rpm -Uvh --nodeps falcon-0.4.0.2.0.6.0-76.el6.noarch.rpm',
                              not_if='yum list installed | grep falcon', )
    self.assertResourceCalled('Directory',
                              '/hadoop/falcon',
                              owner='falcon',
                              recursive=True, )
    self.assertResourceCalled('Directory', '/hadoop/falcon/activemq',
                              owner='falcon',
                              recursive=True, )
    self.assertResourceCalled('File', '/etc/falcon/conf/runtime.properties',
                              content=Template('runtime.properties.j2'),
                              mode=0644, )
    self.assertResourceCalled('File', '/etc/falcon/conf/startup.properties',
                              content=Template('startup.properties.j2'),
                              mode=0644, )
    self.assertNoMoreResources()


