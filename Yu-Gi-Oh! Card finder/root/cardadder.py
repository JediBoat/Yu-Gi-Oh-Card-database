import mysql.connector
from mysql.connector import Error




connection = mysql.connector.connect(host='sql8.freesqldatabase.com',
                                     user='sql8681610',
                                    password='bjTUhQneyh',
                                    database="sql8681610"
                                    )#Connect to the database

mycursor = connection.cursor()


Yugiohcards = [("3-Hump Lacooda", "Beast / Effect", "NO98" ,"N"), #list of data for card table
               ("A-to-Z-Dragon Buster Cannon", "Machine / Fusion / Effect", "NO98" ,"N"),
               ("7 Colored Fish", "Fish / Normal", "NO98" ,"N"),
               ("A D Changer", "Warrior / Effect", "NO98" ,"N"),
               ("Abominable Unchained Soul", "Fiend / Effect", "NO98" ,"N"),
               ("Absorouter Dragon", "Dragon / Effect", "YESROK" ,"N"),
               ("Abyss Actor - Comic Relief", "Fiend / Pendulum / Effect", "YESABY55" ,"N"),
               ("Invader of Darkness", "Fiend / Effect", "NO98" ,"N"), #list of data for card table
               ("Chaos Emperor Dragon - Envoy of the End", "Dragon / Effect", "NO98" ,"N"),
               ("Mazera DeVille", "Fiend / Effect", "NO98" ,"N"),
               ("The End of Anubis", "Fiend / Effect", "NO98" ,"N"),
               ("4-Starred Ladybug of Doom", "Insect / Flip / Effect", "NO98" ,"N"),
               ("Blue-Eyes White Dragon", "Dragon / Normal", "YESBE97" ,"N"),
               ("Archnemeses Protos", "Wyrm / Effect", "NO98" ,"F"),
               ("Dark Magician", "Spellcaster / Normal", "NO98" ,"N"),
               ("Ancient Gear Golem", "Machine / Effect", "YESOG8" ,"N"),		
               ("Megaton Ancient Gear Golem", "Machine / Fusion / Effect", "YESOG8" ,"N"),
               ("Ancient Gear Golem - Ultimate Pound", "Machine / Effect", "YESOG8" ,"N"),
               ("Stardust Synchron", "Machine / Tuner / Effect", "YESST5" ,"N"),
               ("Stardust Trail", "Dragon / Effect", "YESST5" ,"N"),
               ("Stardust Xiaolong", "Dragon / Effect", "YESST5" ,"N"),
               ("Stardust Charge Warrior", "Warrior / Synchro / Effect", "YESST5" ,"N"),
               ("Shooting Majestic Star Dragon", "Dragon / Synchro / Effect", "YESST5" ,"N"),
               ("Majestic Dragon", "Dragon / Tuner / Effect", "YESST5" ,"N"),
               ("Blue-Eyes Alternative White Dragon", "Dragon / Effect", "YESBE97" ,"N"),
               ("Neo Blue-Eyes Ultimate Dragon", "Dragon / Fusion / Effect", "YESBE97" ,"N"),
               ("Deep-Eyes White Dragon", "Dragon / Effect", "YESBE97" ,"N"),
               ("Abyss Dweller", "Sea Serpent / Xyz / Effect", "NO98" ,"N"),
               ("Borrelend Dragon", "Dragon / Link / Effect", "NO98" ,"N"),
               ("Blackwing - Gofu the Vague Shadow", "Winged Beast / Tuner / Effect", "YESBW89" ,"F"),
               ("Block Dragon", "Rock / Effect", "NO98" ,"F"),
               ("Orcust Harp Horror", "Machine / Effect", "NO98" ,"F"),
               ("Number 42: Galaxy Tomahawk", "Machine / Xyz / Effect", "NO98" ,"N"),
               ("Astrograph Sorcerer", "Spellcaster / Pendulum / Effect", "YESSOC9" ,"L1"),
               ("Destiny HERO - Malicious", "Warrior / Effect", "YESZ67" ,"N")]

Yghcardsdetails = [(3, "Earth", 500, 1500, "If there are 3 face-up 3-Hump Lacooda cards on your side of the field, Tribute 2 of them to draw 3 cards."), #list of data for card details table
                   (10, "Light", 4000, 4000, "(ABC-Dragon Buster + XYZ-Dragon Cannon)   Must be Special Summoned (from your Extra Deck) by banishing cards you control with the above original names, and cannot be Special Summoned by other ways. (You do not use Polymerization.) During either player's turn, when your opponent activates a Spell/Trap Card, or monster effect: You can discard 1 card; negate the activation, and if you do, destroy that card. During either player's turn: You can banish this card, then target 1 each of your banished ABC-Dragon Buster, and XYZ-Dragon Cannon; Special Summon them."),
                   (4, "Water", 1800, 800, "A rare rainbow fish that has never been caught by mortal man."),
                   (1, "Light", 100, 100, "You can banish this card from your Graveyard, then target 1 monster on the field; change its battle position."),
                   (8, "Dark", 3000, 1500, "You can only Special Summon Abominable Unchained Soul(s) once per turn. If a card(s) you control is destroyed by battle or card effect: You can Special Summon this card from your hand. If this card is Special Summoned: You can discard 1 card; destroy 1 card on the field. Once per turn, during the End Phase, if this card is in the GY because it was destroyed on the field and sent there this turn: You can Special Summon this card, but place it on the bottom of the Deck when it leaves the field."),
                   (7, "Dark", 1200, 2800, "If you control a Rokket monster, you can Special Summon this card (from your hand). You can only Special Summon Absorouter Dragon once per turn this way. If this card is sent to the GY: You can add 1 Rokket monster from your Deck to your hand. You can only use this effect of Absorouter Dragon once per turn."),
                   (3, "Dark", 1000, 2000, "Pendulum Scale: 8      Pendulum Effect:You can target 1 Abyss Actor Pendulum Monster you control and 1 monster your opponent controls; switch control of both monsters, then destroy this card. You can only use this effect of Abyss Actor - Comic Relief once per turn.     Card Text:You take no battle damage from attacks involving this card. Once per turn, during your Standby Phase: Give control of this card to your opponent. Once per turn, if control of this face-up card changes: Activate this effect; the owner of this card can destroy 1 Set Abyss Script Spell in their Spell & Trap Zone."),
                   (7, "Dark", 2900, 2500, "Your opponent cannot activate Quick-Play Spell Cards."), #list of data for card details table
                   (8, "Dark", 3000, 2500, "Cannot be Normal Summoned/Set. Must be Special Summoned (from your hand) by banishing 1 LIGHT and 1 DARK monster from your GY. Once per turn: You can pay 1000 LP; send as many cards in both players' hands and on the field as possible to the GY, then inflict 300 damage to your opponent for each card sent to the opponent's GY by this effect. You cannot activate other cards or effects during the turn you activate this card's effect."),
                   (8, "Dark", 2800, 2300, "This card cannot be Normal Summoned or Set. This card cannot be Special Summoned except by Tributing 1 face-up Warrior of Zera on your side of the field while Pandemonium is on the field. If Pandemonium is on your side of the field when you Special Summon this card, your opponent discards 3 random cards from their hand. If Pandemonium  is not on your side of the field, this effect is not applied."),
                   (6, "Dark", 2500, 0, "While this card is face-up on the field, all effects of Spell, Trap, and Monster Cards that target a card(s) in the Graveyard or that activate in the Graveyard are negated."),
                   (3, "Wind", 800, 0, "FLIP: Destroy all Level 4 monsters your opponent controls."),
                   (8, "Light", 3000, 2500, "This legendary dragon is a powerful engine of destruction. Virtually invincible, very few have faced this awesome creature and lived to tell the tale."),
                   (11, "Dark", 2500, 3000, "Cannot be Normal Summoned/Set. Must first be Special Summoned (from your hand) by banishing 3 monsters with different Attributes from your GY and/or face-up field. Cannot be destroyed by card effects. You can declare 1 monster Attribute on the field; destroy all monsters on the field with that Attribute, also until the end of the next turn, neither player can Special Summon monsters with that Attribute. You can only use this effect of Archnemeses Protos once per turn."),
                   (7, "Dark", 2500, 2100, "The ultimate wizard in terms of attack and defense."),
                   (8, "Earth", 3000, 3000, "Cannot be Special Summoned. If this card attacks, your opponent cannot activate any Spell/Trap Cards until the end of the Damage Step. If this card attacks a Defense Position monster, inflict piercing battle damage."),
                   (9, "Earth", 3300, 3300, "3 Ancient Gear monsters. If this card attacks, your opponent cannot activate Spell/Trap Cards until the end of the Damage Step. If this card was Fusion Summoned using 2 or more Ancient Gear Golem and/or Ancient Gear Golem - Ultimate Pound as material, it can attack up to that many times during each Battle Phase. If this face-up Fusion Summoned card in its owner's control leaves the field because of an opponent's card effect: You can Special Summon 1 Ultimate Ancient Gear Golem from your Extra Deck, ignoring its Summoning conditions."),
                   (8, "Earth", 3000, 3000, "Cannot be Special Summoned. If this card attacks a Defense Position monster, inflict piercing battle damage. Up to twice per turn, when this attacking card destroys a monster by battle: You can discard 1 Machine monster; this card can attack again in a row. If this card on the field is destroyed by battle or card effect: You can add 1 Polymerization from your Deck to your hand, and if you do, add 1 other Ancient Gear monster from your GY to your hand."),
                   (4, "Light", 1500, 1000, "If this card is in your hand or GY: You can Tribute 1 monster; Special Summon this card, but banish it when it leaves the field, also, you cannot Special Summon monsters from the Extra Deck for the rest of this turn, except Synchro Monsters. If this card is Normal or Special Summoned: You can add 1 Spell/Trap from your Deck to your hand that mentions Stardust Dragon. You can only use each effect of Stardust Synchron once per turn."),
                   (4, "Light", 500, 2000, "If a monster you control is Tributed (except during the Damage Step): You can Special Summon this card from your hand or GY, but banish it when it leaves the field. If a Warrior, Synchron, or Stardust Synchro Monster is Synchro Summoned using this card as material: You can Special Summon 1 Stardust Token (Dragon/LIGHT/Level 1/ATK 0/DEF 0). You can only use each effect of Stardust Trail once per turn."),
                   (1, "Light", 100, 100, "When you Synchro Summon Stardust Dragon: You can Special Summon this card from your GY in Attack Position. Each turn, the first time this card would be destroyed by battle, it is not destroyed."),
                   (6, "Wind", 2000, 1300, "1 Tuner + 1+ non-Tuner monsters. When this card is Synchro Summoned: You can draw 1 card. You can only use this effect of Stardust Charge Warrior once per turn. This card can attack all Special Summoned monsters your opponent controls, once each."),
                   (11, "Wind", 4000, 3300, "Majestic Dragon + 1+ non-Tuner monsters, including a Dragon Synchro Monster. Must first be Synchro Summoned. Once per turn: You can negate the effects of 1 Effect Monster your opponent controls. This card gains 1 additional attack each Battle Phase for every monster in your GY that is Stardust Dragon or is a Synchro Monster with Stardust Dragon in its text. Once per turn, when your opponent activates a card or effect (Quick Effect): You can banish this card (until the End Phase), and if you do, negate the activation, and if you do that, banish that card."),
                   (0, "Light", 0, 0, "Cannot be used as Synchro Material, except for the Synchro Summon of a Majestic monster."),
                   (8, "Light", 3000, 2500, "Cannot be Normal Summoned/Set. Must first be Special Summoned (from your hand) by revealing Blue-Eyes White Dragon in your hand. You can only Special Summon Blue-Eyes Alternative White Dragon once per turn this way. This card's name becomes Blue-Eyes White Dragon while on the field or in the GY. Once per turn: You can target 1 monster your opponent controls; destroy it. This card cannot attack the turn this effect is activated."),
                   (12, "Light", 4500, 3800, "Blue-Eyes White Dragon + Blue-Eyes White Dragon + Blue-Eyes White Dragon. At the end of the Damage Step, if this is the only face-up card you control, and this Fusion Summoned card attacked: You can send 1 Blue-Eyes Fusion Monster from your Extra Deck to the Graveyard; this card can attack again in a row. You can use this effect of Neo Blue-Eyes Ultimate Dragon up to twice per turn. During either player's turn, when a card or effect is activated that targets a Blue-Eyes monster(s) you control: You can banish this card from your Graveyard; negate the activation, and if you do, destroy that card."),
                   (10, "Light", 0, 0, "When a face-up Blue-Eyes monster(s) you control is destroyed by battle or an opponent's card effect, and you have a Dragon-Type monster in your Graveyard: You can Special Summon this card from your hand, and if you do, inflict 600 damage to your opponent for each Dragon-Type monster with different names in your Graveyard. If this card is Normal or Special Summoned: Target 1 Dragon-Type monster in your Graveyard; this card's ATK becomes equal to that monster's. If this card on the field is destroyed by a card effect: Destroy all monsters your opponent controls."),
                   (7, "Dark", 2500, 2100, "The ultimate wizard in terms of attack and defense."),
                   (4, "Water", 1700, 1400, "While this card has a material attached that was originally WATER, all WATER monsters you control gain 500 ATK. Once per turn (Quick Effect): You can detach 1 material from this card; your opponent cannot activate any card effects in their GY this turn."),
                   (5, "Dark", 3500, 0, "3+ Effect Monsters. Cannot be destroyed by battle or card effects, also neither player can target this card with monster effects. This card can attack all monsters your opponent controls, once each. (Quick Effect): You can target 1 Effect Monster on the field and 1 Rokket monster in your GY; negate the effects of that monster on the field, and if you do, Special Summon that other monster from your GY. Your opponent cannot activate cards or effects in response to this effect's activation. You can only use this effect of Borrelend Dragon once per turn."),
                   (8, "Earth", 2500, 3000, "Cannot be Normal Summoned/Set. Must be Special Summoned (from your hand or GY) by banishing 3 EARTH monsters from your hand and/or GY. Rock monsters you control cannot be destroyed, except by battle. If this card is sent from the field to the GY: You can add up to 3 Rock monsters from your Deck to your hand, whose total Levels equal 8. You can only use this effect of Block Dragon once per turn."),
                   (4, "Dark", 1700, 1400, "You can banish this card from your GY; Special Summon 1 Orcust monster from your Deck, except Orcust Harp Horror, also you cannot Special Summon monsters for the rest of this turn, except DARK monsters. You can only use this effect of Orcust Harp Horror once per turn."),
                   (7, "Wind", 0, 3000, "Once per turn: You can detach 2 Xyz Materials from this card; Special Summon as many Battle Eagle Tokens (Machine-Type/WIND/Level 6/ATK 2000/DEF 0) as possible, destroy them during the End Phase of this turn, also your opponent takes no further battle damage this turn."),
                   (7, "Dark", 2500, 2000, "Pendulum Scale 1, Pendulum Effect:During your Main Phase: You can destroy this card, and if you do, take 1 Stargazer Magician from your hand or Deck, and either place it in your Pendulum Zone or Special Summon it. You can only use this effect of Astrograph Sorcerer once per turn. Card Text:If a card(s) you control is destroyed by battle or card effect: You can Special Summon this card from your hand, then you can choose 1 monster in the GY, Extra Deck, or that is banished, and that was destroyed this turn, and add 1 monster with the same name from your Deck to your hand. You can banish this card you control, plus 4 monsters from your hand, field, and/or GY (1 each with Pendulum Dragon, Xyz Dragon, Synchro Dragon, and Fusion Dragon in their names); Special Summon 1 Supreme King Z-ARC from your Extra Deck. (This is treated as a Fusion Summon.)"),
                   (6, "Dark", 800, 800, "You can banish this card from your GY; Special Summon 1 Destiny HERO - Malicious from your Deck.")]

Yugiohspelltraps = [("1st Movement Solo", "SPELL", "YESM4" ,"N"), #list of data for card table
               ("A Wingbeat of Giant Dragon", "SPELL", "NO98" ,"N"),
               ("Polymerization", "SPELL", "YESPOL54" ,"N"),
               ("Xyz Revenge", "SPELL", "NO98" ,"N"),
               ("Zombie World", "SPELL", "YESZOO" ,"N"),
               ("A Hero Emerges", "TRAP", "YESZ67" ,"N"),
               ("Blackbird Close", "TRAP", "YESBW89" ,"N"),
               ("Monster Reborn", "SPELL", "NO98" ,"L1"),
               ("Reinforcement of the Army", "SPELL", "NO98" ,"L1"),
               ("Sky Striker Mobilize - Engage!", "SPELL", "YESPOL54" ,"L1"),
               ("Pot of Desires", "SPELL", "NO98" ,"L2"),
               ("Mystic Mine", "SPELL", "NO98" ,"F"),
               ("1st Movement Solo", "SPELL", "YESM4" ,"N"), #list of data for card table
               ("A Wingbeat of Giant Dragon", "SPELL", "NO98" ,"N"),
               ("Polymerization", "SPELL", "YESPOL54" ,"N"),
               ("Xyz Revenge", "SPELL", "NO98" ,"N"),
               ("Zombie World", "SPELL", "YESZOO" ,"N"),
               ("A Hero Emerges", "TRAP", "YESZ67" ,"N"),
               ("Blackbird Close", "TRAP", "YESBW89" ,"N"),
               ("Monster Reborn", "SPELL", "NO98" ,"L1"),
               ("Reinforcement of the Army", "SPELL", "NO98" ,"L1"),
               ("Sky Striker Mobilize - Engage!", "SPELL", "YESPOL54" ,"L1"),
               ("Pot of Desires", "SPELL", "NO98" ,"L2"),
               ("Mystic Mine", "SPELL", "NO98" ,"F"),
               ("Alien Brain", "TRAP", "NO98" ,"N")]

Yghcardsspelltrapdetails = [("Normal Spell", "If you control no monsters: Special Summon 1 Level 4 or lower Melodious monster from your hand or Deck. You can only activate 1 1st Movement Solo per turn. You cannot Special Summon monsters during the turn you activate this card, except Melodious monsters."), #list of data for spell trap table
                   ("Normal Spell", "Return 1 Level 5 or higher Dragon-Type monster you control to the hand, and if you do, destroy all Spell and Trap Cards on the field."),
                   ("Normal Spell", "Fusion Summon 1 Fusion Monster from your Extra Deck, using monsters from your hand or field as Fusion Material."),
                   ("Normal Spell", "If your opponent controls a face-up Xyz Monster that has Xyz Material: Target 1 Xyz monster in your Graveyard; Special Summon it, then detach 1 Xyz Material from a monster your opponent controls and attach it to that monster as an Xyz Material. You can only activate 1 Xyz Revenge per turn."),
                   ("Field Spell", "All monsters on the field and in the GYs become Zombie monsters. Neither player can Tribute Summon monsters, except Zombie monsters."),
                   ("Normal trap", "When an opponent's monster declares an attack: Your opponent chooses 1 random card from your hand, then if it is a monster that can be Special Summoned, Special Summon it. Otherwise, send it to the GY."),
                   ("Counter Trap", "When a monster your opponent controls activates its effect: You can send 1 face-up Blackwing monster you control to the GY; negate the activation, and if you do, destroy it, then, you can Special Summon 1 Black-Winged Dragon from your Extra Deck. If you control a Blackwing Synchro Monster or Black-Winged Dragon, you can activate this card from your hand."),
                   ("Normal Spell", "Target 1 monster in either GY; Special Summon it."), 
                   ("Normal Spell", "Add 1 Level 4 or lower Warrior monster from your Deck to your hand."),
                   ("Normal Spell", "If you control no monsters in your Main Monster Zone: Add 1 Sky Striker card from your Deck to your hand, except Sky Striker Mobilize - Engage!, then, if you have 3 or more Spells in your GY, you can draw 1 card."),
                   ("Field Spell", "If your opponent controls more monsters than you do, your opponent cannot activate monster effects or declare an attack. If you control more monsters than your opponent does, you cannot activate monster effects or declare an attack. Once per turn, during the End Phase, if both players control the same number of monsters: Destroy this card."),
                   ("Normal Spell", "Add 1 Level 4 or lower Warrior monster from your Deck to your hand."),
                   ("Normal Spell", "If you control no monsters: Special Summon 1 Level 4 or lower Melodious monster from your hand or Deck. You can only activate 1 1st Movement Solo per turn. You cannot Special Summon monsters during the turn you activate this card, except Melodious monsters."), #list of data for spell trap table
                   ("Normal Spell", "Return 1 Level 5 or higher Dragon-Type monster you control to the hand, and if you do, destroy all Spell and Trap Cards on the field."),
                   ("Normal Spell", "Fusion Summon 1 Fusion Monster from your Extra Deck, using monsters from your hand or field as Fusion Material."),
                   ("Normal Spell", "If your opponent controls a face-up Xyz Monster that has Xyz Material: Target 1 Xyz monster in your Graveyard; Special Summon it, then detach 1 Xyz Material from a monster your opponent controls and attach it to that monster as an Xyz Material. You can only activate 1 Xyz Revenge per turn."),
                   ("Field Spell", "All monsters on the field and in the GYs become Zombie monsters. Neither player can Tribute Summon monsters, except Zombie monsters."),
                   ("Normal trap", "When an opponent's monster declares an attack: Your opponent chooses 1 random card from your hand, then if it is a monster that can be Special Summoned, Special Summon it. Otherwise, send it to the GY."),
                   ("Counter Trap", "When a monster your opponent controls activates its effect: You can send 1 face-up Blackwing monster you control to the GY; negate the activation, and if you do, destroy it, then, you can Special Summon 1 Black-Winged Dragon from your Extra Deck. If you control a Blackwing Synchro Monster or Black-Winged Dragon, you can activate this card from your hand."),
                   ("Normal Spell", "Target 1 monster in either GY; Special Summon it."), 
                   ("Normal Spell", "Add 1 Level 4 or lower Warrior monster from your Deck to your hand."),
                   ("Normal Spell", "If you control no monsters in your Main Monster Zone: Add 1 Sky Striker card from your Deck to your hand, except Sky Striker Mobilize - Engage!, then, if you have 3 or more Spells in your GY, you can draw 1 card."),
                   ("Normal Spell", "Banish 10 cards from the top of your Deck, face-down; draw 2 cards. You can only activate 1 Pot of Desires per turn."), 
                   ("Normal Spell", "If your opponent controls more monsters than you do, your opponent cannot activate monster effects or declare an attack. If you control more monsters than your opponent does, you cannot activate monster effects or declare an attack. Once per turn, during the End Phase, if both players control the same number of monsters: Destroy this card."), 
                   ("Normal Spell", "If a Reptile monster you control is destroyed by battle with an opponent's attacking monster and sent to the GY: Take control of the opponent's monster, and if you do, it becomes a Reptile.")]






Q1 = "CREATE TABLE Cards (cardID int PRIMARY KEY AUTO_INCREMENT, cardname VARCHAR(100), cardtype VARCHAR(50), relatedid VARCHAR(50), forbiddenlistid VARCHAR(50))"#Creates the Card table

Q2 = """CREATE TABLE Cardsdetails (carddetailsID int PRIMARY KEY, FOREIGN KEY(carddetailsID) REFERENCES Cards(cardID), 
                    cardlevel int, 
                    cardattributte VARCHAR(50), 
                    cardattack int, 
                    carddefence int, 
                    flavourtext VARCHAR(7000))""" #Creates the Card details table

Q11 = """CREATE TABLE Spelltrap (SpelltrapID int PRIMARY KEY, FOREIGN KEY(SpelltrapID) REFERENCES Cards(cardID), 
                    speedspell VARCHAR(50), 
                    stflavourtext VARCHAR(7000))""" #Creates the Card details table



Q3 = "INSERT INTO Cards (Cardname, Cardtype, relatedid, forbiddenlistid) VALUES (%s, %s, %s, %s)"#Query for inserting vaules into Cardname and Cardtype columns

Q4 = "INSERT INTO Cardsdetails(carddetailsID, cardlevel, cardattributte, cardattack, carddefence, flavourtext) VALUES (%s, %s, %s, %s, %s, %s)"#Query for inserting vaules into columns of card detail table

Q12 = "INSERT INTO Spelltrap (SpelltrapID, speedspell, stflavourtext) VALUES (%s,%s, %s)"#Query for inserting vaules into columns of spelltrap table
Q20 = "CREATE DATABASE carddatabase"


Q24 = "DROP TABLE Cardsdetails"
Q25 = "DROP TABLE Spelltrap"
Q26 = "DROP TABLE Cards"

# Q15 = "SELECT * FROM Cards "#test if all the cards have been added
# mycursor.execute(Q15)

# for x in mycursor:
#     print (x)


mycursor.execute(Q1)
mycursor.execute(Q2)
mycursor.execute(Q11)

connection.commit()


for x, Yugiohcard in enumerate(Yugiohcards):
    mycursor.execute(Q3, Yugiohcard)#Adds data to my tables
    last_id = mycursor.lastrowid
    mycursor.execute(Q4, (last_id,) + Yghcardsdetails[x]) #loops through array of data and inserts them into columns from in both table linked correctly by primary and foregin key.
connection.commit()

#For spell cards
for x, Yugiohspelltrap in enumerate(Yugiohspelltraps):
    mycursor.execute(Q3, Yugiohspelltrap)#Adds data to my tables
    last_id = mycursor.lastrowid
    mycursor.execute(Q12, (last_id,) + Yghcardsspelltrapdetails[x]) #loops through array of data and inserts them into columns from in both table linked correctly by primary and foregin key.

connection.commit()



# Q13 = "SELECT* FROM Cards FULL JOIN Cardsdetails ON cardID = carddetailsID WHERE cardname = 'The End of Anubis' "#Search cards table for the card name and coloumns linked to it in the card details table
# mycursor.execute(Q13)#excutesthe queries

# for x in mycursor:
#     print (x)

# Q76 =  "SELECT* FROM Cards FULL JOIN Spelltrap ON cardID = SpelltrapID WHERE cardname = 'Zombie World'"
# mycursor.execute(Q76)#excutesthe queries
# for x in mycursor:
#     print (x)

