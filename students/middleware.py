#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import connection
from django.conf import settings


class SetQueriesTime(object):
    def process_response(self, request, response):
        """
        add executed queries time and count for html pages
        and exclude images urls
        """
        if settings.MEDIA_URL not in request.path \
                and "text/html" in response['Content-Type']:
            total_time = 0
            queries_count = len(connection.queries)

            for query in connection.queries:
                query_time = query.get('time')
                total_time += float(query_time)

            queries_html_string = '<div class="panel-footer">' \
                                      '<div class="queries">' \
                                          'Runned queries count is {0}' \
                                          '</br>' \
                                          'Total queries time is {1}' \
                                      '</div>' \
                                  '</div>' \
                                  '</body>'.format(queries_count,
                                                   "{:.3f}".format(total_time))

            response.content = response.content.replace("</body>",
                                                        queries_html_string)
        return response
