

news = [
	'0.10.1: Добавлена функция вызова лога изменений.',
	'0.10.0: Удалена автоматическая установка пакета catboost при установке pandasflow',
]


def get_news(i:int=1):
	
	for x in range(i):
		if x < len(news):
			print(news[x])
	
	return



if __name__ == "__main__":
	get_news(5)