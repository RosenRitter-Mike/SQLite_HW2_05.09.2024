'''

==========================  Question 2  =======================================

'''

import sqlite3
import pprint

conn = sqlite3.connect('q1_db.db');
conn.row_factory = sqlite3.Row;
cursor = conn.cursor();

'''
1.
********    Ex. 1    *********
********  Question 6 *********

-  Which songs that won the Eurovision contest were solo performances ?

'''
print('********    Ex. 1    *********\n'
      '********  Question 6 *********\n'
      '-  Which songs that won the Eurovision contest were solo performances ?');

cursor.execute('SELECT ew.song_name FROM eurovision_winners as ew '
               'JOIN song_details as sd on ew.year = sd.year '
               'WHERE sd.solo_performance;');
result = cursor.fetchall();
list_results = [tuple(row) for row in result];

list_data = [list(tup) for tup in list_results];
pprint.pprint(list_data);
print();
'''
1.
********    Ex. 1    *********
********  Question 13 *********

-  List the Eurovision winner countries by descending number of wins ?

'''
print('********    Ex. 1    *********\n'
      '********  Question 13 *********\n'
      '-  List the Eurovision winner countries by descending number of wins ?');

cursor.execute('SELECT country FROM ('
               'SELECT country, count(*) as wins FROM eurovision_winners '
               'GROUP by country '
               'ORDER by wins DESC'
               ');');
result = cursor.fetchall();
list_results = [tuple(row) for row in result];

list_data = [list(tup) for tup in list_results];
pprint.pprint(list_data);
print();

'''
2.
-  Update the length in seconds of Netta's song from 2018, from 175 seconds to 180 seconds
'''
cursor.execute('''UPDATE song_details
set song_length_seconds = 180
where year = 2018;''');
cursor.connection.commit();

print('********    Ex. 2    *********\n********  Question 2 *********');
cursor.execute('SELECT * FROM song_details AS sd '
               'JOIN eurovision_winners AS ew ON ew.year = sd.year '
               'WHERE sd.year = 2018');
result = cursor.fetchall();
list_results = [tuple(row) for row in result];
for row in list_results:
    print(row);