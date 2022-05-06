from app import db
from app.models import User, Category, Items

db.drop_all()

db.create_all()

# insert rows for User table
userTest = User(id=0, first_name='Testy', last_name='Test', username='testyTest', email='testy@gmail.com', password_hash='randomHash', securityQuestion='a', question_answer_hash= 'a')

guestUser = User(id =9999, first_name="Guest", last_name = None, username="Guest1", email=None)
userTest2 = User(id=1, first_name='Taeyong', last_name='Lee', username='ty_xoxo', email='lty1995@neotech.com', password_hash='randomHash2')
userTest3 = User(id=2, first_name='Johnny', last_name='Suh', username='johnnysuhlee', email='jjsuh@neotech.com', password_hash='randomHash3')
userTest4 = User(id=3, first_name='Yuta', last_name='Nakamoto', username='tako_ya', email='naYu06@neotech.com', password_hash='randomHash4')
userTest5 = User(id=4, first_name='Mark', last_name='Lee', username='onyour__mark', email='mmarkly99@neotech.com', password_hash='randomHash5')
userTest6 = User(id=5, first_name='Sungchan', last_name='Jung', username='jschannie27', email='singsangsung_chan@neotech.com', password_hash='randomHash6')
userTest7 = User(id=6, first_name='Doyoung', last_name='Kim', username='do0_ie', email='doyo982@neotech.com', password_hash='randomHash7')
userTest8 = User(id=7, first_name='Yangyang', last_name='Liu', username='wooly_yang', email='blacksheep9023@neotech.com', password_hash='randomHash8')
userTest9 = User(id=8, first_name='Kun', last_name='Qian', username='kuncloud1010', email='cloudy1011@neotech.com', password_hash='randomHash9')
userTest10 = User(id=9, first_name='Oliver', last_name='Stuart', username='oliveStu389', email='oliver_stuart5843@info44.tech', password_hash='randomHash10')
userTest11 = User(id=10, first_name='Roger', last_name='Hunt', username='rrrogerd', email='Roger_Hunt6249@gmal.com', password_hash='randomHash11')
userTest12 = User(id=11, first_name='Gil', last_name='Brooks', username='gills17Fsh', email='Gil_Brooks5827@atink.com', password_hash='randomHash12')
userTest13 = User(id=12, first_name='Holly', last_name='Poulton', username='mistletoad12', email='Holly_poulton532@nickia.com', password_hash='randomHash13')
userTest14 = User(id=13, first_name='Alessia', last_name='Middleton', username='alleycaat0', email='alessia_Middleton1512@gmail.com', password_hash='randomHash14')

db.session.add(userTest)
db.session.add(guestUser) 
db.session.add(userTest2)
db.session.add(userTest3) 
db.session.add(userTest4)
db.session.add(userTest5) 
db.session.add(userTest6)
db.session.add(userTest7) 
db.session.add(userTest8)
db.session.add(userTest9) 
db.session.add(userTest10)
db.session.add(userTest11) 
db.session.add(userTest12)
db.session.add(userTest13) 
db.session.add(userTest14)
db.session.commit()


# inserting rows for Category table
categoryTest = Category(categoryID = 0, category_name="food")

categoryTest2 = Category(categoryID = 1, category_name="books")
categoryTest3 = Category(categoryID = 2, category_name="entertainment")
categoryTest4 = Category(categoryID = 3, category_name="home decor")
categoryTest5 = Category(categoryID = 4, category_name="women's clothing")
categoryTest6 = Category(categoryID = 5, category_name="men's clothing")
categoryTest7 = Category(categoryID = 6, category_name="electronics")
categoryTest8 = Category(categoryID = 7, category_name="kids")
categoryTest9 = Category(categoryID = 8, category_name="toys")
categoryTest10 = Category(categoryID = 9, category_name="beauty")
categoryTest11 = Category(categoryID = 10, category_name="outdoors")
categoryTest12 = Category(categoryID = 11, category_name="shoes")
categoryTest13 = Category(categoryID = 12, category_name="storage")
categoryTest14 = Category(categoryID = 13, category_name="kitchen")
categoryTest15 = Category(categoryID = 14, category_name="school & office")
categoryTest16 = Category(categoryID = 15, category_name="health")
categoryTest17 = Category(categoryID = 16, category_name="household needs")
categoryTest18 = Category(categoryID = 17, category_name="misc & others")

db.session.add(categoryTest) 
db.session.add(categoryTest2)
db.session.add(categoryTest3) 
db.session.add(categoryTest4)
db.session.add(categoryTest5) 
db.session.add(categoryTest6)
db.session.add(categoryTest7) 
db.session.add(categoryTest8)
db.session.add(categoryTest9) 
db.session.add(categoryTest10)
db.session.add(categoryTest11) 
db.session.add(categoryTest12)
db.session.add(categoryTest13) 
db.session.add(categoryTest14)
db.session.add(categoryTest15) 
db.session.add(categoryTest16)
db.session.add(categoryTest17) 
db.session.add(categoryTest18)
db.session.commit()


# inserting rows for Items table
itemsTest = Items(itemID=0, product_name='Ketchup', condition= 'New', description='Made from quality tomatoes', 
                  price=5, quantity=4, sellerID=0, categoryID=0)

itemsTest2 = Items(itemID=1, product_name='The Alchemist', condition= 'Used - Good', description='A best seller from Paulo Coelho', 
                  price=12, quantity=4, sellerID=0, categoryID=1)
itemsTest3 = Items(itemID=2, product_name='Fruits Basket DVD Collection', condition='Used - Good', description='Adapted into DVD the anime Fruits Basket', 
                  price=16, quantity=4, sellerID=0, categoryID=2)
itemsTest4 = Items(itemID=3, product_name='Study Desk', condition= 'New', description='Students tears go brrrrr', 
                  price=35, quantity=4, sellerID=0, categoryID=3)
itemsTest5 = Items(itemID=4, product_name='Maxi Dress', condition= 'New', description='Cool Dress. Near floor length', 
                  price=59, quantity=4, sellerID=0, categoryID=4)
itemsTest6 = Items(itemID=5, product_name='Suit Jacket', condition= 'New', description='It suits you nicely.', 
                  price=60, quantity=4, sellerID=0, categoryID=5)
itemsTest7 = Items(itemID=6, product_name='Nintendo Switch Lite', condition= 'Used - Like New', description='Tested. Nitendo Switch Lite handheld console', 
                  price=200, quantity=4, sellerID=0, categoryID=6)
itemsTest8 = Items(itemID=7, product_name='Baby Onesies', condition= 'New', description='Made from high quality soft cottons. For 2 year olds to 3 year olds', 
                  price=29, quantity=4, sellerID=0, categoryID=7)
itemsTest9 = Items(itemID=8, product_name='Pokemon Cards', condition= 'New', description='Pokemon Trading Cards - Starter Pack', 
                  price=6, quantity=4, sellerID=0, categoryID=8)
itemsTest10 = Items(itemID=9, product_name='Colourpop - Eyeliner', condition= 'New', description='Line those eyelids with our best eyeliner formula', 
                  price=14, quantity=4, sellerID=0, categoryID=9)
itemsTest11 = Items(itemID=10, product_name='Garden Gnome - Gnomeo', condition= 'Used - Good', description='Inspired by the animated movie, Juliet and Gnomeo', 
                  price=32, quantity=4, sellerID=0, categoryID=10)
itemsTest12 = Items(itemID=11, product_name='Uggs Boots', condition= 'Used - Acceptable', description='Warmth for your feet', 
                  price=87, quantity=4, sellerID=0, categoryID=11)
itemsTest13 = Items(itemID=12, product_name='Cabinents', condition= 'Used - Good', description='6 feet cabient tower. It has 5 drawers for your stuff', 
                  price=64, quantity=4, sellerID=0, categoryID=12)
itemsTest14 = Items(itemID=13, product_name='Hand Mixer', condition= 'New', description='Mix that batter!', 
                  price=25, quantity=4, sellerID=0, categoryID=13)
itemsTest15 = Items(itemID=14, product_name='College Ruled - Filler Paper', condition= 'New', description='To fill your binders with paper', 
                  price=2, quantity=4, sellerID=0, categoryID=14)
itemsTest16 = Items(itemID=15, product_name='Advil', condition= 'New', description='Advil for pain management and fever supression', 
                  price=35, quantity=4, sellerID=0, categoryID=15)
itemsTest17 = Items(itemID=16, product_name='Roomba', condition= 'Used - Good', description='A roomba to automatically clean your floors', 
                  price=100, quantity=4, sellerID=0, categoryID=16)
itemsTest18 = Items(itemID=17, product_name='Pride Pins', condition= 'New', description='Handmade pins to celebrate pride and our identities', 
                  price=5, quantity=4, sellerID=0, categoryID=16)

itemsTest19 = Items(itemID=18, product_name='NCT Resonance Album', condition= 'New', description='NCT 2020 K-pop album', 
                  price=30, quantity=4, sellerID=0, categoryID=2)
itemsTest20 = Items(itemID=19, product_name='Splatoon 2', condition= 'Used - Like New', description='Nintendo Switch - Splatoon game - Third person shooter action', 
                  price=60, quantity=4, sellerID=0, categoryID=2)
itemsTest21 = Items(itemID=20, product_name='Splatoon 3', condition= 'New', description='Splatlands!! Woohoo another Splatoon game.', 
                  price=60, quantity=4, sellerID=0, categoryID=2)
itemsTest22 = Items(itemID=21, product_name='Apple Sauce', condition= 'New', description='Made from quality apples', 
                  price=3, quantity=4, sellerID=4, categoryID=0)
itemsTest23 = Items(itemID=22, product_name='Salmon Filet', condition= 'New', description='A salmon cut packaged with ice', 
                  price=15, quantity=4, sellerID=8, categoryID=0)
itemsTest24 = Items(itemID=23, product_name='Roses', condition= 'New', description='Florist quality rose bouquet', 
                  price=12, quantity=4, sellerID=1, categoryID=10)
itemsTest25 = Items(itemID=24, product_name='Turning Red - DVD', condition= 'Used - Acceptable', description="Disney and Pixar's hit movie of 2022 - Turning Red", 
                  price=20, quantity=4, sellerID=8, categoryID=2)
itemsTest26 = Items(itemID=25, product_name='Shampoo', condition= 'New', description='Dove Shampoo', 
                  price=12, quantity=4, sellerID=5, categoryID=9)
itemsTest27 = Items(itemID=26, product_name='Cargo Pants', condition= 'Used - Good', description='A midlength cargo pants for men - size XL', 
                  price=20, quantity=4, sellerID=3, categoryID=5)

db.session.add(itemsTest) 
db.session.add(itemsTest2)
db.session.add(itemsTest3) 
db.session.add(itemsTest4)
db.session.add(itemsTest5) 
db.session.add(itemsTest6)
db.session.add(itemsTest7) 
db.session.add(itemsTest8)
db.session.add(itemsTest9) 
db.session.add(itemsTest10)
db.session.add(itemsTest11) 
db.session.add(itemsTest12)
db.session.add(itemsTest13) 
db.session.add(itemsTest14)
db.session.add(itemsTest15) 
db.session.add(itemsTest16)
db.session.add(itemsTest17) 
db.session.add(itemsTest18)
db.session.add(itemsTest19) 
db.session.add(itemsTest20)
db.session.add(itemsTest21) 
db.session.add(itemsTest22)
db.session.add(itemsTest23) 
db.session.add(itemsTest24)
db.session.add(itemsTest25) 
db.session.add(itemsTest26)
db.session.add(itemsTest27)
db.session.commit()


# test output from database tables
users = User.query.all()
for u in users:
	print(u.id, u.username)

u = User.query.get(0)
print(u)
print()

categories = Category.query.all()
for c in categories:
	print(c.categoryID, c.category_name)
c = Category.query.get(0)
print(c)
print()

items = Items.query.all()
for i in items:
	print(i.product_name, i.price)
i = Items.query.get(0)
print(i)
print()

