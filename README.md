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

I'm putting these in the in/ folder of this repository.

### Public domain

These are in the in/public-domain/ folder.

* A very few haiku, just for the sake of initial testing, either by Basho or his 
contemporaries. English translations are provided.
* The original Chinese texts which were translated to German by Hans Bethge and 
then used by Gustav Mahler for *Das Lied von der Erde*. Although Mahler made 
changes to Bethge's text, those changes are not reflected in either the original 
Chinese texts or the provided German translations. I'm not sure which texts the 
English texts correspond to.

### Copyrighted

These are in the in/copyrighted/ folder.

#### With advance permission

These are going to be texts that I have obtained permission to use and include 
in this repository. I also plan to include a few haiku I've written myself, 
though I make no promises that they're going to be any good or that they're 
going to serve any purpose other than provide some context for the use of 
high-stroke count characters.

#### Without advance permission

These are going to be texts that I have not gotten permission to use and include 
in this repository. They're excluded by the Git Ignore.

I figure that if only scrape the Chinese and Japanese newspapers one level from 
their websites' front pages, no one should have any objection, just as long as I 
don't upload that content here on GitHub.

## Dependencies

* Python 3.7 or later
* Beautiful Soup
* Unihan ETL
