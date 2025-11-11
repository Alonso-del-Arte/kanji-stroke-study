# Kanji Stroke Study

WORK IN PROGRESS

A lot of people wonder which Chinese character has the most strokes. When I 
wondered that, and put the question to Google (and I didn't even have to type 
the whole question), I got a webpage listing a 64-stroke character pronounced 
"zh&eacute;" meaning "noisy" and using a component that also occurs in the 
character '&#x807E;', meaning "deaf." The character for "deaf" only has 22 
strokes.

It took me a lot of effort on Jim Breen's WWWJDIC to identify '&#x807E;' as 
U+807E in Unicode. As for the character for "noisy," I wonder if it's even 
present in Unicode. The page has it as an image file, not as a character that 
can be copied and pasted to a plain text file.

When the Chinese write about something that is noisy, they're probably going to 
use a character with a lot fewer strokes than the 64 of "zh&eacute;". And the 
Japanese bypass kanji altogether, with "&#x3046;&#x308B;&#x3055;&#x3044;" 
("urusai").

The page also listed a character with almost two hundred strokes, but 
acknowledged it was probably meant as a talisman rather than as actual 
communication.

So then my question is: Which Chinese character that you can actually find in a 
Chinese or Japanese newspaper has the most strokes?

I don't intend to open this project to Hacktoberfest.

## Text selections

### Public domain

* A very few haiku, just for the sake of initial testing, either by Basho or his 
contemporaries.
* The original Chinese texts which were translated to German by Hans Bethge and 
then used by Gustav Mahler for *Das Lied von der Erde*.

### Copyrighted

PLACEHOLDER

## Dependencies

* Python 3.7 or later
* Beautiful Soup
* Unihan ETL
