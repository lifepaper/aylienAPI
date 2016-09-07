import requests



CRED = {
	'id': "dd9a452f",
    'key': "0b9a122ce54003cad9e8f2ff37c10ea4",
}

def get_endpoint(type_='summarize'):
	options =[
		'summarize',
		'classify',
	]
	if type_ in options:
		endpoint = 'https://api.aylien.com/api/v1/'+type_
	else:
		print 'wrong type'
		return
	return endpoint

def aylienAPI(type_, content):
	endpoint = get_endpoint(type_)
	if type(content) != dict:
		return
	header={
	'X-AYLIEN-TextAPI-Application-ID':CRED['id'],
	'X-AYLIEN-TextAPI-Application-Key':CRED['key'],
	}

	response = requests.get(endpoint, headers=header, params=content)
	return response

if __name__ == '__main__':
	type_ = 'summarize'
	content = {
	'url': 'https://www.theguardian.com/science/2016/sep/06/new-drug-wakes-up-immune-system-to-fight-one-of-deadliest-cancers',
	'title': None,
	'text': None,
	'sentences_number':2
	}
	response = aylienAPI(type_,content)
	print response.text
