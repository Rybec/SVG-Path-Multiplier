# SVG Path Multiplier
---

## Why?

### The Problem

This program was written to solve the problem of multi-pass laser cuts often failing to cut all the way through or causing scorching in 3mm plywood, when making complex cuts where each pass took a significant amount of time to complete.

It turns out that when the full program is run on each pass, and each pass takes more than a few minutes, the wood has significant time to cool and possibly also to absorb significant moisture from the atmosphere.  When this happens, significant energy is consumed on each pass reheating the wood and evaporating the moisture.  This can cause the laser to fail to fully penetrate the wood regardless of the number of passes, and because the moisture leaches heat away from the cut into the adjacent wood, this can lead to excessive scorching on the edges of the cut.

### The Solution

To solve this, each cut path can be given the number of passes required before moving on to the next path.  Unless a path is extremely long and complex, this minimizes the time it has to cool and absorb moisture between passes, creating _much_ cleaner cuts that are far more likely to cut all the way through consistently.  Unfortunately, at this time, most laser cutting software does not provide this kind of multi-pass option, and manually editing the SVG file to duplicate all of the paths and group them so that they will cut in the correct order is tedious and time consuming for more complex cuts.


## What?

### This Program

This program takes an SVG file and a number as arguments, and it traverses the file duplicating all paths the specified number of times and the groups each set of duplicates to guarantee that each path will go through all of its passes before moving on to the next path.

## How?

### Usage

This is a fairly simple Python program that uses the built-in XML parsing module to look for path tags and duplicate them.  It takes two positional arguments.  The first is the name of the SVG file to be modified.  The second is an integer value indicate the number of passes desired.  For an SVG file named `circle.svg`, where four passes are desired, the command would look like this `python SVG_path_multiplier circle.svg 4`.  This is a very simple program and does no sanity checking.  Invalid arguments will cause it to crash with an error.  The output is a file named with `x-pass_` appended to the original filename, where x is the number of passes specified.  In the previous example, the file produced would be named `4-pass_circle.svg`.


## Caveats

At the time of this writing, the output of this program has not been tested on an actual laser cutter.  That said, I _have_ done this manually, by duplicating the paths in Inkscape and grouping each set of duplicate paths together, and the results on my laser cutter were absolutely amazing.  This program replicates the process I used in Inkscape.  I used LaserGRBL to convert the SVG into a Gcode program and send the instructions to my laser cutter.  I cannot guarantee the same results with other software, as I do not know how every piece of laser cutting software handles path ordering in SVGs, and LaserGRBL is what I have that works with my laser cutter.

Over the next week, I will be cutting several copies of some fairly complex projects that I have had issues with before, doing program level multi-passes.  I intended on using this application to do path level multi-passes when I do these cuts.  I'll report back and amend this with information about the results once I've done this.  I'll still be using LaserGRBL though, so this will only provide information on whether this works as expected with LaserGRBL.  If you try this with programs other than LaserGRBL, please open an issue and let me know how it went, so I can add a compatibility list to this documentation.

It should also be noted that this software may not play nicely with software that reorders the minimize travel distance and reduce total cut time.  After using this technique manually with a fairly complex set of cuts, I attempted to optimize travel with https://svg.zovu.co/, and it just hung.  This may have been due to multiplying a large number of cuts by four, overwhelming it, however it might have been due to division by zero errors, when trying to calculate the distance between duplicate paths occupying the exact same space.  With that particular optimizer, the solution is to optimize paths _before_ running this program on the file.  I haven't tested this extensively, but the order appears to be preserved this way.  (I'll see if I can check this later and update this one I have more information.)


## Disclaimer

There are no guarantees with this.  Check your stuff before starting a cut that has used this, to make sure it will function as expected.  I take no responsibility if this ruins some cutting media.

