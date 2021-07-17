---
title: Основные настройки задачи
---

Задача - это то, что хранит в себе ваши намерения о каком-то конкретном торговом инстументе. 
Она включает в себя следующие пункты:
- статус о работе. Включена ли задача или нет. Если нет, то бот не будет отслеживать ордера и подключаться к бирже 
для этого конкретного инструмента
- профиль. Профиль содержит название биржи, API ключи для подключения к вашему аккаунту и некоторые другие вещи
- символ инструмента. Например, BTCUSDT
- стратегия торговли и ее настройки. Без нее, как и без самой задачи, торговать невозможно. 
В настройках стратегии указаны десятки параметров. О них позже.
- кошелек. Для Квика - это код клиента, а для Binance - это может быть спотовый кошелек, маржинальный, фьючерсный 
или кошелек для остальных фьючерсов. Если торговля происходит на демо субпрофиле, то кошелек всегда `Демо`
- тип разрешенных ордеров. Эта опция только для бота. Можете разрешить лишь покупки, лишь продажи, или и то, 
и другое. Или вообще все запретить и тогда он сам будет лишь реагировать на ваши ордера. 
Подробнее смотрите описание конкретных стратегий
- минимальный объем ордера. Используется ботом для отправки ордеров с выбранным объемом, а также учитывается при 
создании ордера в мобильном приложении. Указывается в Bitcoin'ах для криптобирж или в рублях для Квика, 
а конвертируется в любую валюту, которой вы торгуете. Либо же вы можете выбрать другую валюту, например, 
доллары или валюты из инструмента, для которого эта задача
- заметки. Просто место для ваших мыслей, которые могут пригодиться в будущем.

Итак, что мы имеем. Файл задач, который называется `tasks.json`. Он содержит все задачи, которые вам интересны для 
торговли. Через приложение легко изменить его содержимое. Тогда сервер будет знать, что на таком-то инструменте 
надо использовать такую-то стратегию, торговать на такой-то бирже и на выбранную сумму для одного ордера.

Пойдемте-ка дальше.

