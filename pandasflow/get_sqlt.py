



def get_sqlt():
	print('''
con = sqlite3.connect('/content/drive/MyDrive/Data/database')

def select(sql):
	return pd.read_sql(sql, con)

'''[1:])


if __name__ == "__main__":
	get_sqlt()