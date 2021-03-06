# -*- coding: utf-8 -*-
from base import APIHandler
from tornado_letv.tornado_basic_auth import require_basic_auth
from componentNode.kibana_opers import KibanaOpers


@require_basic_auth
class Kibana_Config_Handler(APIHandler):

    kibana_opers = KibanaOpers()

    def post(self):
        """
        function: start node
        url example: curl --user root:root -d "" "http://localhost:8888/elasticsearch/start"
        """
        args = self.pretty_param()
        self.kibana_opers.config(args)
        self.finish({"message": "config kibana success"})


@require_basic_auth
class Kibana_Start_Handler(APIHandler):

    kibana_opers = KibanaOpers()

    def post(self):
        """
        function: start node
        url example: curl --user root:root -d "" "http://localhost:8888/elasticsearch/start"
        """
        result = self.kibana_opers.start()
        self.finish(result)


@require_basic_auth
class Kibana_Stop_Handler(APIHandler):

    kibana_opers = KibanaOpers()

    def post(self):
        """
        function: stop node
        url example: curl --user root:root -d "" "http://localhost:8888/elasticsearch/stop"
        """
        result = self.kibana_opers.stop()
        self.finish(result)


@require_basic_auth
class Kibana_Restart_Handler(APIHandler):

    kibana_opers = KibanaOpers()

    def post(self):
        """
        function: reload node
        url example: curl --user root:root -d "" "http://localhost:8888/elasticsearch/restart"
        """
        result = self.kibana_opers.restart()
        self.finish(result)
