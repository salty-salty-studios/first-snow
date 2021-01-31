init python:

    ### Function to call the writing of the note in a new context.
    def renedit_write_the_note():
        return renpy.input("what's up?",default="",screen="renedit_input_note")

    ### Log a typo to the file.
    def renedit_add_typo():
        with open( os.path.join( renpy.config.gamedir, renedit_logdir + "EditingLog.txt" ), 'a' ) as editlog:
            editlog.write("\nTypo logged at "+ str(renpy.get_filename_line()) + ":\n" + _last_say_what + "\n\n----------------------------\n")
        store.renedit_issue_log_line = renpy.get_filename_line()
        persistent.renedit_issue_log.append((store.renedit_issue_log_line,"typo"))
        persistent.renedit_total_typo_count += 1
        renpy.notify("Successfully logged typo to file.")

    ### Add a note to the file.
    def renedit_add_note():
        note = renpy.invoke_in_new_context(renedit_write_the_note)
        if note == "CLEAR DATA": ## Let the user clear data.
            renpy.call_in_new_context("renedit_confirm_deletion")
        elif note == "VIEW TOTALS": ## Let the user view totals.
            persistent.renedit_visible_log = not persistent.renedit_visible_log
        elif note == "ALLOW MULTI":
            persistent.renedit_allow_multi = not persistent.renedit_allow_multi
        elif note == "HELP":
            renpy.show_screen("renedit_help")
        elif note != "": ## Log any actual input,
            with open( os.path.join( renpy.config.gamedir, renedit_logdir + "EditingLog.txt" ), 'a' ) as editlog:
                editlog.write( "\nNote created at " + str(renpy.get_filename_line()) +":\n"+ note + "\n\n----------------------------\n")
            renpy.notify("Successfully added note to file.")
            store.renedit_issue_log_line = renpy.get_filename_line()
            persistent.renedit_total_note_count += 1
            persistent.renedit_issue_log.append((store.renedit_issue_log_line,"note"))

        else: ## And don't log it if there's none.
            renpy.notify("Adding note cancelled.")

label renedit_confirm_deletion:

    menu:
        "Do you want to clear all editing data?"
        "Yes, delete all persistent typo/note data. (This will not effect EditingLog.txt)":
            $ persistent.renedit_issue_log = []
            $ persistent.renedit_total_typo_count = 0
            $ persistent.renedit_total_note_count = 0
            return
        "Yes, {b}and{/b} clear the Editing Log. (Deletes all content of EditingLog.txt)":
            $ persistent.renedit_issue_log = []
            $ persistent.renedit_total_typo_count = 0
            $ persistent.renedit_total_note_count = 0
            python:
                with open( os.path.join( renpy.config.gamedir, renedit_logdir + "EditingLog.txt" ), 'w' ) as editlog:
                    pass
            return
        "No!!!":
            return
