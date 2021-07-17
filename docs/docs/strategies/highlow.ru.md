---
title: Хайлоу
---

Эта стратегия работает по принципу "купи ниже всех, продай выше всех". Как только бот понимает, 
что рынок валится в пропасть, обновляя минимумы за определенный период (лои), 
он ждет разворота на дне и совершает покупку. Это работает и в обратную сторону - как только рынок 
обновляет максимумы (хаи), ждет разворота и продает (шортит). Одновременно с вхождением в рынок 
выставляются стопы и тейки (ордера, которые закроют позицию с прибылью).

Для того, чтобы бот принял решение о входе в рынок, ему нужно дождаться соблюдения настроек, 
которые вы укажите. Из-за различий тех или иных торговых инструментов лучше создавать один набор 
параметров под один инструмент.

Стратегия основана на идее, что когда подавляющее большинство людей на лоях стремятся продать по рынку, 
то разворот рынка уже близок. И в какой-то момент расклад сил изменится - станет больше покупателей 
по рынку и цена отскочет. Поэтому нужно подобрать такие настройки, при которых гарантированно получим 
разворот.

Итого, что делает бот:
- ждет, когда процент сделок по тренду будет подходящим
- ждет обновления экстремумов
- определяет разворот и заходит
- ставит стоп, потом тейк
- ждет
- если исполнился стоп, то снимает тейк и дальше либо перезаходит, либо снова ждет обновления 
экстремумов
- если цена отходит на расстояние `дальность до перестановки в безубыток`, то переставляет ордер
- если исполняется стоп, то снимает тейк и дальше либо перезаходит, либо снова ждет обновления экстремумов
- если исполнился тейк, то снимает стоп и все начинается снова.

Вот, что можно настроить:
- количество сделок для анализа. Пример: выбрали 300. То есть каждую секунду (в зависимости от 
настроек `профиля`, опция `задержка между запросами на биржу`) будет анализироваться 300 последних 
сделок и рассчитываться, сколько же из них было по тренду, а сколько - против тренда
- процент сделок по тренду. Пример: 98.4%. Значит, когда из 300 сделок 296+ будет по тренду 
(продажи на падении цены, покупки на росте цены), то бот будет ждать обновления минимумов или максимумов
- количество свечей для анализа. Определяет, сколько брать свечей графика для высчитывания минимума и 
максимума цен
- таймфрейм свеч. Сколько в одной свече - 1 минута, 5 минут, час, день. Чем больше таймфрейм, 
тем реже будут сделки
- подождать разворота. Сколько секунд бот будет ждать разворота перед тем, как быть готовым зайти в рынок. 
Пример: выставили 4 секунды, цена падает, количество сделок по тренду подходящее количество, 
обновляется минимум, бот начинает раскладывать все сделки по "свечам" длительностью одна секунда. 
Берет 4 секундной свечи * количество процентов перехая/перелоя. Определяет, начал ли рынок разворот 
за эти несколько секунд или нет. Если начал, то входит в сделку. Обратите внимание, что 
количество секундных свеч = значение опции * процент удаления цены от хая/лоя. 
Пример: цена вышла за минимум на 2.5% по сравнению с предыдущим минимумом. 
4 секунды (ваш выбор) * 2.5% = 10 секундных свечей. Такой подход помогает поймать самые 
выгодные цены даже при сильнейших движениях XBTUSD на 5% за минуту. Ведь чем сильнее движение, 
тем дольше цена будет на экстремумах и тем сложнее определить разворот
- входить в позицию лимиткой. На некоторых биржах комиссию заплатят вам, а не вы, при входе 
лимиткой. Цена может не вернуться к вашей одиноко стоящей лимитке (в идеале, правильный вход гарантирует, 
что цена не вернется). Но если вдруг цена вернется, то вы сэкономите на коммиссии и получите более 
выгодную цену входа. При определенных настройках такой подход может быть предпочтительнее, чем вход по 
рынку
- отодвинуть цену входа ниже/выше на процент. Если выбран вход лимиткой, значение этой опции 
отодвигает цену входа от той цены, на которой бот определил начало разворота. Пример: на цене 100 
бот определил, что рынок разворачивается и можно заходить. Отсчитвает этот процент от цены bid/ask 
(при покупке/продаже), ставит лимитный ордер, ставит стопы и тейки
- перезаходить после стопа еще n раз. Когда бот зашел в позицию, рынок может немножко откатить, 
а потом захотеть вынести стопы новоприбывших, а только потом действительно сильно откатить. 
Такое явление часто происходит, поэтому вы можете решить, что боту нужно перезайти после стопа повторно. 
Но не просто тупо в этот же момент залететь в рынок, а снова подождать разворота. Пример: цена 100, 
бот зашел по 101, цена погуляла в районе 101.5-101.7, но не дошла до вашего тейка. Потом пошла вниз, 
исполнила ваш стоп на 100.8, продолжила падение до 100.1, не обновив минимум, бот выждал разворот и 
снова зашел в сделку. Так будет повторяться до тех пор, пока количество разрешенных подряд стопов 
будет позволять (ведь иначе бот возьмет перерыв), либо пока количество перезаходов будет позволять. 
Очень НЕ рекомендую разрешать перезаходить много раз.