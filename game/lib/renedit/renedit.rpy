### Welcome to Ren'Edit, your tool for providing valuable feedback for developers.
### Installation instructions can be found in the README of Ren'Edit.


### NOTE FOR DEVELOPERS:
### Below is a list of possible ways to enable Ren'Edit in your project.

## Automatic inclusion: Add this line to your quick menu in screens.rpy.
# use renedit_overlay

## Button toggle: Add this line to your quick menu.
# textbutton "Editing Mode" action ToggleScreen("renedit_overlay")

## Persistent toggle/Options screen/Easter egg: To enable Ren'Edit out of context or hide it from normal play.
## 1: Create the variable.
# default persistent.renedit_editing_mode = False
## 2: Create a way to enable persistent.editing_mode and add it to the screen of your choice. Example: An image of a pen that enables editing mode on or off.
# imagebutton idle Transform(renedit_basedir + "pen.png",alpha=0.5) hover (renedit_basedir + "pen.png") action SetField(persistent, "renedit_editing_mode", True)
## 3: Change the renedit_overlay to include the following line at the very top, and shift the rest of the contents under this condition.
# if persistent.renedit_editing_mode:


### NOTE FOR EDITORS:
### If the Ren'Py project you're working on does not use Ren'Edit, you can enable it yourself.
### Follow the installation instructions as normal in the ReadMe, but uncomment the following lines (15-17).

# init python:
#     config.underlay.append(renpy.Keymap(renedit_mode = Show("renedit_overlay")))
#     config.keymap["renedit_mode"] = ['e']

### Then, simply press "e" in-game to enable the overlay.






### Code continues here. (DO NOT TOUCH... unless you know what you're doing.)
### Screen Variables
define renedit_green = "#182719EB"
define renedit_blue = "#181F27EB"
default renedit_color = renedit_green

define renedit_tl_add_note = _("Add\nNote")
define renedit_tl_log_typo = _("Log\nTypo")

### Images
define renedit_basedir = "lib/renedit/"
define renedit_logdir = "./"

image renedit addnotebase = renedit_basedir + "addnotebase.png"
image renedit logtypobase = renedit_basedir + "logtypo.png"
image renedit logtypohover = Fixed(renedit_basedir + "logtypohover.png",Transform(Text(renedit_tl_log_typo,text_align=0.5,color="#fff",size=36,bold=True),xpos=.15))
image renedit addnotehover = Fixed(renedit_basedir + "addnotehover.png",Transform(Text(renedit_tl_add_note,text_align=0.5,color="#fff",size=36,bold=True),xpos=.15))

### Used internally
default persistent.renedit_issue_log = []
default persistent.renedit_allow_multi = False
default persistent.renedit_visible_log = False
default persistent.renedit_total_typo_count = 0
default persistent.renedit_total_note_count = 0
