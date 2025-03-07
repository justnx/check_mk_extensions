#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

#
# (c) 2020 Heinlein Support GmbH
#          Robert Sander <r.sander@heinlein-support.de>
#

# This is free software;  you can redistribute it and/or modify it
# under the  terms of the  GNU General Public License  as published by
# the Free Software Foundation in version 2.  This file is distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
# out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
# PARTICULAR PURPOSE. See the  GNU General Public License for more de-
# ails.  You should have  received  a copy of the  GNU  General Public
# License along with GNU Make; see the file  COPYING.  If  not,  write
# to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
# Boston, MA 02110-1301 USA.

from cmk.gui.i18n import _

from cmk.gui.plugins.metrics import (
    check_metrics,
    metric_info,
    graph_info,
)

metric_info["rusage_user"] = {
    "title" : _("User CPU time used"),
    "unit"  : "",
    "color" : "31/a",
}

metric_info["rusage_system"] = {
    "title" : _("System CPU time used"),
    "unit"  : "",
    "color" : "41/a",
}

graph_info['memcached_cpu_usage'] ={
    "title"   : _("CPU usage"),
    "metrics" : [
        ( "rusage_user", "area" ),
        ( "rusage_system", "stack" ),
    ],
}


metric_info["auth_cmds"] = {
    "title" : _("Authorizations"),
    "unit"  : "1/s",
    "color" : "31/a",
}

metric_info["auth_errors"] = {
    "title" : _("Authorization Errors"),
    "unit"  : "1/s",
    "color" : "13/a",
}

graph_info['memcached_authorizations'] = {
    "title"   : _("Authorizations"),
    "metrics" : [
        ( "auth_cmds", "area" ),
        ( "auth_errors", "line" ),
    ],
}


metric_info["bytes_read"] = {
    "title" : _("Read"),
    "unit"  : "bytes/s",
    "color" : "31/a"
}

metric_info["bytes_written"] = {
    "title" : _("Written"),
    "unit"  : "bytes/s",
    "color" : "41/a"
}

graph_info['memcached_rw'] = {
    "title"   : _("Read and written"),
    "metrics" : [
        ( "bytes_read", "area" ),
        ( "bytes_written", "-area" ),
    ],
}


metric_info["get_hits"] = {
    "title" : _("GET Hits"),
    "unit"  : "1/s",
    "color" : "31/a"
}

metric_info["get_misses"] = {
    "title" : _("GET Misses"),
    "unit"  : "1/s",
    "color" : "13/a"
}

metric_info["cmd_get"] = {
    "title" : _("GET Commands"),
    "unit"  : "1/s",
    "color" : "23/a"
}

graph_info['memcached_get'] = {
    "title"   : _("GET"),
    "metrics" : [
        ( "get_hits", "area" ),
        ( "get_misses", "stack" ),
        ( "cmd_get", "line" ),
    ],
}

metric_info["cmd_set"] = {
    "title" : _("SET Commands"),
    "unit"  : "1/s",
    "color" : "33/a"
}

metric_info["cmd_flush"] = {
    "title" : _("Flush Commands"),
    "unit"  : "1/s",
    "color" : "43/a"
}


graph_info['memcached_commands'] = {
    "title"   : _("Commands"),
    "metrics" : [
        ( "cmd_get", "area" ),
        ( "cmd_set", "stack" ),
        ( "cmd_flush", "stack" ),
    ],
}


metric_info["cas_hits"] = {
    "title" : _("CAS hits"),
    "unit"  : "1/s",
    "color" : "32/a"
}

metric_info["cas_misses"] = {
    "title" : _("CAS misses"),
    "unit"  : "1/s",
    "color" : "22/a"
}

metric_info["cas_badval"] = {
    "title" : _("CAS bad identifier"),
    "unit"  : "1/s",
    "color" : "12/a"
}

graph_info['memcached_cas'] = {
    "title"   : _("CAS"),
    "metrics" : [
        ( "cas_hits", "area" ),
        ( "cas_misses", "stack" ),
        ( "cas_badval", "line" ),
    ],
}


metric_info["incr_hits"] = {
    "title" : _("Increase Hits"),
    "unit"  : "1/s",
    "color" : "42/a"
}

metric_info["incr_misses"] = {
    "title" : _("Increase misses"),
    "unit"  : "1/s",
    "color" : "12/a"
}

metric_info["decr_hits"] = {
    "title" : _("Decrease Hits"),
    "unit"  : "1/s",
    "color" : "45/a"
}

metric_info["decr_misses"] = {
    "title" : _("Decrease misses"),
    "unit"  : "1/s",
    "color" : "15/a"
}

graph_info['memcached_incdec'] = {
    "title"   : _("Increase/Decrease"),
    "metrics" : [
        ( "incr_hits", "area" ),
        ( "incr_misses", "stack" ),
        ( "decr_hits", "-area" ),
        ( "decr_misses", "-stack" ),
    ],
}

metric_info["delete_hits"] = {
    "title" : _("Delete Hits"),
    "unit"  : "1/s",
    "color" : "43/a"
}

metric_info["delete_misses"] = {
    "title" : _("Delete misses"),
    "unit"  : "1/s",
    "color" : "13/a"
}

graph_info['memcached_deletions'] = {
    "title"   : _("Deletions"),
    "metrics" : [
        ( "delete_hits", "area" ),
        ( "delete_misses", "stack" ),
    ],
}


metric_info["total_connections"] = {
    "title" : _("Connections"),
    "unit"  : "1/s",
    "color" : "33/a",
}

metric_info["conn_yields"] = {
    "title" : _("Forced connection yields"),
    "unit"  : "1/s",
    "color" : "14/a",
}

metric_info["curr_connections"] = {
    "title" : _("Current Connections"),
    "unit"  : "",
    "color" : "24/a",
}

metric_info["connection_structures"] = {
    "title" : _("Connection Structures"),
    "unit"  : "",
    "color" : "44/a",
}

metric_info["listen_disabled_num"] = {
    "title" : _("Listen disabled"),
    "unit"  : "1/s",
    "color" : "15/a",
}

metric_info["total_items"] = {
    "title" : _("Items stored"),
    "unit"  : "1/s",
    "color" : "33/a",
}

metric_info["curr_items"] = {
    "title" : _("Items in cache"),
    "unit"  : "",
    "color" : "41/a"
}

metric_info["reclaimed"] = {
    "title" : _("Items reclaimed"),
    "unit"  : "1/s",
    "color" : "22/a",
}

metric_info["cache_hit_rate"] = {
    "title" : _("Rate of cache hits"),
    "unit"  : "%",
    "color" : "46/a",
}

metric_info["threads"] = {
    "title" : _("Threads"),
    "unit"  : "",
    "color" : "31/a",
}

metric_info["bytes_percent"] = {
    "title" : _("Cache Usage"),
    "unit"  : "%",
    "color" : "31/a"
}

metric_info["evictions"] = {
    "title" : _("Evictions"),
    "unit"  : "1/s",
    "color" : "21/a"
}

#graph_info.append({
#    "title"   : _("Items"),
#    "metrics" : [
#        ( "total_items", "area" ),
#        ( "curr_items", "line" ),
#    ],
#})


