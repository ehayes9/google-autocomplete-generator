from urllib.request import urlopen
import re
import pandas as pd
import numpy as np

# TODO: update query list with terms you want to search, use '+' to represent spaces

query_list = ['kale','data+science']


def get_xml(query):
	url = "http://suggestqueries.google.com/complete/search?&output=toolbar&gl=us&hl=en&q={query}%20vs%20".format(query=query)
	html_page = urlopen(url)
	file = html_page.read().decode("utf-8")
	return file

def get_suggestions(file):

	pattern = 'vs ([^"]+)'

	suggestions = re.findall(pattern,file)
	return suggestions


if __name__ == "__main__":

	array_of_df = []

	for query in query_list:
		file = get_xml(query)
		suggestions = get_suggestions(file)
		sr= pd.Series(suggestions)
		df = pd.DataFrame(sr, columns={query})
		array_of_df.append(df)

	final_df = pd.concat(array_of_df,axis=1)
	
	final_df.to_csv('data/output.csv',index=False)



	

