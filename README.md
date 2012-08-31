# WWOP

**WWOP** - is a simple worldweatheronline.com parser, designed for use with conky system monitor.

Distributed under GNU GPL v3 or any higher version you may want.

## Installation

Get fresh source:

    $ git clone git://github.com/pztrn/wwop
    
And use wwop.py with conky!

## Configuration

Config file: ~/.config/wwop/config. Config example:

    [main]
    API_KEY=YOUR_API_KEY
    CITY=Moscow,Russia
    
    [forecast]
    LANGUAGE=ru
    DAYS=4
    TEMP_TYPE=C

## Usage

First, you will need current data:

    $ wwop.py --download
    
Data will be stored in 'cache', located in script's config dir (defaults to ~/.config/wwop). After that you can pass options to script, like:

    $ conkygw.py opt {day} modificator
    
All available opt's:

 * **-c** - Current condition
 * **-d** - Condition by day

All available modificators:

 * **mintemp** - Minimal temperature
 * **maxtemp** - Maximum temperature
 * **cond** - Condition
 * **dof** - Day of week
 
Maximum 'day' specified in config , starts from 1.

'day' option must be specified with '-d' option and must not be specified with '-c' option!

## Example

    TEXT
    ${execi 1800 /data/Projects/github/wwop/wwop.py --download}${color aad6ff}ATM: ${color ffd1ba}${execi 1800 /data/Projects/github/wwop/wwop.py -c temp} ${alignr}$color ${execi 1800 /data/Projects/github/wwop/wwop.py -c cond}
    
    ${color ffb966}${execi 1800 /data/Projects/github/wwop/wwop.py -d 1 dof}: ${color 82ffab}${execi 1800 /data/Projects/github/wwop/wwop.py -d 1 maxtemp}$color..${color b3ecff}${execi 1800 /data/Projects/github/wwop/wwop.py -d 1 mintemp} 
    ${alignr}$color(${execi 1800 /data/Projects/github/wwop/wwop.py -d 1 cond})
    
    ${color ffb966}${execi 1800 /data/Projects/github/wwop/wwop.py -d 2 dof}: ${color 82ffab}${execi 1800 /data/Projects/github/wwop/wwop.py -d 2 maxtemp}$color..${color b3ecff}${execi 1800 /data/Projects/github/wwop/wwop.py -d 2 mintemp} 
    ${alignr}$color(${execi 1800 /data/Projects/github/wwop/wwop.py -d 2 cond})
    
    ${color ffb966}${execi 1800 /data/Projects/github/wwop/wwop.py -d 3 dof}: ${color 82ffab}${execi 1800 /data/Projects/github/wwop/wwop.py -d 3 maxtemp}$color..${color b3ecff}${execi 1800 /data/Projects/github/wwop/wwop.py -d 3 mintemp} 
    ${alignr}$color(${execi 1800 /data/Projects/github/wwop/wwop.py -d 3 cond})
    
    ${color ffb966}${execi 1800 /data/Projects/github/wwop/wwop.py -d 4 dof}: ${color 82ffab}${execi 1800 /data/Projects/github/wwop/wwop.py -d 4 maxtemp}$color..${color b3ecff}${execi 1800 /data/Projects/github/wwop/wwop.py -d 4 mintemp} 
    ${alignr}$color(${execi 1800 /data/Projects/github/wwop/wwop.py -d 4 cond})    
