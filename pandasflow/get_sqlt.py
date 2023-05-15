



def get_sqlt():
	print('''
con = sqlite3.connect('/content/drive/MyDrive/Data/_database_')

def select(sql):
	return pd.read_sql(sql, con)

'''[1:])


if __name__ == "__main__":
	get_sqlt()