# gutspacebot

Алгоритм запуска бота:

py venv -m .venv                  #создаем виртуальное окружение в папке с проектом

.venv/Skripts/activate            #активируем виртуальное окружение

pip install -r requirements.txt   #устанаваливаем необходимые библиотеки

$env:TOKEN=""                     #в кавычки вставляем токен от паблика

python bot.py                     #запускаем бота
