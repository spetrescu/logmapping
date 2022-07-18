CODE_EXTENSIONS_SPECIFIC_LANGUAGE = {
    "JAVA": "*.java",
    "Python": "*.py",
    "C++": "*.cpp"
}

FORMULAE_LOGGING_STATEMENTS_SPECIFIC_LANGUAGE = {
    "JAVA": ["LOG.info("],
}

LINE_TERMINATOR_SPECIFIC_LANGUAGE = {
    "JAVA": ";\n",
}

RUNTIME_LOG_FILE_EXTENSION = "*.log"

MAPPING_LEVELS = {
    "LEVEL_3": ["Task:", "is done.", "And is in the process of committing"],
    "LEVEL_4": ["Progress of ", " is : "],
    "LEVEL_5": ["Failed to renew lease for ", " for ", " seconds.", "Will retry shortly ..."],
    "LEVEL_6": ["JVM with ID : ", " asked for a task"],
    "LEVEL_7": ["Shuffle port returned by ContainerManager for ", " : "],
    "LEVEL_8": ["TaskAttempt Transitioned from ", " to "],
    "LEVEL_9": ["TaskAttempt: [", "] using containerId: [", " on NM: ["],
    "LEVEL_10": [" Task Transitioned from ", " timeout of ", " exceeded"],
}

MAPPING_TEMPLATE_ENTITY = {
    "LEVEL_3": "Task:<ID> is done. And is in the process of committing",
    "LEVEL_4": "Progress of TaskAttempt <ID> is : <GENERIC_VAR>",
    "LEVEL_5": "Failed to renew lease for <GENERIC_VAR> for <GENERIC_VAR> seconds.  Will retry shortly ...",
    "LEVEL_6": "JVM with ID : <ID> asked for a task",
    "LEVEL_7": "Shuffle port returned by ContainerManager for <ID> : <GENERIC_VAR>",
    "LEVEL_8": "<ID> TaskAttempt Transitioned from <GENERIC_VAR> to <GENERIC_VAR>",
    "LEVEL_9": "TaskAttempt: [<ID>] using containerId: [<ID> on NM: [<ID>]",
    "LEVEL_10": "<GENERIC_VAR> Task Transitioned from <GENERIC_VAR> to <GENERIC_VAR>"
}


MAPPING_TEMPLATE_GENERIC_VAR = {
    "LEVEL_3": "Task:<GENERIC_VAR> is done. And is in the process of committing",
    "LEVEL_4": "Progress of TaskAttempt <GENERIC_VAR> is : <GENERIC_VAR>",
    "LEVEL_5": "Failed to renew lease for <GENERIC_VAR> for <GENERIC_VAR> seconds.  Will retry shortly ...",
    "LEVEL_6": "JVM with ID : <GENERIC_VAR> asked for a task",
    "LEVEL_7": "Shuffle port returned by ContainerManager for <GENERIC_VAR> : <GENERIC_VAR>",
    "LEVEL_8": "<GENERIC_VAR> TaskAttempt Transitioned from <GENERIC_VAR> to <GENERIC_VAR>",
    "LEVEL_9": "TaskAttempt: [<GENERIC_VAR>] using containerId: [<GENERIC_VAR> on NM: [<GENERIC_VAR>]",
    "LEVEL_10": "<GENERIC_VAR> Task Transitioned from <GENERIC_VAR> to <GENERIC_VAR>"
}

MAPPING_TEMPLATE_UNDERLYING_STATEMENT = {
    "LEVEL_5": "LOG.warn(""Failed to renew lease for "" + clientsString() + "" for "" + (elapsed/1000) + "" seconds.  Will retry shortly ..."");"
}


ZOOKEEPER_MAPPING_LEVELS = {
    "LEVEL_1": ["Received connection request "],
    "LEVEL_2": ["Cannot open channel to ", " at election address "],
    "LEVEL_3": ["Accepted socket connection from "],
    "LEVEL_4": ["Closed socket connection for client ", " which had sessionid "],
    "LEVEL_5": ["Established session ", " with negotiated timeout ", " for client "],
    "LEVEL_6": ["Connection request from old client ", " will be dropped if server is in r-o mode"],
    "LEVEL_7": ["Expiring session ", " timeout of ", " exceeded"],
    "LEVEL_8": ["******* GOODBYE ", " ********"],
}
ZOOKEEPER_MAPPING_TEMPLATE_ENTITY = {
    "LEVEL_1": "Received connection request <GENERIC_VAR>",
    "LEVEL_2": "Cannot open channel to <ID> at election address <GENERIC_VAR>",
    "LEVEL_3": "Accepted socket connection from <GENERIC_VAR>",
    "LEVEL_4": "Closed socket connection for client <GENERIC_VAR> which had sessionid <ID>",
    "LEVEL_5": "Established session <ID> with negotiated timeout <GENERIC_VAR> for client <GENERIC_VAR>",
    "LEVEL_6": "Connection request from old client <GENERIC_VAR> will be dropped if server is in r-o mode",
    "LEVEL_7": "Expiring session <ID> timeout of <GENERIC_VAR> exceeded",
    "LEVEL_8": "******* GOODBYE <GENERIC_VAR> ********",
    
}
ZOOKEEPER_MAPPING_TEMPLATE_GENERIC_VAR = {
    "LEVEL_1": "Received connection request <GENERIC_VAR>",
    "LEVEL_2": "Cannot open channel to <GENERIC_VAR> at election address <GENERIC_VAR>",
    "LEVEL_3": "Accepted socket connection from <GENERIC_VAR>",
    "LEVEL_4": "Closed socket connection for client <GENERIC_VAR> which had sessionid <GENERIC_VAR>",
    "LEVEL_5": "Established session <GENERIC_VAR> with negotiated timeout <GENERIC_VAR> for client <GENERIC_VAR>",
    "LEVEL_6": "Connection request from old client <GENERIC_VAR> will be dropped if server is in r-o mode",
    "LEVEL_7": "Expiring session <GENERIC_VAR> timeout of <GENERIC_VAR> exceeded",
    "LEVEL_8": "******* GOODBYE <GENERIC_VAR> ********",
}
ZOOKEEPER_MAPPING_TEMPLATE_UNDERLYING_STATEMENT = {
    "LEVEL_1": "LOG.info(""Received connection request {}"", client.getRemoteSocketAddress());",
    "LEVEL_2": "LOG.warn(""Cannot open channel to {} at election address {}"", sid, electionAddr);",
    "LEVEL_3": "LOG.debug(""Accepted socket connection from {}"", sc.socket().getRemoteSocketAddress());",
    "LEVEL_4": "LOG.debug(""Closed socket connection for client %s which had sessionid %s"", sock.socket().getRemoteSocketAddress(), Long.toHexString(sessionId));",
    "LEVEL_5": "LOG.debug(""Established session {} with negotiated timeout {} for client {}"", Long.toHexString(cnxn.getSessionId()), cnxn.getSessionTimeout(), cnxn.getRemoteSocketAddress());",
    "LEVEL_6": "LOG.warn(""Connection request from old client {} will be dropped if server is in r-o mode"",cnxn.getRemoteSocketAddress());",
    "LEVEL_7": "LOG.info(""Expiring session {} timeout of {} exceeded"", Long.toHexString(sessionId), session.getTimeout());",
    "LEVEL_8": "LOG.warn(""******* GOODBYE {} ********"", remoteAddr);"
}
ZOOKEEPER_VARIBLE_TUPLES = {
    "LEVEL_1": ["client.getRemoteSocketAddress()", "GENERIC_VAR"],
    "LEVEL_2": ["sid, electionAddr", "ID, GENERIC_VAR"],
    "LEVEL_3": ["sc.socket().getRemoteSocketAddress()", "GENERIC_VAR"],
    "LEVEL_4": ["sock.socket().getRemoteSocketAddress(), Long.toHexString(sessionId)", "GENERIC_VAR, ID"],
    "LEVEL_5": ["Long.toHexString(cnxn.getSessionId()), cnxn.getSessionTimeout(), cnxn.getRemoteSocketAddress()", "ID, GENERIC_VAR, GENERIC_VAR"],
    "LEVEL_6": ["cnxn.getRemoteSocketAddress()", "GENERIC_VAR"],
    "LEVEL_7": ["Long.toHexString(sessionId), session.getTimeout()", "ID, GENERIC_VAR"],
    "LEVEL_8": ["remoteAddr", "GENERIC_VAR"],
}

OPENSTACK_MAPPING_LEVELS = {
    "LEVEL_1": ["Took ", " seconds to deallocate network for instance."],
    "LEVEL_2": ["Deleting instance files "],
    "LEVEL_3": ["Deletion of ", " complete"],
    "LEVEL_4": ["Took ", " seconds to spawn the instance on the hypervisor."],
}
OPENSTACK_MAPPING_TEMPLATE_ENTITY = {
    "LEVEL_1": "Took <GENERIC_VAR> seconds to deallocate network for instance.",
    "LEVEL_2": "Deleting instance files <PATH>",
    "LEVEL_3": "Deletion of <PATH> complete",
    "LEVEL_4": "Took <GENERIC_VAR> seconds to spawn the instance on the hypervisor.",
}
OPENSTACK_MAPPING_TEMPLATE_GENERIC_VAR = {
    "LEVEL_1": "Took <GENERIC_VAR> seconds to deallocate network for instance.",
    "LEVEL_2": "Deleting instance files <GENERIC_VAR>",
    "LEVEL_3": "Deletion of <GENERIC_VAR> complete",
    "LEVEL_4": "Took <GENERIC_VAR> seconds to spawn the instance on the hypervisor.",
}
OPENSTACK_MAPPING_TEMPLATE_UNDERLYING_STATEMENT = {
    "LEVEL_1": "LOG.info(""Took %0.2f seconds to deallocate network for instance."", timer.elapsed(), instance=instance)",
    "LEVEL_2": "LOG.info(""Deleting instance files %s"", target_del, instance=instance)",
    "LEVEL_3": "LOG.info(""Deletion of %s complete"", target_del, instance=instance)",
    "LEVEL_4": "LOG.info(""Took %0.2f seconds to spawn the instance on the hypervisor."", timer.elapsed(), instance=instance)",
}
OPENSTACK_VARIBLE_TUPLES = {
    "LEVEL_1": ["timer.elapsed()", "GENERIC_VAR"],
    "LEVEL_2": ["target_del", "PATH"],
    "LEVEL_3": ["target_del", "PATH"],
    "LEVEL_4": ["timer.elapsed()", "GENERIC_VAR"],
}


LINUX_MAPPING_LEVELS = {
    "LEVEL_1": ["new USB bus registered, assigned bus ", "number "],
}
LINUX_MAPPING_TEMPLATE_ENTITY = {
    "LEVEL_1": "<GENERIC_VAR> new USB bus registered, assigned bus number <GENERIC_VAR>",
}
LINUX_MAPPING_TEMPLATE_GENERIC_VAR = {
    "LEVEL_1": "<GENERIC_VAR> new USB bus registered, assigned bus number <GENERIC_VAR>",
}
LINUX_MAPPING_TEMPLATE_UNDERLYING_STATEMENT = {
    "LEVEL_1": "dev_info (bus->controller, ""new USB bus registered, assigned bus number %d\\n"", bus->busnum);"
}
LINUX_VARIBLE_TUPLES = {
    "LEVEL_1": ["bus->controller, bus->busnum", "GENERIC_VAR, GENERIC_VAR"],
}


APACHE_MAPPING_LEVELS = {
    "LEVEL_1": ["File does not exist: "],
}
APACHE_MAPPING_TEMPLATE_ENTITY = {
    "LEVEL_1": "File does not exist: <PATH>",
}
APACHE_MAPPING_TEMPLATE_GENERIC_VAR = {
    "LEVEL_1": "File does not exist: <GENERIC_VAR>",
}
APACHE_MAPPING_TEMPLATE_UNDERLYING_STATEMENT = {
    "LEVEL_1": "ap_log_rerror(""File does not exist: %s"", r->filename);",
}
APACHE_VARIBLE_TUPLES = {
    "LEVEL_1": ["r->filename", "PATH"],
}


SPARK_MAPPING_LEVELS = {
    "LEVEL_1": ["Reading broadcast variable ", " took "],
    "LEVEL_2": ["Created local directory at "],
    "LEVEL_3": ["Times: total = ", ", boot = ", ", init = ", " finish = "],
}
SPARK_MAPPING_TEMPLATE_ENTITY = {
    "LEVEL_1": "Reading broadcast variable <ID> took <GENERIC_VAR> ms",
    "LEVEL_2": "Created local directory at <PATH>",
    "LEVEL_3": "Times: total = <GENERIC_VAR> boot = <GENERIC_VAR> init = <GENERIC_VAR> finish = <GENERIC_VAR>",
}
SPARK_MAPPING_TEMPLATE_GENERIC_VAR = {
    "LEVEL_1": "Reading broadcast variable <GENERIC_VAR> took <GENERIC_VAR> ms",
    "LEVEL_2": "Created local directory at <GENERIC_VAR>",
    "LEVEL_3": "Times: total = <GENERIC_VAR> boot = <GENERIC_VAR> init = <GENERIC_VAR> finish = <GENERIC_VAR>",
}
SPARK_MAPPING_TEMPLATE_UNDERLYING_STATEMENT = {
    "LEVEL_1": "logInfo(s""Reading broadcast variable $id took ${Utils.getUsedTimeNs(startTimeNs)} ms"")",
    "LEVEL_2": "logInfo(s""Created local directory at $localDir"")",
    "LEVEL_3": "logInfo(""Times: total = %s, boot = %s, init = %s, finish = %s"".format(total, boot, init, finish))"
}
SPARK_VARIBLE_TUPLES = {
    "LEVEL_1": ["id, Utils.getUsedTimeNs(startTimeNs)", "ID, GENERIC_VAR"],
    "LEVEL_2": ["localDir", "PATH"],
    "LEVEL_3": ["total, boot, init, finish", "GENERIC_VAR, GENERIC_VAR, GENERIC_VAR, GENERIC_VAR"],
}
