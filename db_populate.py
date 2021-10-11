import sqlite3

db_locale='students.db'

connie= sqlite3.connect(db_locale)
c= connie.cursor()

c.execute("""
INSERT into contact_details(firstname,surname,street_address,suburb) VALUES
('BHUVAN','ESWAR','TVK','CHENNAI'),
('BHAVESH','NARA','NHERU','ADAYAR'),
('SAMANVITHA','SREE','GHANDHI','ERODE'),
('BHARANI','KAPPOR','KKP','CHENNAI')
""")

connie.commit()
connie.close()