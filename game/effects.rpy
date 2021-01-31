# effects.rpy
# All effect (transformation/transition) definitions are stored here.

python early:
    @renpy.atl_warper
    def eyewarp(x):
        return x**1.33

    @renpy.atl_warper
    def easeout_subtle(t):
        return pow(t, 1.25)

    @renpy.atl_warper
    def easein_subtle(t):
        return 1 - easeout_subtle(1 - t)

    @renpy.atl_warper
    def ease_subtle(t):
        if t < .5:
            return easeout_subtle(t * 2.0) / 2.0
        else:
            return 1 - easeout_subtle((1 - t)* 2.0) / 2.0


# Transistion definitions
define smoothDissolve = Dissolve(0.5, old_widget=None, new_widget=None, alpha=True)
define fastDissolve = Dissolve(0.5, old_widet=None, new_widget=None, alpha=True)
define midDissolve = Dissolve(1.5, old_widget=None, new_widget=None, alpha=True)
define midlongDissolve = Dissolve(2.0, old_widget=None, new_widget=None, alpha=True)
define longDissolve = Dissolve(3.0, old_widget=None, new_widget=None, alpha=True)
define verylongDissolve = Dissolve(5.0, old_widget=None, new_widget=None, alpha=True)
# hmm
define thelongestDissolve = Dissolve(7.0, old_widget=None, new_widget=None, alpha=True)
define thefinalDissolve = Dissolve(20.0, old_widget=None, new_widget=None, alpha=True)
define fadeInOut = Fade(1.0, 0, 1.0)
define menuFade = Fade(2,0,1, color="#f0f0f0")
define inkfade = ImageDissolve(im.Tile("vfx/inkfade.webp"), 2.8, 15)
define inkfade2 = ImageDissolve(im.Tile("vfx/inkfade.webp"), 2.2, 15)
define flash = Fade(0.6, 0.0, 1.0, color="#fff")
define circlewipe = ImageDissolve("vfx/circlewipe.webp", 2.0, 8)
define eye_open = ImageDissolve("vfx/eye.webp", .8, ramplen=128, reverse=False, time_warp=eyewarp)
define eye_shut = ImageDissolve("vfx/eye.webp", .8, ramplen=128, reverse=True, time_warp=eyewarp)


# Sprite position definitions
init -2 python:
    leftoffscreen = Position(xpos=0.0,xanchor=1.0,ypos=1.0,yanchor=1.0)
    leftedge = Position(xpos=0.05,xanchor=0.5,ypos=1.0,yanchor=1.0)
    leftside = Position(xpos=0.15,xanchor=0.5,ypos=1.0,yanchor=1.0)
    left2 = Position(xpos=0.225,xanchor=0.5,ypos=1.0,yanchor=1.0)
    leftish = Position(xpos=0.3,xanchor=0.5,ypos=1.0,yanchor=1.0)
    centerleft = Position(xpos=0.35,xanchor=0.5,ypos=1.0,yanchor=1.0)
    offcenterleft = Position(xpos=0.45,xanchor=0.5,ypos=1.0,yanchor=1.0)
    center = Position(xpos=0.5,xanchor=0.5,ypos=1.0,yanchor=1.0)
    offcenterright = Position(xpos=0.55,xanchor=0.5,ypos=1.0,yanchor=1.0)
    centerright = Position(xpos=0.65,xanchor=0.5,ypos=1.0,yanchor=1.0)
    rightish = Position(xpos=0.7,xanchor=0.5,ypos=1.0,yanchor=1.0)
    right2 = Position(xpos=0.775,xanchor=0.5,ypos=1.0,yanchor=1.0)
    rightside = Position(xpos=0.85,xanchor=0.5,ypos=1.0,yanchor=1.0)
    rightedge = Position(xpos=0.95,xanchor=0.5,ypos=1.0,yanchor=1.0)
    rightoffscreen = Position(xpos=1.0,xanchor=0.0,ypos=1.0,yanchor=1.0)
    
transform null:
    pass

# Center
transform center:
    xanchor 0.5
    xpos 0.5 yalign 1.0

# Close
transform closeleft:
    xanchor 0.5
    xpos .30 yalign 1.0

transform closeright:
    xanchor 0.5
    xpos .70 yalign 1.0

# Near
transform midleft:
    xanchor 0.5
    xpos .15 yalign 1.0

transform midright:
    xanchor 0.5
    xpos .85 yalign 1.0

# Far
transform farleft:
    xanchor 0.5
    xpos .07 yalign 1.0

transform farright:
    xanchor 0.5
    xpos .93 yalign 1.0

# Whereever you are
transform exleft:
    xanchor 0.5
    xpos -0.10 yalign 1.0

transform exright:
    xanchor 0.5
    xpos 1.10 yalign 1.0


# Effects
transform delayed(delay):
    alpha 0
    time delay
    alpha 1

transform showrepeat(first, firstdur, then, thendur):
    first
    time firstdur
    block:
        then
        time thendur
        repeat

transform moveto(t, x):
    subpixel True
    ease t xalign x

transform movetop(t, x):
    subpixel True
    ease t xpos x

transform trotate(alpha):
    subpixel True
    rotate alpha

transform tprotate(alpha):
    subpixel True
    rotate alpha
    rotate_pad False

transform transparent(a):
    alpha a

transform tdissolve(length):
    alpha 0.0
    linear length alpha 1.0

transform tddissolve(length, delay):
    alpha 0.0
    pause delay
    linear length alpha 1.0

transform fadein(speed):
    alpha 0.0
    linear speed alpha 1.0

transform mirror:
    xzoom -1.0

transform jflip(scale=1.0, wait=0.0, duration=0.2):
    time wait
    xzoom scale
    easein duration xzoom 0.0
    easeout duration xzoom -scale

transform jflipto(new, scale=1.0, wait=0.0, duration=0.2):
    time wait
    xzoom scale
    easein duration xzoom 0.0
    new
    easeout duration xzoom -scale

transform jcollapse(scale=1.0, wait=0.0, duration=0.2):
    time wait
    xzoom scale
    easein duration xzoom 0.0
    easeout duration xzoom scale

transform jcollapseto(new, scale=1.0, wait=0.0, duration=0.2):
    time wait
    xzoom scale
    easein duration xzoom 0.0
    new
    easeout duration xzoom scale

transform shaking:
    linear 0.08 xoffset 1
    linear 0.08 xoffset -1
    repeat
    
transform shaking2:
    linear 0.08 xoffset 1
    linear 0.08 xoffset -1
    linear 0.08 xoffset 1
    linear 0.08 xoffset -1
    linear 0.08 xoffset 0
    
transform bounce:
    pause .15
    yoffset 0
    easein .15 yoffset -18
    easeout .175 yoffset 0
    easein .15 yoffset -8
    easeout .175 yoffset 0
    yoffset 0
    
transform stretch:
    yoffset 0
    easein .25 yoffset -15
    easeout .2 yoffset 0
    easein .25 yoffset -5
    easeout .2 yoffset 0
    yoffset 0
    
transform nod:
    ease 0.5 yoffset 5
    ease 0.5 yoffset -5
    ease 0.2 yoffset 0

transform nod2:
    ease 0.5 xoffset 5
    ease 0.5 xoffset -5
    ease 0.2 xoffset 0
    
transform nod2_repeat:
    ease 0.5 xoffset 5
    ease 0.5 xoffset -5
    ease 0.2 xoffset 0
    repeat


init python:
    # Screen and snow effects
    import random
    import math

    class SpriteLayer(object):
        def __init__(self, child, prefill=False, spawn_tries=3, spawn_rate=0.02, xmargin=0.05 * config.screen_width, ymargin=0.08 * config.screen_height, **kwargs):
            super(SpriteLayer, self).__init__()
            self.manager = SpriteManager(update=self.update)
            self.child = renpy.displayable(child)
            self.flakes = []
            self.spawn_tries = spawn_tries
            self.spawn_rate = spawn_rate
            self.xmargin = self.to_concrete(xmargin)
            self.ymargin = self.to_concrete(ymargin)

            if prefill:
                for _ in range(config.screen_height):
                    if random.random() < self.spawn_rate:
                        self.flakes.append(self.spawn_flake(prefill=True))

        def to_concrete(self, x):
            if isinstance(x, tuple):
                if hasattr(x[0], '__call__'):
                    args = [self.to_concrete(a) for a in x[1:]]
                    return lambda f: x[0](f, *[a(f) for a in args])
                return lambda f: random.uniform(*x)
            return lambda f: x

        def update(self, st):
            # Update existing flakes.
            self.flakes[:] = [flake for flake in self.flakes if self.update_flake(flake)]

            # Create new flakes if desired!
            for _ in range(self.spawn_tries):
                if random.random() < self.spawn_rate:
                    self.flakes.append(self.spawn_flake())

            return 0

        def spawn_flake(self, prefill=True):
            return self.manager.create(self.child)
        
        def update_flake(self, flake):
            if flake.x < -self.xmargin(flake) or flake.x > config.screen_width + self.xmargin(flake):
                flake.destroy()
                return False
            if flake.y < -self.ymargin(flake) or flake.y > config.screen_height + self.ymargin(flake):
                flake.destroy()
                return False
            return True

    class SnowLayer(SpriteLayer):
        def __init__(self, *args, **kwargs):
            self.dir_rate = self.to_concrete(kwargs.pop('dir_rate', 0.005))
            self.xspeed = self.to_concrete(kwargs.pop('xspeed', (0, 0.0005 * config.screen_width)))
            self.xmult = self.to_concrete(kwargs.pop('xmult', 1))
            self.xvar = self.to_concrete(kwargs.pop('xvar', (0, 0.0002 * config.screen_width)))
            self.yspeed = self.to_concrete(kwargs.pop('yspeed', 0.0015 * config.screen_height))
            self.ymult = self.to_concrete(kwargs.pop('ymult', 1))
            self.yvar = self.to_concrete(kwargs.pop('yvar', (0, 0.0002 * config.screen_width)))
            super(SnowLayer, self).__init__(*args, **kwargs)

        def spawn_flake(self, prefill=False):
            if prefill:
                yinit = random.uniform(-self.ymargin(None), config.screen_height + self.ymargin(None))
            else:
                yinit = -50

            flake = super(SnowLayer, self).spawn_flake(prefill)
            flake.x = flake.xinit = random.randint(0, config.screen_width)
            flake.xdir = random.choice([1, -1])
            flake.xmult = self.xmult(flake)
            flake.y = yinit
            flake.ymult = self.ymult(flake)
            return flake

        def update_flake(self, flake):
            flake.xdir *= -1 if self.dir_rate and random.random() < self.dir_rate else 1
            flake.x += (self.xspeed(flake) * flake.xmult + self.xvar(flake)) * flake.xdir
            flake.y += self.yspeed(flake) * flake.ymult + self.yvar(flake)
            return super(SnowLayer, self).update_flake(flake)

    class SmokeLayer(SpriteLayer):
        def __init__(self, *args, **kwargs):
            self.xorigin = self.to_concrete(kwargs.pop('xorigin', 500))
            self.yorigin = self.to_concrete(kwargs.pop('yorigin', 300))
            self.angle = self.to_concrete(kwargs.pop('angle', (-30, 30)))
            self.growth_speed = self.to_concrete(kwargs.pop('growth_speed', (0.05, 0.1)))
            self.rotate_speed = self.to_concrete(kwargs.pop('rotate_speed', (0.05, 0.1)))
            super(SmokeLayer, self).__init__(*args, **kwargs)

        def spawn_flake(self, prefill=False):
            flake = super(SmokeLayer, self).spawn_flake()
            flake.x = self.xorigin(flake)
            flake.y = self.yorigin(flake)
            flake.angle = self.angle(flake)
            flake.size = 0.1
            flake.growth_speed= self.growth_speed(flake)
            flake.rotation = 0
            flake.rotation_speed = self.rotate_speed(flake)
            return flake

        def update_flake(self, flake):
            flake.x += math.sin(flake.angle) * 5
            flake.y -= abs(math.cos(flake.angle) * 5)
            if flake.size < 1.0:
                flake.size = max(flake.size + flake.growth_speed, 1.0)
            flake.rotation = (flake.rotation + flake.rotation_speed) % 1.0
            return super(SmokeLayer, self).update_flake(flake)

    def sin(flake, period):
        return math.sin((flake.y / float(period)) * 2 * math.pi) - (flake.x - flake.xinit) / flake.xmult

    def LightSnow(prefill=False):
        return LiveComposite((config.screen_width, config.screen_height),
                             (0, 0), SnowLayer("vfx/smallflake.webp", prefill=prefill, spawn_rate=0.10, xspeed=(sin, 100), xmult=5,  xvar=0, ymult=0.5, dir_rate=0).manager,
                             (0, 0), SnowLayer("vfx/medflake.webp",   prefill=prefill, spawn_rate=0.04, xspeed=(sin, 200), xmult=20, xvar=0, ymult=0.7, dir_rate=0).manager,
                             (0, 0), SnowLayer("vfx/bigflake.webp",   prefill=prefill, spawn_rate=0.02, xspeed=(sin, 500), xmult=60, xvar=0, dir_rate=0).manager)

    def LightSnowSepia(prefill=False):
        return LiveComposite((config.screen_width, config.screen_height),
                             (0, 0), SnowLayer(im.Sepia("vfx/smallflake.webp"), prefill=prefill, spawn_rate=0.10, xspeed=(sin, 100), xmult=5,  xvar=0, ymult=0.5, dir_rate=0).manager,
                             (0, 0), SnowLayer(im.Sepia("vfx/medflake.webp"),   prefill=prefill, spawn_rate=0.04, xspeed=(sin, 200), xmult=20, xvar=0, ymult=0.7, dir_rate=0).manager,
                             (0, 0), SnowLayer(im.Sepia("vfx/bigflake.webp"),   prefill=prefill, spawn_rate=0.02, xspeed=(sin, 500), xmult=60, xvar=0, dir_rate=0).manager)

image snow light starting = LightSnow(prefill=False)
image snow light = LightSnow(prefill=True)
image snow light switch = LightSnow(prefill=True)
image snow sepia = LightSnowSepia(prefill=True)

# Image effects
init python:
    def vblur(name, img):
        # fixes the scary eyes
        if name.startswith('eileen'):
            radius = 2.2
        else:
            radius = 5.0
        return im.Blur(img, radius)
