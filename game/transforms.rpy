transform shake:
        ease .06 xoffset 24
        ease .06 xoffset -24
        ease .05 xoffset 20
        ease .05 xoffset -20
        ease .04 xoffset 16
        ease .04 xoffset -16
        ease .03 xoffset 12
        ease .03 xoffset -12
        ease .02 xoffset 8
        ease .02 xoffset -8
        ease .01 xoffset 4
        ease .01 xoffset -4
        ease .01 xoffset 0

transform shake2:
       ease .04 xoffset 12
       ease .04 xoffset -12
       ease .03 xoffset 9
       ease .03 xoffset -9
       ease .02 xoffset 5
       ease .02 xoffset -5
       ease .01 xoffset 2
       ease .01 xoffset -2
       ease .01 xoffset 0

transform bounce:
        ease .10 yoffset 12
        ease .10 yoffset -10
        ease .10 yoffset 5
        ease .10 yoffset -5
        ease .10 yoffset 0

transform wiggle(x=640, z=0.80):
     xcenter x yoffset 0 yanchor 1.0 ypos 1.03 zoom z*1.00 alpha 1.00 subpixel True
     easein 0.15 xoffset 20
     easeout 0.15 xoffset 0
     easein 0.15 xoffset -15
     easeout 0.15 xoffset 0
     easein 0.15 xoffset 10
     easeout 0.15 xoffset 0
     easein 0.15 xoffset -5
     ease 0.15 xoffset 0
