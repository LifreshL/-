Для закуска нужно:
1) Скачать файлы main.py и Map_Zone_Text.py
2) Установить библиотеку pygame
3) Запустить файл main.py
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
В проекте представлена реализация основных механик игры, которую я хочу создать (что-то близкое к обучающему уровню).
Основной механикой игры должен стать свет и направление этого самого света, поэтому в первую очередь здесь реализован фонарик:
Что должен уметь фонарик?
1) По внешнему виду: сектор круга с углом 120, направленный в сторону местоположения курсора, становящийся менее ярким к краю (сливается с фоном).
2) По функции: изначально у игрока нет никой (почти) информации о местности, только там где проходил свет фонарика видна карта/объекты.
3) Мелочи: не должен отображать детали комнат в которые у персонажа ещё нет доступа.

Следующая идейная часть игры - смерть. Бороться нам предстоит с существами которые не существуют/ не двигаются в области света, ну и конечно могут быть в любой точке, где этого света нет (сам ГГ конечно тоже особенный...)
Поэтому если мы уж повернёмся к такому существу спиной, то это верная смерть! Но как говорят: мыслишь - значит существуешь! Смерть переносит персонажа в безопасную зону.
Но есть кое-что пострашнее смерти - потеряться в собственных мыслях. Это приходит, когда ты обнаруживаешь свой труп, на том месте, где умер. Такое когнитивное противоречие ломает твой мир.
Что в связи с этим происходит в игре?
1) Есть ситуация, которая почти гарантированно приводит к смерти персонажа
2) Смерть переносит тебя в точку старта
3) На месте смерти появляется точка обозначающая труп.
4) Если свет от фонаря коснётся этой точки, то игра автоматически выключается.

Ну и последнее, что надо - это вывод подсказок, кнопки передвижения и паузы.
Реализовано для этого:
1) Реализация передвижения/паузы/взаимодействия
2) Описание функций клавиш для включения режима передвижения/паузы/взаимодействия
3) Вывод текста для описания происходящего и/или подсказок.

Ну и бонус, пока что бесполезная, но в дальнейшем сюжетно/концептуально интересная (эта фича не афишируется внутри игры ввиду своей бесполезности):
При удержании клавиши Q, фонарик начинает концентрировать свой свет на положении курсора пока не станет тонким красным лучём.
При этом длина луча увеличивается в 2 раза, а передвижение персонажа и изменение направления луча заблокированы.



