import frappe

@frappe.whitelist()
def get_lat_lon(doc, method):
	# get and save latitude and langitude
	if not doc.latitude or not doc.longitute:
		from upande import get_latitude_longitude

		address = ""
		address_fields = ["address_line1", "address_line2", "city", "state", "country", "pincode"]
		for field in address_fields:
			value = doc.get(field) if doc.get(field) else None
			if not value:
				continue

			address += value + " " if field != "pincode" else ""

		address = address.replace(" ", "+").lower()
		address = address[0:-1] if address[-1] == "+" else address
		if get_latitude_longitude(address):
			doc.latitude, doc.longitute = get_latitude_longitude(address)
