screen renedit_input_note(prompt):
    style_prefix "input"
    add Solid("#181F27EB") # Set an overlay for readability.
    vbox:
        ypos 0.35 xalign 0.5 xsize 950
        add "renedit addnotebase" xalign 0.5 # Icon for decoration
        label _("{color=#90a6ad}Write your note below.\n") xalign 0.5 text_outlines [(absolute(2),renedit_blue,0,0)] # Prompt
        input id "input" color "#90a6ad" outlines [(absolute(2),renedit_blue,0,0)] caret Transform(renedit_basedir + "pen.png",xzoom=-1,ypos=-0.2) # Input styling
    text "TIP: Type \"HELP\" to view Ren'Edit commands." size 28 color "#90a6ad" outlines [(absolute(2),renedit_blue,0,0)] xalign 0.5 text_align 0.5 ypos .9 # Tips and other functionality.
screen renedit_help():
    modal True
    add Solid("#181F27EB")
    key 'K_ESCAPE' action Hide("renedit_help")
    vbox:
        xalign 0.5 ypos 0.35
        add "renedit addnotebase" xalign 0.5
        text "All Ren'Edit commands. Please note these are all CASE-SENSITIVE.Close with ESCAPE.\n" color "#90a6ad" outlines [(absolute(2),renedit_blue,0,0)]
        vbox:
            xalign 0.5 xmaximum 950
            hbox:

                label _("CLEAR DATA") xsize 350
                text _("Delete persistent issue log data.") color "#90a6ad" outlines [(absolute(2),renedit_blue,0,0)]
            add Solid(renedit_blue,ysize=5,xsize=1000,xalign=0.5)
            hbox:

                label _("VIEW TOTALS") xsize 350
                text _("Toggle visibility of total edit counts. Currently set to [persistent.renedit_visible_log].") color "#90a6ad" outlines [(absolute(2),renedit_blue,0,0)]
            add Solid(renedit_blue,ysize=5,xsize=1000,xalign=0.5)
            hbox:

                label _("ALLOW MULTI") xsize 350
                text _("Toggle ability to log multiple typos times per line. Currently set to [persistent.renedit_allow_multi].") color "#90a6ad" outlines [(absolute(2),renedit_blue,0,0)]
            add Solid(renedit_blue,ysize=5,xsize=1000,xalign=0.5)

        text "\nCreated by minute and Caps." text_align 1.0 xalign 1.0 color "#90a6ad" outlines [(absolute(2),renedit_blue,0,0)]
### THE OVERLAY
## I really don't recommend changing this unless you know what you're doing! But here you are anyway.
screen renedit_overlay():
    hbox:
        vbox:
            fixed: ### We set the add note button as a fixed so we can display the note count correctly.
                xsize 120 ## The width of the addnote button.
                ysize 115 ## The height of the addnote button.

                imagebutton: ### ADD_NOTE BUTTON
                    idle "renedit addnotebase" hover "renedit addnotebase" hover_foreground "renedit addnotehover" # Imagebutton appearance
                    action Function(renedit_add_note) # What it does
                    tooltip _("Add a note on the current line.") # A tooltip!
                    hovered SetVariable("renedit_color",renedit_blue) # Set the tooltip background color to match the icon.

                ## Checks if this line already has a note, and if so, displays how many so far.
                if (renpy.get_filename_line(),"note") in persistent.renedit_issue_log:
                    $ note_count = persistent.renedit_issue_log.count((renpy.get_filename_line(),"note"))
                    frame:
                        background None
                        yalign 0.95 xalign 1.0
                        text "x" + str(note_count) bold True color "#90a6ad" outlines [(absolute(2),renedit_blue,0,0)]
            ### ADD_TYPO BUTTON
            ## First, we check if a typo exists. No need to mark a typo or grammar error multiple times, so we'll set it to insensitive if it exists already. Unless of course, allow multi is toggled...
            if (renpy.get_filename_line(),"typo") in persistent.renedit_issue_log and not persistent.renedit_allow_multi:
                imagebutton:
                    idle "renedit logtypobase" hover "renedit logtypobase" # Imagebutton appearance
                    tooltip _("Typo logged at current line.") # A tooltip!
                    action NullAction() # Do nothing!
                    hovered SetVariable("renedit_color",renedit_green) # Set the tooltip background color to match the icon.
                    at transform: # Set the button at a low transparency.
                        alpha 0.5
            ## If it DOESN'T EXIST, we show the button.
            else:
                fixed:
                    xsize 120 ## The width of the addtypo button.
                    ysize 115 ## The height of the addtypo button.
                    imagebutton:
                        idle "renedit logtypobase" hover "renedit logtypobase" hover_foreground "renedit logtypohover" # Imagebutton appearance
                        action Function(renedit_add_typo) # What it does
                        tooltip _("Log a typo on the current line.") # A tooltip!
                        hovered SetVariable("renedit_color",renedit_green) # Set the tooltip background color to match the icon.
                    if persistent.renedit_allow_multi:
                        if (renpy.get_filename_line(),"typo") in persistent.renedit_issue_log:
                            $ typo_count = persistent.renedit_issue_log.count((renpy.get_filename_line(),"typo"))
                            frame:
                                background None
                                yalign 0.95 xalign 1.0
                                text "x" + str(typo_count) bold True color "#8faa8f" outlines [(absolute(2),renedit_green,0,0)]

        $ tooltip = GetTooltip() # Make sure the tooltip shows up.
        if tooltip: # If we're hovering over an object with a tooltip...
            frame: # Set a frame,
                if renedit_color == renedit_green: # Choose the color,
                    background Frame(renedit_green)
                    ypos 0.5 # Move it where it needs to be
                else:
                    background Frame(renedit_blue)
                text "[tooltip]" color "#fff" italic True # And display it!

    ### If the user wants to to see their totals, we display it here.
    if persistent.renedit_visible_log:
        vbox:
            xalign 1.0
            frame:
                xalign 1.0 xsize 350
                text str(persistent.renedit_total_note_count) + " notes created." xalign 1.0 text_align 1.0
                background Frame(renedit_blue)
            frame:
                xalign 1.0 xsize 350
                text str(persistent.renedit_total_typo_count) + " typos found." xalign 1.0 text_align 1.0
                background Frame(renedit_green)
