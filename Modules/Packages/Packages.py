from doctest import OutputChecker
import sound.effects.echo

sound.effects.echo.echofilter(input, OutputChecker, delay=0.7, atten=4)

from sound.effects import echo

echo.echofilter(input, OutputChecker, delay=0.7, atten=4)

from sound.effects.echo import echofilter

echofilter(input, OutputChecker, delay=0.7, atten=4)
