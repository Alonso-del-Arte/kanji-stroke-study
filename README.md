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

It should be noted that there is a standard way to count strokes, and it doesn't 
always match what one might assume, or at least what I have assumed. For 
example, '&#x4E09;', meaning "three," quite obviously consists of three strokes. 
However, a character like '&#x53E3;', often meaning "mouth," also consists of 
three strokes, and not, as I incorrectly assumed, four strokes. As it turns out, 
to write that character correctly, the left vertical line is written as the 
first stroke, then the upper horizontal line and the right vertical line are 
written together as one stroke (the second stroke), and finally the lower 
horizontal line makes the third stroke.

The way that I intend to run this project is that first I bring in the necessary
information from Unihan, then I scrape two or three newspapers, count up which
characters occur the most frequently.

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
English texts correspond to. I'm assuming the English translations are public 
domain until someone tells me otherwise.
* The original Chinese texts of four Tang dynasty poems which Kiang Kang-hu and 
Witter Bynner translated to English and Peter Mennin used for a 1948 choral 
composition. As I doubt the translations are public domain, I have not included 
them in this folder.

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

* Python 3.7 or later &mdash; I would like to be able to use Match statements, 
so if I get to that point, I'll have to upgrade to Python 3.10.
* Beautiful Soup &mdash; Not so sure now I need this one. Characters that occur 
in both HTML metadata and the page proper should be counted accordingly, I 
think.
* Unihan ETL &mdash; I figured I would need this one to process the Unihan data, 
but it has turned out to be so confusing that I might just have to write my own 
ETL from scratch.
