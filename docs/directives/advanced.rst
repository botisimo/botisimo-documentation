Advanced Example
================

This example shows you how to combine the ``$(pick)`` and ``$(repeat)`` :doc:`response variables </variables/index>` with the ``$[cost]`` and ``$[give]`` :doc:`response directives</directives/index>` to make a !gamble command.

Example
    This command will cost the user ``100`` currency to run and will give them a 5:16 chance to break even, a 5:16 chance to lose it, a 5:16 chance to get a return, and a 1:16 chance to hit the jackpot::

        $[cost 100] $(pick $(repeat 5 $[give 100] You broke even +0 | )$(repeat 5 You lost it all -100 | )$(repeat 5 $[give 150] You got a return on your investment +50 | )$[give 300] You hit the jackpot! +200)

    ``!gamble`` -> ``You got a return on your investment +50``
