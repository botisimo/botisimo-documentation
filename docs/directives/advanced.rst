Advanced Example
================

This example shows you how to combine the ``$(pick)`` and ``$(repeat)`` :doc:`response variables </variables/index>` with the ``$[cost]`` and ``$[give]`` :doc:`response directives</directives/index>` to make a !gamble command.

Example Command:
    **name**: !gamble

    **response**: $[cost 100] $(pick $(repeat 5 $[give 100] You broke even +0 | )$(repeat 5 You lost it all -100 | )$(repeat 5 $[give 150] You got a return on your investment +50 | )$[give 300] You hit the jackpot! +200)

    **output**::

        user:     !gamble
        botisimo: You got a return on your investment +50
        user:     !gamble
        botisimo: You lost it all -100
