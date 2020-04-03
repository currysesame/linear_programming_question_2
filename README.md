# linear_programming_question_2
The question is come from: 來源：奇點無限股份有限公司-演算法工程師筆試題目

Eight people want to enjoy the party, there are requests:

|Main food	|Sub food1	|Sub food2	|The drinks|
| ----- | ------ | ------ | ------ |
|A|	(Any hamburger)	|Salad|	|	Coca Cola|
|B|	Fried chicken *2	|Smoothie|		| |
|C|	Beef burger|	French fries|	|	Black tea|
|D|	|	French fries *2|	Salad	|Coca Cola|
|E|	(Any hamburger)|	French fries|	Popcorn Chicken| |	
|F|	Chicken burger|	Smoothie *2|	|	Sprite|
|G|	(Any Main)|	French fries|	Smoothie|	(Any drink)|
|H|	Fried chicken|	(Any sub food)|	|	Sprite|

Other constrains:
Cannot waste too much food- buy 2 more(contain 2) main foods, 4 more(contain 4) sub foods or 3 more(contain 3) drinks are totally the waste.

The menu is as follow:

|Set|	price|	Main food	|Sub food	|drinks|
| ----- | ------ | ------ | ------ | ------ |
|Beef burger set	|150|	Beef burger	|French fries	|Coca Cola|
|Pork burger set	|130|	Pork burger	|Popcorn Chicken|	Sprite|
|Chicken burger set	|140|	Chicken burger	|Smoothie	|Black tea|
|Fried chicken set	|150|	fried chicken *2 |	Salad	|Green tea|
|Party set	|200	|fried chicken *4	|French fries *3、smoothie *3	|Coca Cola *4|

|Main food	|price	|Sub food	|price|	drinks|	price|
| ----- | ------ | ------ | ------ | ------ | ------ |
|Beef burger|	120|	French fries	|55|	Coca Cola|	30|
|Pork burger|	100|	Popcorn Chicken|	60|	Sprite	|30|
|Chicken burger|	110	|Smoothie|	45	|Black tea	|25|
|Fried chicken|	60	|Salad	|50	|Green tea|	25|

They need minimize the cost and satisfy these requirements. Please use the integer programming to help him solve this problem. Need to write down the function, constraints and the variables.

The following is my solution:

They can buy:
|Beef burger set*1|	Beef burger*0	|French fries*1|	Coca Cola*0|
|Pork burger set*1|	Pork burger*0	|Popcorn Chicken*0	|Sprite*1|
|Chicken burger set*1|	Chicken burger*1|	Smoothie*1|	Black tea*0|
|Fried chicken set*0|	Fried chicken*0	|Salad*2	|Green tea*0|
|Party set*1| | | |			

To satisfy the demand:
|Beef burger*1|	French fries*5	|Coca Cola*3|
|Pork burger*1|	Popcorn Chicken*1|	Sprite*2|
|Chicken burger*2|	Smoothie*5|	Black tea*1|
|Fried chicken*4	|Salad*2	|Green tea*0|

Beef burger set 1 *150 + Pork burger set 1*130 + Chicken burger set 1*140 + Party set1 * 200 + Chicken burger 1 *110 + French fries 1 *55 + Smoothie 1 * 45 + Salad 2 * 50 + Sprite 1 * 30
= 150 + 130 + 140 + 200 + 110 + 55 + 45 + 100 + 30 
= 960

The cost is 960. And the demand is satisfied with 2 more Coca Cola.

