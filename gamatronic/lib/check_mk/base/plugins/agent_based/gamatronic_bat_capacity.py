#!/usr/bin/python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# (c) 2018 Heinlein Support GmbH
#          Robert Sander <r.sander@heinlein-support.de>

# This is free software;  you can redistribute it and/or modify it
# under the  terms of the  GNU General Public License  as published by
# the Free Software Foundation in version 2.  check_mk is  distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
# out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
# PARTICULAR PURPOSE. See the  GNU General Public License for more de-
# tails. You should have  received  a copy of the  GNU  General Public
# License along with GNU Make; see the file  COPYING.  If  not,  write
# to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
# Boston, MA 02110-1301 USA.

# factory_settings["gamatronic_bat_capacity_default"] = {
#     "battime"     : (0, 0),
#     "capacity"    : (95, 90),
# }

# def inventory_gamatronic_bat_capacity(info):
#     for line in info:
#         yield line[0], {}

# def check_gamatronic_bat_capacity(item, params, info):
#     for line in info:
#         if item == line[0]:
#             pass

# check_info["gamatronic_bat_capacity"] = {
#     "inventory_function"     : inventory_gamatronic_bat_capacity,
#     "check_function"         : check_gamatronic_bat_capacity,
#     "service_description"    : "Battery Capacity %s",
#     "has_perfdata"           : True,
#     "default_levels_variable": "gamatronic_bat_capacity_default",
#     "snmp_info"              : (".1.3.6.1.4.1.6050.1.2", [
#                                         1, # psBatteryNumber
#                                         4, # psBatteryNominalCapacity
#                                         5, # psBatteryActualCapacity
#                                ]),
#     "snmp_scan_function"     : lambda oid: oid(".1.3.6.1.2.1.1.2.0") == ".1.3.6.1.4.1.6050.5",
#     "includes"               : [ "ups_capacity.include" ],
# }
