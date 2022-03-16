# Twofold: First Snow

![HACKERWOMAN](https://github.com/salty-salty-studios/first-snow/blob/main/sourcecode.png?raw=true)

## Overview

This is the source code for First Snow. It is released in the hope people can learn from it, make translations, and modify it to their needs and wishes (with the license conditions in mind).

## Requirements

* A relatively modern PC (anything made in the former half of the 10's will do fine), running either:
  - Windows XP+ (but please do upgrade to a more modern Windows)
  - OS X 10.7+
  - Linux with glibc or glibc-compatible libc and X11
* Ren'Py 7.4.11
* Some creativity (optional!)

## Working with the script

First Snow uses a semi-custom script system called RABBL. This allowed the developers to efficiently manage choice structures, if First Snow had any, and at some point before Ren'Py had built-in translation support, translations.

The game story is handled by the master script file in `game/script/script.rpy`. This file contains the entry point for RABBL and guides the general script flow. It tells the engine what scenes to perform, what choices should be made and how the results should be handled, centrally.

RABBL introduces the perform statement to perform a scene. Essentially, ignoring all the tiny extras RABBL gives us, this calls the label `scene_<name>_<currentlanguage>`. Likewise, there is also the choice statement to perform a choice. This, again, gives us some tiny extras, but also fixes the choice so it can't be made again when rolling back. It calls c`hoice_<name>_<currentlanguage> `to display the choice, and relies that said label returns a numeric value indicating what choice was made.

RABBL and, as a result, First Snow do not support Ren'Py's built-in translation system because they predate it. However, RABBL is internationalization-friendly: to translate, all you need to do is copy game/scripts/en to your target language (e.g. `game/scripts/fr`), rename all labels from `_en` to `_fr`, and add the new language to `all_languages` in `game/script/init.rpy`. You then can start translating! Translation requires at least a tiny amount of familiarity with Ren'Py's script format.

All new scenes must be added to the `scenes` variable in `game/script/init.rpy` in order to be registered with the scene replay system and have their title shown in the pause menu. They also need an entry in `game/script/sceneshots` if they aren't set to hidden in the scene replay system.

All new characters must be registered using the `characters` variable in `game/script/init.rpy` and `character_names` and `character_tags` (if applicable) variables in `game/script/<language>/init.rpy`. You don't have to define characters manually: just adding them here will initialize them.

All UI strings are registered in `game/script/<language>/init.rpy` for translation.

For language-specific images, please use the folder `game/vfx/<language>`. Create it if it doesn't exist.

## Working with assets

Assets are automatically defined from the folders: see `game/resources.rpy` for the exact rules. Currently, they are as follows:

* All images from `game/sprites` are defined using a custom sprite composition system: for every character, there's subfolders for every layer. The system then combines all possible combinations with an image name according to the used layers. For instance, `eileen indoors_onhip disbelief smile` consists of `game/sprites/eileen/bodies/indoors_onhip.webp`, `game/sprites/eileen/eyes/disbelief.webp` and `game/sprites/eileen/faces/smile.webp`. Layer folders starting with a `_` are optional.
* All images from `game/sprites-static` get defined as their base/folder name: `game/sprites-static/caprice/smile.png` becomes `caprice smile` and `game/sprites-static/allison/smile_eyesclosed.png` becomes `allison smile eyesclosed`. They also get adjusted vertically according to the sprite_offsets variable, defined in `game/script/init.rpy`.
* All images from `game/bgs` get defined with a `bg` prefix: `game/bgs/apartment/bathroom.png` becomes `bg apartment bathroom`.
* All images from `game/cgs` get defined with a `cg` prefix: `game/cgs/allie_intro.png` becomes `cg allie intro`.
* All images from `game/vfx` get defined with a `misc` prefix: `game/vfx/phone.png` becomes `misc phone`.

All music tracks must be added to the tracks variable in `game/script/<language>/init.rpy` in order to be registered in the jukebox and have their title shown in the pause menu.

## Working with the code

First Snow's code is managed using the [git](http://git-scm.com/) source code control system. A primer on git is available [here](http://git-scm.com/documentation).

All hacks and additions to Ren'Py are stored in the `game/lib` folder. Try to make game functionality as non-specific to First Snow as possible, and store it there. Then the game code can make use of it.

## Building distributions

Internally, First Snow distributions are built using [Drone](http://drone.io/). The exact build instructions are documented in [.drone.yml](./.drone.yml). There's three kinds of distributions built from every release:

- Regular installers for direct downloads. The source files for the installers are located in `installer/win` (Windows, [NSIS 3.0](http://nsis.sourceforge.net/)), `installer/mac` (macOS) and `installer/appimage` (Linux, [AppImage](https://appimage.org/)).
- Steam. The build metadata files are located in `installer/steam`.
- Itch.io. The build metadata is fully contained in `.drone.yml`.

## License

This release of First Snow as a whole will be licensed under the Creative Commons BY-NC-ND 4.0 license. Individual components of this release should be treated as such:

* Art (files in the `game/bgs`, `game/cgs`, `game/sprites`, `game/ui` and `game/vfx` directories) is unconditionally released under the Creative Commons BY-NC-ND 4.0 license.
* Music (files in the `game/music` directory) is unconditionally released under the Creative Commons BY-NC-ND 4.0 license.
* Sound effects (files in the `game/sfx` directory) are licensed, at your choice, under either the Creative Commons BY-NC-ND 4.0 license or the individual original licenses, documented in [SOUND-CREDITS.txt](./SOUND-CREDITS.txt).
* Voice acting (files in the `game/voice` directory) is unconditionally released under the Creative Commons BY-NC-ND 4.0 license.
* Writing (files in the `game/scripts` directory that involve dialogue) is unconditionally released under the Creative Commons BY-NC-ND 4.0 license.
* Code (top-level files in the `game` directory, files in the `game/lib` and `game/scripts` directories) is, at your choice, released under either the Creative Commons BY-NC-ND 4.0 or the BSD 3-Clause license.

    - The engine code, Ren'Py, is licensed under a variety of licenses for its subcomponents. Refer to [the Ren'Py license](https://web.archive.org/web/20200609170052/https://renpy.org/doc/html/license.html) for further details.
    - The terms of the BSD 3-clause license are as follows:
    
```
Copyright 2020, 2021,
  Abigail Turner (voice acting: Elizabeth),
  AcoTan (sprite art),
  adirosa (colouring),
  Aimee Smith (voice acting: Eve),
  All-Maker (CG art, editing)
  birdluvr (colouring),
  Bradley Gareth (voice acting: Andrew),
  Cura (background art, colouring),
  Elissa Park (voice acting: Hayley),
  Elizabeth Quedenfeld (voice acting: Allison),
  James J (music),
  Jill Harris (voice acting: Millie),
  Kira Buckland (voice acting: Eileen),
  Lisa Reimold (voice acting: Caprice),
  Nola Klop (voice acting: Rose),
  Shiz (programming, rough direction),
  Skrats (additional art),
  Steven Kelly (voice acting: Wallace),
  Suriko (writing),
  Syon (voice acting casting, voice acting direction)
  theo minute (act card art),
  TopHat (UI design),
  Träumendes Mädchen (direction)

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```

In addition to these licenses, we would like to make the following specific waivers to further define the wishes of our developers and allow:

* Art: The artwork (Sprites, CGs and background art) of First Snow is non-derivative and forbidden to be used in any works other than First Snow, except as set forth in the derivation waiver. However, fan-made artwork of characters is allowed, but has to released as-is for the enjoyment of others and not as part of another project or compound work, except as set forth in the derivation waiver. 
* Music: It is allowed to make direct remixes, sampling or remakes (further referred to as "derivative music") of First Snow's soundtrack, under the following conditions or the conditions of the derivation waiver.
    - Derivative music will not be released in other collaborative works, such as but not limited to: video games, visual novels, or other projects of any scope or scale.
    - Derivative music may be released as-is and as standalone songs (or albums) for the enjoyment of others. 

Furthermore, we would not like to impair your ability to modify First Snow itself to suit your individual needs or tastes. That is why we add the following waiver for both the entirety of this release and the individual components listed previously (from here on labeled "assets"):

## Derivation waiver

Any person(s) (further referred to as "end-user") who wish to modify and redistribute modifications of the assets involved in First Snow (further referred to as "derivative work") are allowed to, providing they abide by the following conditions:

* No credit is claimed or implied by the end-user for assets made by those other than themselves. Note: Modifying any asset does not change who the original creator is. In order to assert that an asset is the end-user's, they must create it themselves. Additionally, creating an asset in the exact likeness of another does not entitle you to claim said asset as your own. Plagiarizing any pre-existing assets will not change ownership of said asset.
* Any derivative work must be transparent about the fact that it is a derivative work of First Snow and not claim to be anything else.
* Any derivative work must be transparent about the fact that it is not an official release of First Snow by Salty Salty Studios, and mark itself as such.
* All of First Snow's original assets (modified or unmodified) will maintain their licenses and clauses when redistributed in a derivative work.

Both the derivative work and all the assets themselves should follow the terms both set forth in the Creative Commons BY-NC 4.0 license, this additional waiver, and be licensed under the Creative Commons BY-NC-ND 4.0 license WITH this waiver.

## Support

This release comes without any support, warranty or guarantee that your PC won't be set on fire. However, if you have any questions, you can drop by on [our Discord](https://discord.gg/rVR6TFp), open an issue here on GitHub, or hit us up [on Twitter](https://twitter.com/saltyx2studios).
