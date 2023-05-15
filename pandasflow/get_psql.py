







def get_psqlt():
	print('''
!sudo apt-get -y -qq update
!sudo apt-get -y -qq install postgresql
!sudo service postresqg start

!sudo -u postgres psql -U postgres -c "ALTER USER posgres PASSWORD 'postgres';"

from sqlalchemy import create_engine
con = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/postgres')

def select(sql):
  return pd.read_sql(sql, con)

'''[1:])


if __name__ == "__main__":
	get_psqlt()






