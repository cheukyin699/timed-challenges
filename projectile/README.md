> Functionality completed in 56:05 minutes

# Projectile

This is a game, where your ball would travel a distance proportional to the
number of clicks you inputted with your mouse after the first 5 seconds.

# Struggles

One of the major hurdles that I had to get over was a silly one. I originally
had the timer counting the number of seconds that had elapsed since whatever.
Note: **seconds**. This isn't such a big deal until you realize that the
built-in Clock in `pygame` uses miliseconds. Well, I realized that, and changed
the units of my timer from seconds to miliseconds for accuracy, and whenever I
needed to use seconds, just divided by 10^3. You can guess where this is going.
I spent about 30 minutes of my time trying to figure out why the ball was
shooting off into the unknown, at break-neck speeds of 4000m/s. Yes. It took me
that long to figure out what I did wrong.

And after that, everything worked smoothly!

# Further Updates


