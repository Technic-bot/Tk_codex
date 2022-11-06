# TK Codex

Hi! i see you found my small database I made for [Twokinds](https://twokinds.keenspot.com) the comic by Tom Fischbach. 
I made thid because in general it is very hard to try to look for anything specific
in the comic pages itself, this small website allows you to search per character and per textual dialogue.

This by no means try to replace the excellent [Codex Mr Amenon](https://2ks.wogcodex.com) did. Go check that out it is
very cool! Mine lacks features like negative searches and aliases. Moreover Amenons codex indexed panel content by hand
something mine does not. 

Main difference with Amenons work is this thing is up to date with the comic and has, or should have, some features to
keep it automatically in sync whenever a new page comes out. Finally it is completely open source so you can host your
own and or use it for whatever reason.

This is first an exercise for me to learn some web development, you can tell i know nothing of css, and second 
combining something of my work on  twokinds data into something usable for all. 

Again my final objective with this is for people to have some way to quickly crossreference information on the comic.
Hope you find this useful and at least half as interesting as I did making it. 


## Usage
You get  2 searches Art and Text: Art deals with characters on scene, currently only talking characters are matched, so
for example, Dahlia bodyguard is not indexed since she never speaks. May update manually over time for these cases but
  in most of the cases is not a very big limitation

To use it simply add a space separated list of every character, then system will then fetch all pages where ALL the
characters in the list appear, case insensitive. for example the query: 

```
Natani Laura Trace
```

Yields the following:

- 211, 2005-08-03, Comic for August 3, 2005
- 430, 2008-02-27, Comic for February 27, 2008
- 752, 2013-08-04, Comic for August 4, 2013
- 756, 2013-09-08, Comic for September 8, 2013
- 757, 2013-09-17, Comic for September 17, 2013

For textual search the system will fetch everything that matches the exact string you put there for example:

```
25,000
```

Returns:

- 256, 2006-04-24, Comic for April 24, 2006 

Just for clarity output is a list and the header is as it follows:

- Page number, Release Date, Comic Title (Most early comics used release date as titles)

And that is pretty much it, there are plans to add more features in the future but at least what there is here should be
functional

## Contact and further links
For further information check the project github which, should, have more detailed information and documentation as well
as how to deploy your own, plus you can hit me with PRs, bugs complainst etc!

[Techbot Codex Github Repo](https://github.com/Technic-bot/Tk_codex) 


