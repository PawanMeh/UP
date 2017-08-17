# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe

__version__ = '0.0.1'


@frappe.whitelist(allow_guest=True)
def get_latitude_longitude(address):
	# get the latitude and longitude for the :address
	import requests

	url = "http://nominatim.openstreetmap.org/search?q={address}".format(address=address)
	url += "&format=json&addressdetails=1&limit=1&polygon_svg=1"

	response = requests.get(url)
	if response and response.json():
		result = response.json()[0] if response.json()[0] else {}
		return [result.get("lat", ""), result.get("lon", "")]
