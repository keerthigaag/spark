# spark
women's shoe catalog

## DESCRIPTION

A distribued worker sysytem is implemented to update data in Redis using python. Women's shoe catalog based dataset is used. The dataset contains id, brand, colors,dateadded as header. To assume id to be unique. Also to ignore record which have null values. Redis(database) server is used to store each of the record. Spark dataframe is used to read csv dataset, API are used to query and fetch data from redis. All requests and responses are in the format of JSON.

## PREREQUISITES

Install,
canopy-2.1.9.win-x86-cp35
python-2.7.17
redis-2.4.6-setup-32-bit
spark-2.4.4-bin-hadoop2.7
winutils
spark-2.4.4-bin-hadoop2.7

## INSTALLATION

Installing Apache Spark and Python
Windows
1. Install a JDK (Java Development Kit) from http://www.oracle.com/technetwork/java/javase/downloads/index.html . You must install the JDK into a path with no spaces, for example c:\jdk. Be sure to change the default location for the installation!
2. Download a pre-built version of Apache Spark from https://spark.apache.org/downloads.html 3. If necessary, download and install WinRAR so you can extract the .tgz file you downloaded. http://www.rarlab.com/download.htm
4. Extract the Spark archive, and copy its contents into C:\spark after creating that directory. You should end up with directories like c:\spark\bin, c:\spark\conf, etc.
5. Download winutils.exe from https://sundog-spark.s3.amazonaws.com/winutils.exe and move it into a C:\winutils\bin folder that you’ve created. (note, this is a 64-bit application. If you are on a 32-bit version of Windows, you’ll need to search for a 32-bit build of winutils.exe for Hadoop.)
6. Open the the c:\spark\conf folder, and make sure “File Name Extensions” is checked in the “view” tab of Windows Explorer. Rename the log4j.properties.template file to log4j.properties.
Edit this file (using Wordpad or something similar) and change the error level from INFO to
ERROR for log4j.rootCategory
7. Right-click your Windows menu, select Control Panel, System and Security, and then System.
Click on “Advanced System Settings” and then the “Environment Variables” button.
8. Add the following new USER variables:
a. SPARK_HOME c:\spark
b. JAVA_HOME (the path you installed the JDK to in step 1, for example C:\JDK)
c. HADOOP HOME c:\winutils
9. Add the following paths to your PATH user variable:
%SPARK_HOME%\bin
%JAVA_HOME%\bin
10. Close the environment variable screen and the control panels.
11. Install the latest Enthought Canopy for Python 3.5 from https://store.enthought.com/downloads/#default Don’t install a Python 2.7 version!
12. Test it out!
a. Open up Canopy and select “Canopy Command Prompt” from the Tools menu.
b. Enter cd c:\spark and then dir to get a directory listing.
c. Look for a text file we can play with, like README.md or CHANGES.txt
d. Enter pyspark
e. At this point you should have a >>> prompt. If not, double check the steps above.
f. Enter rdd = sc.textFile(“README.md”) (or whatever text file you’ve found)
g. Enter rdd.count()
h. You should get a count of the number of lines in that file! Congratulations, you just ran your first Spark program!
i. Enter quit() to exit the spark shell, and close the console window
j. You’ve got everything set up! Hooray!
MacOS
1. Install Apache Spark using Homebrew.
a. Install Homebrew if you don’t have it already by entering this from a terminal prompt: /usr/bin/ruby -e "$(curl -fsSL
https://raw.githubusercontent.com/Homebrew/install/master/install)"
b. Enter brew install apache-spark
c. Create a log4j.properties file via cd /usr/local/Cellar/apache-spark/2.0.0/libexec/conf cp log4j.properties.template log4j.properties
(substituted 2.0.0 for the version actually installed)
d. Edit the log4j.properties file and change the log level from INFO to ERROR on log4j.rootCategory.
2. Install the latest Enthought Canopy for Python 3.5 from https://store.enthought.com/downloads/#default
3. Test it out!
a. Open up a terminal
b. Enter cd c:\spark and then dir to get a directory listing.
c. Look for a text file we can play with, like README.md or CHANGES.txt
d. Enter pyspark
e. At this point you should have a >>> prompt. If not, double check the steps above.
f. Enter rdd = sc.textFile(“README.md”) (or whatever text file you’ve found)
g. Enter rdd.count()
h. You should get a count of the number of lines in that file! Congratulations, you just ran your first Spark program!
i. Enter quit() to exit the spark shell, and close the terminal window
j. You’ve got everything set up! Hooray!
Linux
1. Install Java, Scala, and Spark according to the particulars of your specific OS. A good starting point is http://www.tutorialspoint.com/apache_spark/apache_spark_installation.htm (but be sure to install Spark 2.0 or newer)
2. Install the latest Enthought Canopy for Python 3.5 from https://store.enthought.com/downloads/#default 3. Test it out!
a. Open up a terminal
b. Enter cd c:\spark and then dir to get a directory listing.
c. Look for a text file we can play with, like README.md or CHANGES.txt
d. Enter pyspark
e. At this point you should have a >>> prompt. If not, double check the steps above.
f. Enter rdd = sc.textFile(“README.md”) (or whatever text file you’ve found)
g. Enter rdd.count()
h. You should get a count of the number of lines in that file! Congratulations, you just ran your first Spark program!
i. Enter quit() to exit the spark shell, and close the console window
j. You’ve got everything set up! Hooray!

# Apache Spark

Spark is a fast and general cluster computing system for Big Data. It provides
high-level APIs in Scala, Java, Python, and R, and an optimized engine that
supports general computation graphs for data analysis. It also supports a
rich set of higher-level tools including Spark SQL for SQL and DataFrames,
MLlib for machine learning, GraphX for graph processing,
and Spark Streaming for stream processing.

<http://spark.apache.org/>


## Online Documentation

You can find the latest Spark documentation, including a programming
guide, on the [project web page](http://spark.apache.org/documentation.html).
This README file only contains basic setup instructions.

## Building Spark

Spark is built using [Apache Maven](http://maven.apache.org/).
To build Spark and its example programs, run:

    build/mvn -DskipTests clean package

(You do not need to do this if you downloaded a pre-built package.)

You can build Spark using more than one thread by using the -T option with Maven, see ["Parallel builds in Maven 3"](https://cwiki.apache.org/confluence/display/MAVEN/Parallel+builds+in+Maven+3).
More detailed documentation is available from the project site, at
["Building Spark"](http://spark.apache.org/docs/latest/building-spark.html).

For general development tips, including info on developing Spark using an IDE, see ["Useful Developer Tools"](http://spark.apache.org/developer-tools.html).

## Interactive Scala Shell

The easiest way to start using Spark is through the Scala shell:

    ./bin/spark-shell

Try the following command, which should return 1000:

    scala> sc.parallelize(1 to 1000).count()

## Interactive Python Shell

Alternatively, if you prefer Python, you can use the Python shell:

    ./bin/pyspark

And run the following command, which should also return 1000:

    >>> sc.parallelize(range(1000)).count()

## Example Programs

Spark also comes with several sample programs in the `examples` directory.
To run one of them, use `./bin/run-example <class> [params]`. For example:

    ./bin/run-example SparkPi

will run the Pi example locally.

You can set the MASTER environment variable when running examples to submit
examples to a cluster. This can be a mesos:// or spark:// URL,
"yarn" to run on YARN, and "local" to run
locally with one thread, or "local[N]" to run locally with N threads. You
can also use an abbreviated class name if the class is in the `examples`
package. For instance:

    MASTER=spark://host:7077 ./bin/run-example SparkPi

Many of the example programs print usage help if no params are given.

## Running Tests

Testing first requires [building Spark](#building-spark). Once Spark is built, tests
can be run using:

    ./dev/run-tests

Please see the guidance on how to
[run tests for a module, or individual tests](http://spark.apache.org/developer-tools.html#individual-tests).

There is also a Kubernetes integration test, see resource-managers/kubernetes/integration-tests/README.md

## A Note About Hadoop Versions

Spark uses the Hadoop core library to talk to HDFS and other Hadoop-supported
storage systems. Because the protocols have changed in different versions of
Hadoop, you must build Spark against the same version that your cluster runs.

Please refer to the build documentation at
["Specifying the Hadoop Version and Enabling YARN"](http://spark.apache.org/docs/latest/building-spark.html#specifying-the-hadoop-version-and-enabling-yarn)
for detailed guidance on building for a particular distribution of Hadoop, including
building for particular Hive and Hive Thriftserver distributions.

## Configuration

Please refer to the [Configuration Guide](http://spark.apache.org/docs/latest/configuration.html)
in the online documentation for an overview on how to configure Spark.

## Contributing

Please review the [Contribution to Spark guide](http://spark.apache.org/contributing.html)
for information on how to get started contributing to the project.

## RELEASE

Spark 2.4.4 built for Hadoop 2.7.3
Build flags: -B -Pmesos -Pyarn -Pkubernetes -Pflume -Psparkr -Pkafka-0-8 -Phadoop-2.7 -Phive -Phive-thriftserver -DzincPort=3036

## LICENSE

                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

------------------------------------------------------------------------------------
This project bundles some components that are also licensed under the Apache
License Version 2.0:

commons-beanutils:commons-beanutils
org.apache.zookeeper:zookeeper
oro:oro
commons-configuration:commons-configuration
commons-digester:commons-digester
com.chuusai:shapeless_2.11
com.googlecode.javaewah:JavaEWAH
com.twitter:chill-java
com.twitter:chill_2.11
com.univocity:univocity-parsers
javax.jdo:jdo-api
joda-time:joda-time
net.sf.opencsv:opencsv
org.apache.derby:derby
org.objenesis:objenesis
org.roaringbitmap:RoaringBitmap
org.scalanlp:breeze-macros_2.11
org.scalanlp:breeze_2.11
org.typelevel:macro-compat_2.11
org.yaml:snakeyaml
org.apache.xbean:xbean-asm5-shaded
com.squareup.okhttp3:logging-interceptor
com.squareup.okhttp3:okhttp
com.squareup.okio:okio
org.apache.spark:spark-catalyst_2.11
org.apache.spark:spark-kvstore_2.11
org.apache.spark:spark-launcher_2.11
org.apache.spark:spark-mllib-local_2.11
org.apache.spark:spark-network-common_2.11
org.apache.spark:spark-network-shuffle_2.11
org.apache.spark:spark-sketch_2.11
org.apache.spark:spark-tags_2.11
org.apache.spark:spark-unsafe_2.11
commons-httpclient:commons-httpclient
com.vlkan:flatbuffers
com.ning:compress-lzf
io.airlift:aircompressor
io.dropwizard.metrics:metrics-core
io.dropwizard.metrics:metrics-ganglia
io.dropwizard.metrics:metrics-graphite
io.dropwizard.metrics:metrics-json
io.dropwizard.metrics:metrics-jvm
org.iq80.snappy:snappy
com.clearspring.analytics:stream
com.jamesmurty.utils:java-xmlbuilder
commons-codec:commons-codec
commons-collections:commons-collections
io.fabric8:kubernetes-client
io.fabric8:kubernetes-model
io.netty:netty
io.netty:netty-all
net.hydromatic:eigenbase-properties
net.sf.supercsv:super-csv
org.apache.arrow:arrow-format
org.apache.arrow:arrow-memory
org.apache.arrow:arrow-vector
org.apache.calcite:calcite-avatica
org.apache.calcite:calcite-core
org.apache.calcite:calcite-linq4j
org.apache.commons:commons-crypto
org.apache.commons:commons-lang3
org.apache.hadoop:hadoop-annotations
org.apache.hadoop:hadoop-auth
org.apache.hadoop:hadoop-client
org.apache.hadoop:hadoop-common
org.apache.hadoop:hadoop-hdfs
org.apache.hadoop:hadoop-mapreduce-client-app
org.apache.hadoop:hadoop-mapreduce-client-common
org.apache.hadoop:hadoop-mapreduce-client-core
org.apache.hadoop:hadoop-mapreduce-client-jobclient
org.apache.hadoop:hadoop-mapreduce-client-shuffle
org.apache.hadoop:hadoop-yarn-api
org.apache.hadoop:hadoop-yarn-client
org.apache.hadoop:hadoop-yarn-common
org.apache.hadoop:hadoop-yarn-server-common
org.apache.hadoop:hadoop-yarn-server-web-proxy
org.apache.httpcomponents:httpclient
org.apache.httpcomponents:httpcore
org.apache.orc:orc-core
org.apache.orc:orc-mapreduce
org.mortbay.jetty:jetty
org.mortbay.jetty:jetty-util
com.jolbox:bonecp
org.json4s:json4s-ast_2.11
org.json4s:json4s-core_2.11
org.json4s:json4s-jackson_2.11
org.json4s:json4s-scalap_2.11
com.carrotsearch:hppc
com.fasterxml.jackson.core:jackson-annotations
com.fasterxml.jackson.core:jackson-core
com.fasterxml.jackson.core:jackson-databind
com.fasterxml.jackson.dataformat:jackson-dataformat-yaml
com.fasterxml.jackson.module:jackson-module-jaxb-annotations
com.fasterxml.jackson.module:jackson-module-paranamer
com.fasterxml.jackson.module:jackson-module-scala_2.11
com.github.mifmif:generex
com.google.code.findbugs:jsr305
com.google.code.gson:gson
com.google.inject:guice
com.google.inject.extensions:guice-servlet
com.twitter:parquet-hadoop-bundle
commons-cli:commons-cli
commons-dbcp:commons-dbcp
commons-io:commons-io
commons-lang:commons-lang
commons-logging:commons-logging
commons-net:commons-net
commons-pool:commons-pool
io.fabric8:zjsonpatch
javax.inject:javax.inject
javax.validation:validation-api
log4j:apache-log4j-extras
log4j:log4j
net.sf.jpam:jpam
org.apache.avro:avro
org.apache.avro:avro-ipc
org.apache.avro:avro-mapred
org.apache.commons:commons-compress
org.apache.commons:commons-math3
org.apache.curator:curator-client
org.apache.curator:curator-framework
org.apache.curator:curator-recipes
org.apache.directory.api:api-asn1-api
org.apache.directory.api:api-util
org.apache.directory.server:apacheds-i18n
org.apache.directory.server:apacheds-kerberos-codec
org.apache.htrace:htrace-core
org.apache.ivy:ivy
org.apache.mesos:mesos
org.apache.parquet:parquet-column
org.apache.parquet:parquet-common
org.apache.parquet:parquet-encoding
org.apache.parquet:parquet-format
org.apache.parquet:parquet-hadoop
org.apache.parquet:parquet-jackson
org.apache.thrift:libfb303
org.apache.thrift:libthrift
org.codehaus.jackson:jackson-core-asl
org.codehaus.jackson:jackson-mapper-asl
org.datanucleus:datanucleus-api-jdo
org.datanucleus:datanucleus-core
org.datanucleus:datanucleus-rdbms
org.lz4:lz4-java
org.spark-project.hive:hive-beeline
org.spark-project.hive:hive-cli
org.spark-project.hive:hive-exec
org.spark-project.hive:hive-jdbc
org.spark-project.hive:hive-metastore
org.xerial.snappy:snappy-java
stax:stax-api
xerces:xercesImpl
org.codehaus.jackson:jackson-jaxrs
org.codehaus.jackson:jackson-xc
org.eclipse.jetty:jetty-client
org.eclipse.jetty:jetty-continuation
org.eclipse.jetty:jetty-http
org.eclipse.jetty:jetty-io
org.eclipse.jetty:jetty-jndi
org.eclipse.jetty:jetty-plus
org.eclipse.jetty:jetty-proxy
org.eclipse.jetty:jetty-security
org.eclipse.jetty:jetty-server
org.eclipse.jetty:jetty-servlet
org.eclipse.jetty:jetty-servlets
org.eclipse.jetty:jetty-util
org.eclipse.jetty:jetty-webapp
org.eclipse.jetty:jetty-xml

core/src/main/java/org/apache/spark/util/collection/TimSort.java
core/src/main/resources/org/apache/spark/ui/static/bootstrap*
core/src/main/resources/org/apache/spark/ui/static/jsonFormatter*
core/src/main/resources/org/apache/spark/ui/static/vis*
docs/js/vendor/bootstrap.js


------------------------------------------------------------------------------------
This product bundles various third-party components under other open source licenses.
This section summarizes those components and their licenses. See licenses-binary/
for text of these licenses.


BSD 2-Clause
------------

com.github.luben:zstd-jni
javolution:javolution
com.esotericsoftware:kryo-shaded
com.esotericsoftware:minlog
com.esotericsoftware:reflectasm
com.google.protobuf:protobuf-java
org.codehaus.janino:commons-compiler
org.codehaus.janino:janino
jline:jline
org.jodd:jodd-core


BSD 3-Clause
------------

dk.brics.automaton:automaton
org.antlr:antlr-runtime
org.antlr:ST4
org.antlr:stringtemplate
org.antlr:antlr4-runtime
antlr:antlr
com.github.fommil.netlib:core
com.thoughtworks.paranamer:paranamer
org.scala-lang:scala-compiler
org.scala-lang:scala-library
org.scala-lang:scala-reflect
org.scala-lang.modules:scala-parser-combinators_2.11
org.scala-lang.modules:scala-xml_2.11
org.fusesource.leveldbjni:leveldbjni-all
net.sourceforge.f2j:arpack_combined_all
xmlenc:xmlenc
net.sf.py4j:py4j
org.jpmml:pmml-model
org.jpmml:pmml-schema

python/lib/py4j-*-src.zip
python/pyspark/cloudpickle.py
python/pyspark/join.py
core/src/main/resources/org/apache/spark/ui/static/d3.min.js

The CSS style for the navigation sidebar of the documentation was originally
submitted by Óscar Nájera for the scikit-learn project. The scikit-learn project
is distributed under the 3-Clause BSD license.


MIT License
-----------

org.spire-math:spire-macros_2.11
org.spire-math:spire_2.11
org.typelevel:machinist_2.11
net.razorvine:pyrolite
org.slf4j:jcl-over-slf4j
org.slf4j:jul-to-slf4j
org.slf4j:slf4j-api
org.slf4j:slf4j-log4j12
com.github.scopt:scopt_2.11

core/src/main/resources/org/apache/spark/ui/static/dagre-d3.min.js
core/src/main/resources/org/apache/spark/ui/static/*dataTables*
core/src/main/resources/org/apache/spark/ui/static/graphlib-dot.min.js
ore/src/main/resources/org/apache/spark/ui/static/jquery*
core/src/main/resources/org/apache/spark/ui/static/sorttable.js
docs/js/vendor/anchor.min.js
docs/js/vendor/jquery*
docs/js/vendor/modernizer*


Common Development and Distribution License (CDDL) 1.0
------------------------------------------------------

javax.activation:activation  http://www.oracle.com/technetwork/java/javase/tech/index-jsp-138795.html
javax.xml.stream:stax-api    https://jcp.org/en/jsr/detail?id=173


Common Development and Distribution License (CDDL) 1.1
------------------------------------------------------

javax.annotation:javax.annotation-api    https://jcp.org/en/jsr/detail?id=250
javax.servlet:javax.servlet-api   https://javaee.github.io/servlet-spec/
javax.transaction:jta http://www.oracle.com/technetwork/java/index.html
javax.ws.rs:javax.ws.rs-api https://github.com/jax-rs
javax.xml.bind:jaxb-api    https://github.com/javaee/jaxb-v2
org.glassfish.hk2:hk2-api https://github.com/javaee/glassfish
org.glassfish.hk2:hk2-locator (same)
org.glassfish.hk2:hk2-utils
org.glassfish.hk2:osgi-resource-locator
org.glassfish.hk2.external:aopalliance-repackaged
org.glassfish.hk2.external:javax.inject
org.glassfish.jersey.bundles.repackaged:jersey-guava
org.glassfish.jersey.containers:jersey-container-servlet
org.glassfish.jersey.containers:jersey-container-servlet-core
org.glassfish.jersey.core:jersey-client
org.glassfish.jersey.core:jersey-common
org.glassfish.jersey.core:jersey-server
org.glassfish.jersey.media:jersey-media-jaxb


Mozilla Public License (MPL) 1.1
--------------------------------

com.github.rwl:jtransforms https://sourceforge.net/projects/jtransforms/


Python Software Foundation License
----------------------------------

pyspark/heapq3.py


Public Domain
-------------

aopalliance:aopalliance
net.iharder:base64
org.tukaani:xz


Creative Commons CC0 1.0 Universal Public Domain Dedication
-----------------------------------------------------------
(see LICENSE-CC0.txt)

data/mllib/images/kittens/29.5.a_b_EGDP022204.jpg
data/mllib/images/kittens/54893.jpg
data/mllib/images/kittens/DP153539.jpg
data/mllib/images/kittens/DP802813.jpg
data/mllib/images/multi-channel/chr30.4.184.jpg

Apache Spark
Copyright 2014 and onwards The Apache Software Foundation.

This product includes software developed at
The Apache Software Foundation (http://www.apache.org/).


Export Control Notice
---------------------

This distribution includes cryptographic software. The country in which you currently reside may have
restrictions on the import, possession, use, and/or re-export to another country, of encryption software.
BEFORE using any encryption software, please check your country's laws, regulations and policies concerning
the import, possession, or use, and re-export of encryption software, to see if this is permitted. See
<http://www.wassenaar.org/> for more information.

The U.S. Government Department of Commerce, Bureau of Industry and Security (BIS), has classified this
software as Export Commodity Control Number (ECCN) 5D002.C.1, which includes information security software
using or performing cryptographic functions with asymmetric algorithms. The form and manner of this Apache
Software Foundation distribution makes it eligible for export under the License Exception ENC Technology
Software Unrestricted (TSU) exception (see the BIS Export Administration Regulations, Section 740.13) for
both object code and source code.

The following provides more details on the included cryptographic software:

This software uses Apache Commons Crypto (https://commons.apache.org/proper/commons-crypto/) to
support authentication, and encryption and decryption of data sent across the network between
services.


// ------------------------------------------------------------------
// NOTICE file corresponding to the section 4d of The Apache License,
// Version 2.0, in this case for
// ------------------------------------------------------------------

Hive Beeline
Copyright 2016 The Apache Software Foundation

This product includes software developed at
The Apache Software Foundation (http://www.apache.org/).

Apache Avro
Copyright 2009-2014 The Apache Software Foundation

This product currently only contains code developed by authors
of specific components, as identified by the source code files;
if such notes are missing files have been created by
Tatu Saloranta.

For additional credits (generally to people who reported problems)
see CREDITS file.

Apache Commons Compress
Copyright 2002-2012 The Apache Software Foundation

This product includes software developed by
The Apache Software Foundation (http://www.apache.org/).

Apache Avro Mapred API
Copyright 2009-2014 The Apache Software Foundation

Apache Avro IPC
Copyright 2009-2014 The Apache Software Foundation

Objenesis
Copyright 2006-2013 Joe Walnes, Henri Tremblay, Leonardo Mesquita

Apache XBean :: ASM 5 shaded (repackaged)
Copyright 2005-2015 The Apache Software Foundation

--------------------------------------

This product includes software developed at
OW2 Consortium (http://asm.ow2.org/)

This product includes software developed by The Apache Software
Foundation (http://www.apache.org/).

The binary distribution of this product bundles binaries of
org.iq80.leveldb:leveldb-api (https://github.com/dain/leveldb), which has the
following notices:
* Copyright 2011 Dain Sundstrom <dain@iq80.com>
* Copyright 2011 FuseSource Corp. http://fusesource.com

The binary distribution of this product bundles binaries of
org.fusesource.hawtjni:hawtjni-runtime (https://github.com/fusesource/hawtjni),
which has the following notices:
* This product includes software developed by FuseSource Corp.
  http://fusesource.com
* This product includes software developed at
  Progress Software Corporation and/or its  subsidiaries or affiliates.
* This product includes software developed by IBM Corporation and others.

The binary distribution of this product bundles binaries of
Gson 2.2.4,
which has the following notices:

                            The Netty Project
                            =================

Please visit the Netty web site for more information:

  * http://netty.io/

Copyright 2014 The Netty Project

The Netty Project licenses this file to you under the Apache License,
version 2.0 (the "License"); you may not use this file except in compliance
with the License. You may obtain a copy of the License at:

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
License for the specific language governing permissions and limitations
under the License.

Also, please refer to each LICENSE.<component>.txt file, which is located in
the 'license' directory of the distribution file, for the license terms of the
components that this product depends on.

-------------------------------------------------------------------------------
This product contains the extensions to Java Collections Framework which has
been derived from the works by JSR-166 EG, Doug Lea, and Jason T. Greene:

  * LICENSE:
    * license/LICENSE.jsr166y.txt (Public Domain)
  * HOMEPAGE:
    * http://gee.cs.oswego.edu/cgi-bin/viewcvs.cgi/jsr166/
    * http://viewvc.jboss.org/cgi-bin/viewvc.cgi/jbosscache/experimental/jsr166/

This product contains a modified version of Robert Harder's Public Domain
Base64 Encoder and Decoder, which can be obtained at:

  * LICENSE:
    * license/LICENSE.base64.txt (Public Domain)
  * HOMEPAGE:
    * http://iharder.sourceforge.net/current/java/base64/

This product contains a modified portion of 'Webbit', an event based
WebSocket and HTTP server, which can be obtained at:

  * LICENSE:
    * license/LICENSE.webbit.txt (BSD License)
  * HOMEPAGE:
    * https://github.com/joewalnes/webbit

This product contains a modified portion of 'SLF4J', a simple logging
facade for Java, which can be obtained at:

  * LICENSE:
    * license/LICENSE.slf4j.txt (MIT License)
  * HOMEPAGE:
    * http://www.slf4j.org/

This product contains a modified portion of 'ArrayDeque', written by Josh
Bloch of Google, Inc:

  * LICENSE:
    * license/LICENSE.deque.txt (Public Domain)

This product contains a modified portion of 'Apache Harmony', an open source
Java SE, which can be obtained at:

  * LICENSE:
    * license/LICENSE.harmony.txt (Apache License 2.0)
  * HOMEPAGE:
    * http://archive.apache.org/dist/harmony/

This product contains a modified version of Roland Kuhn's ASL2
AbstractNodeQueue, which is based on Dmitriy Vyukov's non-intrusive MPSC queue.
It can be obtained at:

  * LICENSE:
    * license/LICENSE.abstractnodequeue.txt (Public Domain)
  * HOMEPAGE:
    * https://github.com/akka/akka/blob/wip-2.2.3-for-scala-2.11/akka-actor/src/main/java/akka/dispatch/AbstractNodeQueue.java

This product contains a modified portion of 'jbzip2', a Java bzip2 compression
and decompression library written by Matthew J. Francis. It can be obtained at:

  * LICENSE:
    * license/LICENSE.jbzip2.txt (MIT License)
  * HOMEPAGE:
    * https://code.google.com/p/jbzip2/

This product contains a modified portion of 'libdivsufsort', a C API library to construct
the suffix array and the Burrows-Wheeler transformed string for any input string of
a constant-size alphabet written by Yuta Mori. It can be obtained at:

  * LICENSE:
    * license/LICENSE.libdivsufsort.txt (MIT License)
  * HOMEPAGE:
    * https://code.google.com/p/libdivsufsort/

This product contains a modified portion of Nitsan Wakart's 'JCTools', Java Concurrency Tools for the JVM,
 which can be obtained at:

  * LICENSE:
    * license/LICENSE.jctools.txt (ASL2 License)
  * HOMEPAGE:
    * https://github.com/JCTools/JCTools

This product optionally depends on 'JZlib', a re-implementation of zlib in
pure Java, which can be obtained at:

  * LICENSE:
    * license/LICENSE.jzlib.txt (BSD style License)
  * HOMEPAGE:
    * http://www.jcraft.com/jzlib/

This product optionally depends on 'Compress-LZF', a Java library for encoding and
decoding data in LZF format, written by Tatu Saloranta. It can be obtained at:

  * LICENSE:
    * license/LICENSE.compress-lzf.txt (Apache License 2.0)
  * HOMEPAGE:
    * https://github.com/ning/compress

This product optionally depends on 'lz4', a LZ4 Java compression
and decompression library written by Adrien Grand. It can be obtained at:

  * LICENSE:
    * license/LICENSE.lz4.txt (Apache License 2.0)
  * HOMEPAGE:
    * https://github.com/jpountz/lz4-java

This product optionally depends on 'lzma-java', a LZMA Java compression
and decompression library, which can be obtained at:

  * LICENSE:
    * license/LICENSE.lzma-java.txt (Apache License 2.0)
  * HOMEPAGE:
    * https://github.com/jponge/lzma-java

This product contains a modified portion of 'jfastlz', a Java port of FastLZ compression
and decompression library written by William Kinney. It can be obtained at:

  * LICENSE:
    * license/LICENSE.jfastlz.txt (MIT License)
  * HOMEPAGE:
    * https://code.google.com/p/jfastlz/

This product contains a modified portion of and optionally depends on 'Protocol Buffers', Google's data
interchange format, which can be obtained at:

  * LICENSE:
    * license/LICENSE.protobuf.txt (New BSD License)
  * HOMEPAGE:
    * http://code.google.com/p/protobuf/

This product optionally depends on 'Bouncy Castle Crypto APIs' to generate
a temporary self-signed X.509 certificate when the JVM does not provide the
equivalent functionality.  It can be obtained at:

  * LICENSE:
    * license/LICENSE.bouncycastle.txt (MIT License)
  * HOMEPAGE:
    * http://www.bouncycastle.org/

This product optionally depends on 'Snappy', a compression library produced
by Google Inc, which can be obtained at:

  * LICENSE:
    * license/LICENSE.snappy.txt (New BSD License)
  * HOMEPAGE:
    * http://code.google.com/p/snappy/

This product optionally depends on 'JBoss Marshalling', an alternative Java
serialization API, which can be obtained at:

  * LICENSE:
    * license/LICENSE.jboss-marshalling.txt (GNU LGPL 2.1)
  * HOMEPAGE:
    * http://www.jboss.org/jbossmarshalling

This product optionally depends on 'Caliper', Google's micro-
benchmarking framework, which can be obtained at:

  * LICENSE:
    * license/LICENSE.caliper.txt (Apache License 2.0)
  * HOMEPAGE:
    * http://code.google.com/p/caliper/

This product optionally depends on 'Apache Commons Logging', a logging
framework, which can be obtained at:

  * LICENSE:
    * license/LICENSE.commons-logging.txt (Apache License 2.0)
  * HOMEPAGE:
    * http://commons.apache.org/logging/

This product optionally depends on 'Apache Log4J', a logging framework, which
can be obtained at:

  * LICENSE:
    * license/LICENSE.log4j.txt (Apache License 2.0)
  * HOMEPAGE:
    * http://logging.apache.org/log4j/

This product optionally depends on 'Aalto XML', an ultra-high performance
non-blocking XML processor, which can be obtained at:

  * LICENSE:
    * license/LICENSE.aalto-xml.txt (Apache License 2.0)
  * HOMEPAGE:
    * http://wiki.fasterxml.com/AaltoHome

This product contains a modified version of 'HPACK', a Java implementation of
the HTTP/2 HPACK algorithm written by Twitter. It can be obtained at:

  * LICENSE:
    * license/LICENSE.hpack.txt (Apache License 2.0)
  * HOMEPAGE:
    * https://github.com/twitter/hpack

This product contains a modified portion of 'Apache Commons Lang', a Java library
provides utilities for the java.lang API, which can be obtained at:

  * LICENSE:
    * license/LICENSE.commons-lang.txt (Apache License 2.0)
  * HOMEPAGE:
    * https://commons.apache.org/proper/commons-lang/

The binary distribution of this product bundles binaries of
Commons Codec 1.4,
which has the following notices:
 * src/test/org/apache/commons/codec/language/DoubleMetaphoneTest.javacontains test data from http://aspell.net/test/orig/batch0.tab.Copyright (C) 2002 Kevin Atkinson (kevina@gnu.org)
  ===============================================================================
  The content of package org.apache.commons.codec.language.bm has been translated
  from the original php source code available at http://stevemorse.org/phoneticinfo.htm
  with permission from the original authors.
  Original source copyright:Copyright (c) 2008 Alexander Beider & Stephen P. Morse.

The binary distribution of this product bundles binaries of
Commons Lang 2.6,
which has the following notices:
 * This product includes software from the Spring Framework,under the Apache License 2.0 (see: StringUtils.containsWhitespace())

The binary distribution of this product bundles binaries of
Apache Log4j 1.2.17,
which has the following notices:
 * ResolverUtil.java
    Copyright 2005-2006 Tim Fennell
  Dumbster SMTP test server
    Copyright 2004 Jason Paul Kitchen
  TypeUtil.java
    Copyright 2002-2012 Ramnivas Laddad, Juergen Hoeller, Chris Beams

The binary distribution of this product bundles binaries of
Jetty 6.1.26,
which has the following notices:
 * ==============================================================
    Jetty Web Container
    Copyright 1995-2016 Mort Bay Consulting Pty Ltd.
   ==============================================================

   The Jetty Web Container is Copyright Mort Bay Consulting Pty Ltd
   unless otherwise noted.

   Jetty is dual licensed under both

     * The Apache 2.0 License
       http://www.apache.org/licenses/LICENSE-2.0.html

         and

     * The Eclipse Public 1.0 License
       http://www.eclipse.org/legal/epl-v10.html

   Jetty may be distributed under either license.

   ------
   Eclipse

   The following artifacts are EPL.
    * org.eclipse.jetty.orbit:org.eclipse.jdt.core

   The following artifacts are EPL and ASL2.
    * org.eclipse.jetty.orbit:javax.security.auth.message

   The following artifacts are EPL and CDDL 1.0.
    * org.eclipse.jetty.orbit:javax.mail.glassfish

   ------
   Oracle

   The following artifacts are CDDL + GPLv2 with classpath exception.
   https://glassfish.dev.java.net/nonav/public/CDDL+GPL.html

    * javax.servlet:javax.servlet-api
    * javax.annotation:javax.annotation-api
    * javax.transaction:javax.transaction-api
    * javax.websocket:javax.websocket-api

   ------
   Oracle OpenJDK

   If ALPN is used to negotiate HTTP/2 connections, then the following
   artifacts may be included in the distribution or downloaded when ALPN
   module is selected.

    * java.sun.security.ssl

   These artifacts replace/modify OpenJDK classes.  The modififications
   are hosted at github and both modified and original are under GPL v2 with
   classpath exceptions.
   http://openjdk.java.net/legal/gplv2+ce.html

   ------
   OW2

   The following artifacts are licensed by the OW2 Foundation according to the
   terms of http://asm.ow2.org/license.html

   org.ow2.asm:asm-commons
   org.ow2.asm:asm

   ------
   Apache

   The following artifacts are ASL2 licensed.

   org.apache.taglibs:taglibs-standard-spec
   org.apache.taglibs:taglibs-standard-impl

   ------
   MortBay

   The following artifacts are ASL2 licensed.  Based on selected classes from
   following Apache Tomcat jars, all ASL2 licensed.

   org.mortbay.jasper:apache-jsp
     org.apache.tomcat:tomcat-jasper
     org.apache.tomcat:tomcat-juli
     org.apache.tomcat:tomcat-jsp-api
     org.apache.tomcat:tomcat-el-api
     org.apache.tomcat:tomcat-jasper-el
     org.apache.tomcat:tomcat-api
     org.apache.tomcat:tomcat-util-scan
     org.apache.tomcat:tomcat-util

   org.mortbay.jasper:apache-el
     org.apache.tomcat:tomcat-jasper-el
     org.apache.tomcat:tomcat-el-api

   ------
   Mortbay

   The following artifacts are CDDL + GPLv2 with classpath exception.

   https://glassfish.dev.java.net/nonav/public/CDDL+GPL.html

   org.eclipse.jetty.toolchain:jetty-schemas

   ------
   Assorted

   The UnixCrypt.java code implements the one way cryptography used by
   Unix systems for simple password protection.  Copyright 1996 Aki Yoshida,
   modified April 2001  by Iris Van den Broeke, Daniel Deville.
   Permission to use, copy, modify and distribute UnixCrypt
   for non-commercial or commercial purposes and without fee is
   granted provided that the copyright notice appears in all copies./

The binary distribution of this product bundles binaries of
Snappy for Java 1.0.4.1,
which has the following notices:
 * This product includes software developed by Google
    Snappy: http://code.google.com/p/snappy/ (New BSD License)

   This product includes software developed by Apache
    PureJavaCrc32C from apache-hadoop-common http://hadoop.apache.org/
    (Apache 2.0 license)

   This library contains statically linked libstdc++. This inclusion is allowed by
   "GCC RUntime Library Exception"
   http://gcc.gnu.org/onlinedocs/libstdc++/manual/license.html

   == Contributors ==
     * Tatu Saloranta
       * Providing benchmark suite
     * Alec Wysoker
       * Performance and memory usage improvement

The binary distribution of this product bundles binaries of
Xerces2 Java Parser 2.9.1,
which has the following notices:
 * =========================================================================
   ==  NOTICE file corresponding to section 4(d) of the Apache License,   ==
   ==  Version 2.0, in this case for the Apache Xerces Java distribution. ==
   =========================================================================

   Apache Xerces Java
   Copyright 1999-2007 The Apache Software Foundation

   This product includes software developed at
   The Apache Software Foundation (http://www.apache.org/).

   Portions of this software were originally based on the following:
     - software copyright (c) 1999, IBM Corporation., http://www.ibm.com.
     - software copyright (c) 1999, Sun Microsystems., http://www.sun.com.
     - voluntary contributions made by Paul Eng on behalf of the
       Apache Software Foundation that were originally developed at iClick, Inc.,
       software copyright (c) 1999.

Apache Commons Collections
Copyright 2001-2015 The Apache Software Foundation

Apache Commons Configuration
Copyright 2001-2008 The Apache Software Foundation

Apache Jakarta Commons Digester
Copyright 2001-2006 The Apache Software Foundation

Apache Commons BeanUtils
Copyright 2000-2008 The Apache Software Foundation

ApacheDS Protocol Kerberos Codec
Copyright 2003-2013 The Apache Software Foundation

ApacheDS I18n
Copyright 2003-2013 The Apache Software Foundation

Apache Directory API ASN.1 API
Copyright 2003-2013 The Apache Software Foundation

Apache Directory LDAP API Utilities
Copyright 2003-2013 The Apache Software Foundation

Curator Client
Copyright 2011-2015 The Apache Software Foundation

htrace-core
Copyright 2015 The Apache Software Foundation

   =========================================================================
   ==  NOTICE file corresponding to section 4(d) of the Apache License,   ==
   ==  Version 2.0, in this case for the Apache Xerces Java distribution. ==
   =========================================================================

   Portions of this software were originally based on the following:
     - software copyright (c) 1999, IBM Corporation., http://www.ibm.com.
     - software copyright (c) 1999, Sun Microsystems., http://www.sun.com.
     - voluntary contributions made by Paul Eng on behalf of the
       Apache Software Foundation that were originally developed at iClick, Inc.,
       software copyright (c) 1999.

# Jackson JSON processor

Jackson is a high-performance, Free/Open Source JSON processing library.
It was originally written by Tatu Saloranta (tatu.saloranta@iki.fi), and has
been in development since 2007.
It is currently developed by a community of developers, as well as supported
commercially by FasterXML.com.

## Licensing

Jackson core and extension components may licensed under different licenses.
To find the details that apply to this artifact see the accompanying LICENSE file.
For more information, including possible other licensing options, contact
FasterXML.com (http://fasterxml.com).

## Credits

A list of contributors may be found from CREDITS file, which is included
in some artifacts (usually source distributions); but is always available
from the source code management (SCM) system project uses.

Apache HttpCore
Copyright 2005-2017 The Apache Software Foundation

Curator Recipes
Copyright 2011-2015 The Apache Software Foundation

Curator Framework
Copyright 2011-2015 The Apache Software Foundation

Apache Commons Lang
Copyright 2001-2016 The Apache Software Foundation

This product includes software from the Spring Framework,
under the Apache License 2.0 (see: StringUtils.containsWhitespace())

Apache Commons Math
Copyright 2001-2015 The Apache Software Foundation

This product includes software developed for Orekit by
CS Systèmes d'Information (http://www.c-s.fr/)
Copyright 2010-2012 CS Systèmes d'Information

Apache log4j
Copyright 2007 The Apache Software Foundation

# Compress LZF

This library contains efficient implementation of LZF compression format,
as well as additional helper classes that build on JDK-provided gzip (deflat)
codec.

Library is licensed under Apache License 2.0, as per accompanying LICENSE file.

## Credit

Library has been written by Tatu Saloranta (tatu.saloranta@iki.fi).
It was started at Ning, inc., as an official Open Source process used by
platform backend, but after initial versions has been developed outside of
Ning by supporting community.

Other contributors include:

* Jon Hartlaub (first versions of streaming reader/writer; unit tests)
* Cedrik Lime: parallel LZF implementation

Various community members have contributed bug reports, and suggested minor
fixes; these can be found from file "VERSION.txt" in SCM.

Apache Commons Net
Copyright 2001-2012 The Apache Software Foundation

Copyright 2011 The Netty Project

http://www.apache.org/licenses/LICENSE-2.0

This product contains a modified version of 'JZlib', a re-implementation of
zlib in pure Java, which can be obtained at:

  * LICENSE:
    * license/LICENSE.jzlib.txt (BSD Style License)
  * HOMEPAGE:
    * http://www.jcraft.com/jzlib/

This product contains a modified version of 'Webbit', a Java event based
WebSocket and HTTP server:

This product optionally depends on 'Protocol Buffers', Google's data
interchange format, which can be obtained at:

This product optionally depends on 'SLF4J', a simple logging facade for Java,
which can be obtained at:

This product optionally depends on 'Apache Log4J', a logging framework,
which can be obtained at:

This product optionally depends on 'JBoss Logging', a logging framework,
which can be obtained at:

  * LICENSE:
    * license/LICENSE.jboss-logging.txt (GNU LGPL 2.1)
  * HOMEPAGE:
    * http://anonsvn.jboss.org/repos/common/common-logging-spi/

This product optionally depends on 'Apache Felix', an open source OSGi
framework implementation, which can be obtained at:

  * LICENSE:
    * license/LICENSE.felix.txt (Apache License 2.0)
  * HOMEPAGE:
    * http://felix.apache.org/

Jackson core and extension components may be licensed under different licenses.
To find the details that apply to this artifact see the accompanying LICENSE file.
For more information, including possible other licensing options, contact
FasterXML.com (http://fasterxml.com).

Apache Ivy (TM)
Copyright 2007-2014 The Apache Software Foundation

Portions of Ivy were originally developed at
Jayasoft SARL (http://www.jayasoft.fr/)
and are licensed to the Apache Software Foundation under the
"Software Grant License Agreement"

SSH and SFTP support is provided by the JCraft JSch package,
which is open source software, available under
the terms of a BSD style license.
The original software and related information is available
at http://www.jcraft.com/jsch/.


ORC Core
Copyright 2013-2018 The Apache Software Foundation

Apache Commons Lang
Copyright 2001-2011 The Apache Software Foundation

ORC MapReduce
Copyright 2013-2018 The Apache Software Foundation

Apache Parquet Format
Copyright 2017 The Apache Software Foundation

Arrow Vectors
Copyright 2017 The Apache Software Foundation

Arrow Format
Copyright 2017 The Apache Software Foundation

Arrow Memory
Copyright 2017 The Apache Software Foundation

Apache Commons CLI
Copyright 2001-2009 The Apache Software Foundation

Google Guice - Extensions - Servlet
Copyright 2006-2011 Google, Inc.

Apache Commons IO
Copyright 2002-2012 The Apache Software Foundation

Google Guice - Core Library
Copyright 2006-2011 Google, Inc.

mesos
Copyright 2017 The Apache Software Foundation

Apache Parquet Hadoop Bundle (Incubating)
Copyright 2015 The Apache Software Foundation

Hive Query Language
Copyright 2016 The Apache Software Foundation

Apache Extras Companion for log4j 1.2.
Copyright 2007 The Apache Software Foundation

Hive Metastore
Copyright 2016 The Apache Software Foundation

Apache Commons Logging
Copyright 2003-2013 The Apache Software Foundation

=========================================================================
==  NOTICE file corresponding to section 4(d) of the Apache License,   ==
==  Version 2.0, in this case for the DataNucleus distribution.        ==
=========================================================================

===================================================================
This product includes software developed by many individuals,
including the following:
===================================================================
Erik Bengtson
Andy Jefferson

===================================================================
This product has included contributions from some individuals,
including the following:
===================================================================

===================================================================
This product includes software developed by many individuals,
including the following:
===================================================================
Andy Jefferson
Erik Bengtson
Joerg von Frantzius
Marco Schulze

===================================================================
This product has included contributions from some individuals,
including the following:
===================================================================
Barry Haddow
Ralph Ullrich
David Ezzio
Brendan de Beer
David Eaves
Martin Taal
Tony Lai
Roland Szabo
Anton Troshin (Timesten)

===================================================================
This product also includes software developed by the TJDO project
(http://tjdo.sourceforge.net/).
===================================================================

===================================================================
This product also includes software developed by the Apache Commons project
(http://commons.apache.org/).
===================================================================

Apache Commons Pool
Copyright 1999-2009 The Apache Software Foundation

Apache Commons DBCP
Copyright 2001-2010 The Apache Software Foundation

Apache Java Data Objects (JDO)
Copyright 2005-2006 The Apache Software Foundation

Apache Jakarta HttpClient
Copyright 1999-2007 The Apache Software Foundation

Calcite Avatica
Copyright 2012-2015 The Apache Software Foundation

Calcite Core
Copyright 2012-2015 The Apache Software Foundation

Calcite Linq4j
Copyright 2012-2015 The Apache Software Foundation

Apache HttpClient
Copyright 1999-2017 The Apache Software Foundation

Apache Commons Codec
Copyright 2002-2014 The Apache Software Foundation

src/test/org/apache/commons/codec/language/DoubleMetaphoneTest.java
contains test data from http://aspell.net/test/orig/batch0.tab.
Copyright (C) 2002 Kevin Atkinson (kevina@gnu.org)

===============================================================================

The content of package org.apache.commons.codec.language.bm has been translated
from the original php source code available at http://stevemorse.org/phoneticinfo.htm
with permission from the original authors.
Original source copyright:
Copyright (c) 2008 Alexander Beider & Stephen P. Morse.

=============================================================================
= NOTICE file corresponding to section 4d of the Apache License Version 2.0 =
=============================================================================
This product includes software developed by
Joda.org (http://www.joda.org/).

===================================================================
This product has included contributions from some individuals,
including the following:
===================================================================
Joerg von Frantzius
Thomas Marti
Barry Haddow
Marco Schulze
Ralph Ullrich
David Ezzio
Brendan de Beer
David Eaves
Martin Taal
Tony Lai
Roland Szabo
Marcus Mennemeier
Xuan Baldauf
Eric Sultan

Apache Thrift
Copyright 2006-2010 The Apache Software Foundation.

=========================================================================
==  NOTICE file corresponding to section 4(d) of the Apache License,
==  Version 2.0, in this case for the Apache Derby distribution.
==
==  DO NOT EDIT THIS FILE DIRECTLY. IT IS GENERATED
==  BY THE buildnotice TARGET IN THE TOP LEVEL build.xml FILE.
==
=========================================================================

Apache Derby
Copyright 2004-2015 The Apache Software Foundation

=========================================================================

Portions of Derby were originally developed by
International Business Machines Corporation and are
licensed to the Apache Software Foundation under the
"Software Grant and Corporate Contribution License Agreement",
informally known as the "Derby CLA".
The following copyright notice(s) were affixed to portions of the code
with which this file is now or was at one time distributed
and are placed here unaltered.

(C) Copyright 1997,2004 International Business Machines Corporation.  All rights reserved.

(C) Copyright IBM Corp. 2003.

The portion of the functionTests under 'nist' was originally
developed by the National Institute of Standards and Technology (NIST),
an agency of the United States Department of Commerce, and adapted by
International Business Machines Corporation in accordance with the NIST
Software Acknowledgment and Redistribution document at
http://www.itl.nist.gov/div897/ctg/sql_form.htm

The JDBC apis for small devices and JDBC3 (under java/stubs/jsr169 and
java/stubs/jdbc3) were produced by trimming sources supplied by the
Apache Harmony project. In addition, the Harmony SerialBlob and
SerialClob implementations are used. The following notice covers the Harmony sources:

Portions of Harmony were originally developed by
Intel Corporation and are licensed to the Apache Software
Foundation under the "Software Grant and Corporate Contribution
License Agreement", informally known as the "Intel Harmony CLA".

The Derby build relies on source files supplied by the Apache Felix
project. The following notice covers the Felix files:

  Apache Felix Main
  Copyright 2008 The Apache Software Foundation

  I. Included Software

  This product includes software developed at
  The Apache Software Foundation (http://www.apache.org/).
  Licensed under the Apache License 2.0.

  This product includes software developed at
  The OSGi Alliance (http://www.osgi.org/).
  Copyright (c) OSGi Alliance (2000, 2007).
  Licensed under the Apache License 2.0.

  This product includes software from http://kxml.sourceforge.net.
  Copyright (c) 2002,2003, Stefan Haustein, Oberhausen, Rhld., Germany.
  Licensed under BSD License.

  II. Used Software

  This product uses software developed at
  The OSGi Alliance (http://www.osgi.org/).
  Copyright (c) OSGi Alliance (2000, 2007).
  Licensed under the Apache License 2.0.

  III. License Summary
  - Apache License 2.0
  - BSD License

The Derby build relies on jar files supplied by the Apache Lucene
project. The following notice covers the Lucene files:

Apache Lucene
Copyright 2013 The Apache Software Foundation

Includes software from other Apache Software Foundation projects,
including, but not limited to:
 - Apache Ant
 - Apache Jakarta Regexp
 - Apache Commons
 - Apache Xerces

ICU4J, (under analysis/icu) is licensed under an MIT styles license
and Copyright (c) 1995-2008 International Business Machines Corporation and others

Some data files (under analysis/icu/src/data) are derived from Unicode data such
as the Unicode Character Database. See http://unicode.org/copyright.html for more
details.

Brics Automaton (under core/src/java/org/apache/lucene/util/automaton) is
BSD-licensed, created by Anders Møller. See http://www.brics.dk/automaton/

The levenshtein automata tables (under core/src/java/org/apache/lucene/util/automaton) were
automatically generated with the moman/finenight FSA library, created by
Jean-Philippe Barrette-LaPierre. This library is available under an MIT license,
see http://sites.google.com/site/rrettesite/moman and
http://bitbucket.org/jpbarrette/moman/overview/

The class org.apache.lucene.util.WeakIdentityMap was derived from
the Apache CXF project and is Apache License 2.0.

The Google Code Prettify is Apache License 2.0.
See http://code.google.com/p/google-code-prettify/

JUnit (junit-4.10) is licensed under the Common Public License v. 1.0
See http://junit.sourceforge.net/cpl-v10.html

This product includes code (JaspellTernarySearchTrie) from Java Spelling Checkin
g Package (jaspell): http://jaspell.sourceforge.net/
License: The BSD License (http://www.opensource.org/licenses/bsd-license.php)

The snowball stemmers in
  analysis/common/src/java/net/sf/snowball
were developed by Martin Porter and Richard Boulton.
The snowball stopword lists in
  analysis/common/src/resources/org/apache/lucene/analysis/snowball
were developed by Martin Porter and Richard Boulton.
The full snowball package is available from
  http://snowball.tartarus.org/

The KStem stemmer in
  analysis/common/src/org/apache/lucene/analysis/en
was developed by Bob Krovetz and Sergio Guzman-Lara (CIIR-UMass Amherst)
under the BSD-license.

The Arabic,Persian,Romanian,Bulgarian, and Hindi analyzers (common) come with a default
stopword list that is BSD-licensed created by Jacques Savoy.  These files reside in:
analysis/common/src/resources/org/apache/lucene/analysis/ar/stopwords.txt,
analysis/common/src/resources/org/apache/lucene/analysis/fa/stopwords.txt,
analysis/common/src/resources/org/apache/lucene/analysis/ro/stopwords.txt,
analysis/common/src/resources/org/apache/lucene/analysis/bg/stopwords.txt,
analysis/common/src/resources/org/apache/lucene/analysis/hi/stopwords.txt
See http://members.unine.ch/jacques.savoy/clef/index.html.

The German,Spanish,Finnish,French,Hungarian,Italian,Portuguese,Russian and Swedish light stemmers
(common) are based on BSD-licensed reference implementations created by Jacques Savoy and
Ljiljana Dolamic. These files reside in:
analysis/common/src/java/org/apache/lucene/analysis/de/GermanLightStemmer.java
analysis/common/src/java/org/apache/lucene/analysis/de/GermanMinimalStemmer.java
analysis/common/src/java/org/apache/lucene/analysis/es/SpanishLightStemmer.java
analysis/common/src/java/org/apache/lucene/analysis/fi/FinnishLightStemmer.java
analysis/common/src/java/org/apache/lucene/analysis/fr/FrenchLightStemmer.java
analysis/common/src/java/org/apache/lucene/analysis/fr/FrenchMinimalStemmer.java
analysis/common/src/java/org/apache/lucene/analysis/hu/HungarianLightStemmer.java
analysis/common/src/java/org/apache/lucene/analysis/it/ItalianLightStemmer.java
analysis/common/src/java/org/apache/lucene/analysis/pt/PortugueseLightStemmer.java
analysis/common/src/java/org/apache/lucene/analysis/ru/RussianLightStemmer.java
analysis/common/src/java/org/apache/lucene/analysis/sv/SwedishLightStemmer.java

The Stempel analyzer (stempel) includes BSD-licensed software developed
by the Egothor project http://egothor.sf.net/, created by Leo Galambos, Martin Kvapil,
and Edmond Nolan.

The Polish analyzer (stempel) comes with a default
stopword list that is BSD-licensed created by the Carrot2 project. The file resides
in stempel/src/resources/org/apache/lucene/analysis/pl/stopwords.txt.
See http://project.carrot2.org/license.html.

The SmartChineseAnalyzer source code (smartcn) was
provided by Xiaoping Gao and copyright 2009 by www.imdict.net.

WordBreakTestUnicode_*.java (under modules/analysis/common/src/test/)
is derived from Unicode data such as the Unicode Character Database.
See http://unicode.org/copyright.html for more details.

The Morfologik analyzer (morfologik) includes BSD-licensed software
developed by Dawid Weiss and Marcin Miłkowski (http://morfologik.blogspot.com/).

Morfologik uses data from Polish ispell/myspell dictionary
(http://www.sjp.pl/slownik/en/) licenced on the terms of (inter alia)
LGPL and Creative Commons ShareAlike.

Morfologic includes data from BSD-licensed dictionary of Polish (SGJP)
(http://sgjp.pl/morfeusz/)

Servlet-api.jar and javax.servlet-*.jar are under the CDDL license, the original
source code for this can be found at http://www.eclipse.org/jetty/downloads.php

===========================================================================
Kuromoji Japanese Morphological Analyzer - Apache Lucene Integration
===========================================================================

This software includes a binary and/or source version of data from

  mecab-ipadic-2.7.0-20070801

which can be obtained from

  http://atilika.com/releases/mecab-ipadic/mecab-ipadic-2.7.0-20070801.tar.gz

or

  http://jaist.dl.sourceforge.net/project/mecab/mecab-ipadic/2.7.0-20070801/mecab-ipadic-2.7.0-20070801.tar.gz

===========================================================================
mecab-ipadic-2.7.0-20070801 Notice
===========================================================================

Nara Institute of Science and Technology (NAIST),
the copyright holders, disclaims all warranties with regard to this
software, including all implied warranties of merchantability and
fitness, in no event shall NAIST be liable for
any special, indirect or consequential damages or any damages
whatsoever resulting from loss of use, data or profits, whether in an
action of contract, negligence or other tortuous action, arising out
of or in connection with the use or performance of this software.

A large portion of the dictionary entries
originate from ICOT Free Software.  The following conditions for ICOT
Free Software applies to the current dictionary as well.

Each User may also freely distribute the Program, whether in its
original form or modified, to any third party or parties, PROVIDED
that the provisions of Section 3 ("NO WARRANTY") will ALWAYS appear
on, or be attached to, the Program, which is distributed substantially
in the same form as set out herein and that such intended
distribution, if actually made, will neither violate or otherwise
contravene any of the laws and regulations of the countries having
jurisdiction over the User or the intended distribution itself.

NO WARRANTY

The program was produced on an experimental basis in the course of the
research and development conducted during the project and is provided
to users as so produced on an experimental basis.  Accordingly, the
program is provided without any warranty whatsoever, whether express,
implied, statutory or otherwise.  The term "warranty" used herein
includes, but is not limited to, any warranty of the quality,
performance, merchantability and fitness for a particular purpose of
the program and the nonexistence of any infringement or violation of
any right of any third party.

Each user of the program will agree and understand, and be deemed to
have agreed and understood, that there is no warranty whatsoever for
the program and, accordingly, the entire risk arising from or
otherwise connected with the program is assumed by the user.

Therefore, neither ICOT, the copyright holder, or any other
organization that participated in or was otherwise related to the
development of the program and their respective officials, directors,
officers and other employees shall be held liable for any and all
damages, including, without limitation, general, special, incidental
and consequential damages, arising out of or otherwise in connection
with the use or inability to use the program or any product, material
or result produced or otherwise obtained by using the program,
regardless of whether they have been advised of, or otherwise had
knowledge of, the possibility of such damages at any time during the
project or thereafter.  Each user will be deemed to have agreed to the
foregoing by his or her commencement of use of the program.  The term
"use" as used herein includes, but is not limited to, the use,
modification, copying and distribution of the program and the
production of secondary products from the program.

In the case where the program, whether in its original form or
modified, was distributed or delivered to or received by a user from
any person, organization or entity other than ICOT, unless it makes or
grants independently of ICOT any specific warranty to the user in
writing, such person, organization or entity, will also be exempted
from and not be held liable to the user for any such damages as noted
above as far as the program is concerned.

The Derby build relies on a jar file supplied by the JSON Simple
project, hosted at https://code.google.com/p/json-simple/.
The JSON simple jar file is licensed under the Apache 2.0 License.

Hive CLI
Copyright 2016 The Apache Software Foundation

Hive JDBC
Copyright 2016 The Apache Software Foundation


Chill is a set of Scala extensions for Kryo.
Copyright 2012 Twitter, Inc.

Third Party Dependencies:

Kryo 2.17
BSD 3-Clause License
http://code.google.com/p/kryo

Commons-Codec 1.7
Apache Public License 2.0
http://hadoop.apache.org



Breeze is distributed under an Apache License V2.0 (See LICENSE)

===============================================================================

Proximal algorithms outlined in Proximal.scala (package breeze.optimize.proximal)
are based on https://github.com/cvxgrp/proximal (see LICENSE for details) and distributed with
Copyright (c) 2014 by Debasish Das (Verizon), all rights reserved.

===============================================================================

QuadraticMinimizer class in package breeze.optimize.proximal is distributed with Copyright (c)
2014, Debasish Das (Verizon), all rights reserved.

===============================================================================

NonlinearMinimizer class in package breeze.optimize.proximal is distributed with Copyright (c)
2015, Debasish Das (Verizon), all rights reserved.


stream-lib
Copyright 2016 AddThis

This product includes software developed by AddThis.

This product also includes code adapted from:

Apache Solr (http://lucene.apache.org/solr/)
Copyright 2014 The Apache Software Foundation

Apache Mahout (http://mahout.apache.org/)
Copyright 2014 The Apache Software Foundation


