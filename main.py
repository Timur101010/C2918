import ccxt

# Создание объекта биржи
exchange = ccxt.binance({
    'apiKey': 'ваш_api_key',
    'secret': 'ваш_api_secret',
})

# Параметры торговой стратегии
symbol = 'BTC/USDT'  # Торгуемая пара
amount = 0.01  # Объем торговой сделки
buy_price = 10000  # Цена покупки
sell_price = 11000  # Цена продажи

# Функция для выполнения покупки
def execute_buy_order():
    print('Выполняется покупка...')
    order = exchange.create_order(symbol, 'limit', 'buy', amount, buy_price)
    print('Покупка выполнена:', order)

# Функция для выполнения продажи
def execute_sell_order():
    print('Выполняется продажа...')
    order = exchange.create_order(symbol, 'limit', 'sell', amount, sell_price)
    print('Продажа выполнена:', order)

# Основной цикл бота
while True:
    ticker = exchange.fetch_ticker(symbol)

    # Проверка условия для покупки
    if ticker['close'] > buy_price:
        execute_buy_order()

    # Проверка условия для продажи
    if ticker['close'] < sell_price:
        execute_sell_order()
