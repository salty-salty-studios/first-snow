# script.rpy
# Contains the script flow.

# A new game has been started, pass control to script performer.
label script_start:
    # First Snow route.
    perform "1S1"
    perform "1S2"
    perform "1S3"
    perform "1S4"
    perform "1S5"
    perform "1S6"
    perform "1S7"
    perform "2S1"
    perform "2S2"
    perform "2S3"
    perform "2S4"
    perform "2S5"
    perform "2S6"
    perform "2S7"
    perform "2S8"
    perform "2S9"
    perform "3S1"
    perform "3S2"
    perform "3S3"
    perform "3S4"
    perform "3S5"
    perform "3S6"
    perform "3S7"
    perform "3S8"

    # Credits.
    perform "4S1"
    # VA scene
    perform "4S2"
    return
