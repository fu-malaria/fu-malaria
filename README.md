### FU Malaria - Open Source Computer Vision Platform for the Detection of Malaria and other Blood Borne Conditions

Last year my engineer FV and I spent a summer working on a skunk works project to train OpenCV to detect Malaria in blood cells. 


![alt text](https://github.com/fu-malaria/fu-malaria/blob/master/Pf_rings_thinC.jpg "Blood Slide")
![alt text](https://github.com/fu-malaria/fu-malaria/blob/master/Pf_rings_thinB.jpg "Blood Slide with Malaria Detection")


We had a vision of using a low cost computing device like a Raspberry Pi or Intel Joule to power a low cost portable Microscope that used computer vision to detect Malaria.

![alt text](https://github.com/fu-malaria/fu-malaria/blob/master/Malaria-retro04.jpg "Portable Low Cost Microscope")

Malaria kills 500,000-750,000 people a year, many of them young children and elderly. It often occurs in remote places that lack access to modern pathology services and so diagnosis is difficult and misdiagnosis is common.

We worked in the startup team of Intellectual Ventures Invention Development Fund and we prototyped a lot of projects but this one wasn't officially sanctioned :) and ended up getting dropped.

The good news is that the new team at http://xinova.com/ have kindly contributed this project to our company Visimagic Inc and we are making it available to the world to help reduce Malaria transmission.

## What Now

We are asking developers in communities around the world to contribute their progamming and computer vision skills to enhance this project. 

It should not need to be said but I will say it anyway, we invite anyone from any community, race, sex, sexual orientation or religion to contribute and encourage anyone who wants to try to build a business around this contribution if it helps achieve the aim of reducing Malaria. 

## FU Malaria Background

**FU Malaria** is a platform that uses OpenCV and a rule set that detects and mark most Malaria species that affect humans. It displays the image with a colored circles to indicate the blood cells and any Malaria pathogens in an image of a thin blood smear.
 
Intellectual Ventures has a long track record of helping the Gates Foundation with Malaria projects but this was outside official channels and designed to be a fast and dirty experiment to see if we could train computer vision to detect Malaria in a blood slide image.

We picked this because we wanted to validate if it was possible to put this capability into a small low cost computing package like a Raspberry PI or Intel Joule Computer Vision kit along with a Microscope so that it could go into field hospitals and clinics everywhere in the world to help cut down the transmission vector of the disease. (this is one of the biggest issues, cut the time it takes to diagnose and treat and you cut the multiplier effect of transmission).
 
After being restructured in 2016 and various life changes my previous employer Invention Development Fund (IDF) one of the investment funds of Intellectual Ventures has very kindly agreed to contribute this code to Visimagic Inc which has taken the step of open sourcing it so that developers of the world who feel strongly about this can do something about it.

Originally implemented on Windows we are moving this to Linux.

##Issues & Limitations.
This is a good proof of concept. To make it in the real world it needs to have some rough edges sanded off. 

It has the following issues Im aware of
- It will occassionally detect cell artifacts that are not Malarial.
- It needs further work on species detection, especially some of the less obvious species.
- It is currently configured to work on Thin Blood smears, normally a lab will use a think smear in order to get sufficient volume to ensure sufficient sensitivity, while it does pick up pathogens in Thick smears it is less definitive and further work from Malarial experts is needed to codify the differences between pathogens and artifacts.

 FU Malaria is the Unix adaptation of ChaoMalaria.
 
    Copyright (C) {2015-2016}  {Mike Nicholls, F Vega}

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
 
