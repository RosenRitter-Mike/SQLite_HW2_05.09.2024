'''

==========================  Question 1  =======================================

1.
SELECT count(*) FROM eurovision_winners
WHERE country = "Israel";
______________________________
Answer: 4

2.
SELECT count(*) FROM eurovision_winners
WHERE country = host_country;
_______________________________
Answer: 6

3.
SELECT year FROM eurovision_winners
WHERE country = "Israel";

4.
SELECT song_length_seconds FROM song_details
WHERE song_length_seconds = (
	SELECT MIN(song_length_seconds)
	FROM song_details
	);

5.
SELECT * FROM eurovision_winners as ew
JOIN song_details as sd on ew.year = sd.year;

6.
SELECT ew.song_name FROM eurovision_winners as ew
JOIN song_details as sd on ew.year = sd.year
WHERE sd.solo_performance;

7.
SELECT count(*) FROM song_details
WHERE language = "English";

8.
SELECT avg(song_length_seconds) FROM song_details;

9.
SELECT year FROM eurovision_winners
WHERE song_name = "Hallelujah";

10.
SELECT min(year) FROM song_details
where solo_performance = False;

11.
SELECT ew.song_name, sd.song_length_seconds FROM eurovision_winners as ew
JOIN song_details as sd on ew.year = sd.year
WHERE sd.song_length_seconds = (SELECT max(song_length_seconds) FROM song_details);

12.
SELECT country FROM (
SELECT country, count(*) as times FROM eurovision_winners
GROUP by country
ORDER by times DESC
LIMIT 1);

13.
SELECT country FROM (
SELECT country, count(*) as wins FROM eurovision_winners
GROUP by country
ORDER by wins DESC
);

14.
SELECT ew.song_name FROM eurovision_winners as ew
JOIN song_details as sd on ew.year = sd.year
WHERE sd.language = "French";

15.
SELECT min(year), max(year) FROM eurovision_winners
WHERE country = "Israel";

16.
SELECT ew.song_name, ew.country, sd.year, sd.song_length_seconds FROM eurovision_winners as ew
JOIN song_details as sd on ew.year = sd.year
ORDER by sd.song_length_seconds DESC;

17.
SELECT ew.country FROM eurovision_winners as ew
JOIN song_details as sd on ew.year = sd.year
WHERE sd.song_length_seconds > (SELECT avg(song_length_seconds) FROM song_details);

18.
SELECT song_name FROM (SELECT ew.song_name, min(sd.song_length_seconds) FROM eurovision_winners as ew
JOIN song_details as sd on ew.year = sd.year
WHERE sd.solo_performance);

19.
SELECT ew.country, avg(sd.song_length_seconds) as times FROM eurovision_winners as ew
JOIN song_details as sd on ew.year = sd.year
GROUP by ew.country

20.
SELECT count(*) FROM song_details
WHERE language != "English";

21.
SELECT count(DISTINCT genre) FROM song_details;

22.
SELECT winner FROM eurovision_winners
WHERE country = "Israel"
ORDER by year DESC
LIMIT 1;

'''

