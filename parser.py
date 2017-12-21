import csv, sys, math, operator, re, os, json
from pprint import pprint

try:
	filename = sys.argv[1]
except:
	print "\nPlease input a valid JSON filename.\n"
	print "Format: python scriptname filename.\n"
	exit()

newCsv = []
output = 'dpla.csv'
newFile = open(output, 'wb') #wb for windows, else you'll see newlines added to csv

# initialize csv writer
writer = csv.writer(newFile)

header_row = ('Id', 'IngestType', 'IngestionSequence', 'DataProvider', 
	'OriginalRecord', 'isShownAt', 'Object', 'Description', 'Format', 'Identifier', 'LanguageName', 'LanguageISO',
	'Rights', 'Title', 'Collection','Type', 'Date', 'Spatial', 'Subject')

writer.writerow(header_row)

with open(filename) as json_file:
	data = json.load(json_file)
	for s in data:
		source = s['_source']
		try:
			id = source['id']
		except:
			id = ""
		try:
			ingest_type = source['ingestType']
		except:
			ingest_type = ""
		try:
			ingestion_sequence = source['ingestionSequence']
		except:
			ingestion_sequence = ""
		try:
			data_provider = source['dataProvider']
		except:
			data_provider = ""
		try:
			original_record = source['originalRecord']
		except:
			original_record = ""
		try:
			is_shown_at = source['isShownAt']
		except:
			is_shown_at = ""
		try:
			_object = source['object']
		except:
			_object = ""

		try:
			source_resource = source['sourceResource']
		except:
			print "Warning: No source resource in record ID: " + id

		try:
			descriptions = source_resource['description']
			string = ""
			for item in descriptions:
				if len(descriptions) > 1:
					description = item.encode() + " | "
				else:
					description = item.encode()
				string = string + description
			description = string
		except:
			description = ""

		try:
			formats = source_resource['format']
			string = ""
			for item in formats:
				if len(formats) > 1:
					format = item.encode() + " | "
				else:
					format = item.encode()
				string = string + format
			format = string
		except:
			format = ""

		try:
			identifiers = source_resource['identifier']
			string = ""
			for item in identifiers:
				if len(identifiers) > 1:
					identifier = item.encode() + " | "
				else:
					identifier = item.encode()
				string = string + identifier
			identifier = string
		except:
			identifier = ""

		try:
			language = source_resource['language'][0]
			try:
				language_name = language['name']
			except:
				language_name = ""
			try:
				language_iso = language['iso639_3']
			except:
				language_iso = ""
		except:
			language_name = ""
			language_iso = ""

		try:
			rights = source_resource['rights']
		except:
			rights = ""

		try:
			titles = source_resource['title']
			string = ""
			for item in titles:
				if len(titles) > 1:
					title = item.encode() + " | "
				else:
					title = item.encode()
				string = string + title
			title = string
		except:
			title = ""

		try:
			collection = source_resource['collection']
			string = ""

			for item in collection:
				try:
					title = item['title'][0]
					id = item['id']
				except:
					title = ""
					id = ""
				string = string + "Title: " + title + ", Id: " + id
						
				if len(collection) > 1:
					string = string + " | "

			collection = string
		except:
			collection = ""

		try:
			type = source_resource['type']
		except:
			type = ""

		try:
			dates = source_resource['date']
			string = ""

			for item in dates:
				try:
					display_date = item['displayDate']
					begin = item['begin']
					end = item['end']
				except:
					display_date = ""
					begin = ""
					end = ""
				string = string + "Display Date: " + display_date + ", Begin: " + begin + ", End: " + end
						
				if len(dates) > 1:
					string = string + " | "
			date = string
		except:
			date = ""

		try:
			spatial = source_resource['spatial']
			string = ""

			for item in spatial:
				try:
					name = item['name']
				except:
					name = ""
				try:
					coordinates = item['coordinates']
				except:
					coordinates = ""
				try:
					city = item['city']
				except:
					city = ""
				try:
					county = item['county']
				except:
					county = ""
				try:
					country = item['country']
				except:
					country = ""
				try:
					region = item['region']
				except:
					region = ""
				try:
					state = item['state']
				except:
					state = ""

				string = string + "Name: " + name + ", Coordinates: " + coordinates + ", City: " + city + ", County: " + county + ", Country: " + country + ", Region: " + region + ", State: " + state
				
				if len(spatial) > 1:
					string = string + " | "

			spatial = string.encode()
		except:
			spatial = ""

		try:
			subjects = source_resource['subject']
			string = ""

			for item in subjects:
				try:
					name = item['name']
				except:
					name = ""

				string = string + "Name: " + name 
				
				if len(subjects) > 1:
					string = string + " | "

			subject = string.encode()
		except:
			subject = ""

		write_tuple = (id, ingest_type,ingestion_sequence, data_provider, original_record, 
			is_shown_at, _object, description, format, identifier, language_name, language_iso, 
			rights, title, collection, type, date, spatial, subject)
		
		writer.writerow(write_tuple)

print "File written to " + output
newFile.close()
