from PIL import Image, ImageDraw, ImageFont
import io

# ASCII art string
ascii_art = """                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                `x!                                                 
                                                0$hi                                                
                                                %$$}                                                
                                               .n$d:                                                
                                                +$X                                                 
                                                !$x                                                 
                                                I$r                                                 
                                                l$r                                                 
                                                >$u                                                 
                                             :!+x$q+!;.                                             
                                             w@@@$$@@B;                                             
                                              ,w$$$@!.                                              
                "                              X$$$M                                                
                OoLf-,.            ."i?]-!`    ~@$$c                           .i(Y<                
                Ia$$$@MqCcnxxnvYQqa8@$$$$$%Q:  ,UUU?   Ix0b*#b0Xr|}+iI,",l<[tXp8$$w.                
                 ,\vCwa8@@$$$$$$@$@Wah*@$$$${lL%$$$@d[ o$$$$$@$$$$$$$@$$@$$$$$@B*Y"                 
                 _k&opOUUL0QCucJcntjvJZ[Q$$*]&$$$$$$$@xm$$@Cvu/|/nJZdaahq0CYcunun>                  
                 ~8$$$$$$@*mCx?@@$$@&mu(-&8+M$$$$$$$$$$\#$L:d@$@@%&Mp-qa&@$$$$$$$b.                 
                  ixunxf\(tc0Q]_XUzncmWBudCj$$$$$$$$$$$p1$t*CjjnCk8b]n|]]|uLwbhoZI                  
                  ^&$$$$$%wj_/wj@$$$@dj1;hnq$$$$$$$$$$$@<$+)ZB$@#p0/|-/m%8odZO00~                   
                  .C@MZn1{upBd/{Y8wj-jkM}@x*$$$$$$$$$$$$-$nQY]\mB@@(u8bx?{zkB@$$\                   
                    >u0o@$BQ{uWW;inb@@C[1Bzo$$$$$$$$$$$$]$L<p@au]{-zb(r*@8wc\/j}.                   
                    O$$$Wc\QB@Cfpu&oz1LBtzwq$$$$$$$$$$$@{@)Wx/b@@h{}q@af/q@$$$#,                    
                    ~pd/j*$@0jb$B{,fq@W(wfqY$$$$$$$$$$$*rXut8Wu{|~B@Cja@%QfJ%@*,                    
                      +#@%U1O@@0-m|&@J?h811f$$$$$$$$$$$Cx!*b]q@@v\|k@%c|d@@w[?"                     
                      <0x{O@$%t{M@t<+nBB|on+$$$$$$$$$$$tlW(%&|(C-@a+u@$Wx1OBq.                      
                        :8$@O?0$%1\w[B%(p*\C%Ym%@$$$kYawtwk)%@Z?/\BBc]a@$%+".                       
                        _#h}\8$%]vB?1~lmM}ZCO. ,z$b>. )%r)*b1X<l&r?%$*}r8$O                         
                          `J@$Btq@uq&?QiIn/v&! >d8&1.`Zo>#_j[!d0\@01%$@zl1!                         
                          `Q@#vM@Ja@(w8<8)I~@%M@B!0$&W$v.<x]dh]@Xz@*u%@@|                           
                            ^:&%na$Of@nU@}W\0@%$k]t$BBW;C-&d}@Xz$oc@%\/].                           
                              !!^uUi8a-@ZU$x`;z$%@8@#",;@bu@)m@]w@f?J~                              
                                   ?z<m%?BBl  0@$$@$@` .a$|M#>*w`:                                  
                                     .c_x@c   X0Qfm#n;  )@q]#}..                                    
                                       .op`   `;vuc?`.  .0@!.                                       
                                       -b,     l$$$t     "dc                                        
                                       ,^      !$$$f      ,t                                        
                                               !$$$f                                                
                                               !$$$f                                                
                                               !$$$j                                                
                                               I$$$t                                                
                                               `B$$}                                                
                                                h$@l                                                
                                                Y$W.                                                
                                                }$J                                                 
                                                .m!                                                 
                                                 .                                                  
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    """

def ascii_to_image(ascii_str, output_filename="ascii_art.png", scale_factor=0.5):
    # Split the ASCII art into lines
    lines = ascii_str.split('\n')
    
    # Calculate image dimensions
    char_width, char_height = int(5 * scale_factor), int(9 * scale_factor)  # Reduced character size
    width = max(len(line) for line in lines) * char_width
    height = len(lines) * char_height
    
    # Create a new image with white background
    image = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(image)
    
    try:
        # Try to use a monospace font with reduced size
        font_size = int(8 * scale_factor)  # Reduced font size
        font = ImageFont.truetype("Courier", font_size)
    except IOError:
        # If the above font is not available, use the default font
        font = ImageFont.load_default()
    
    # Draw each character of the ASCII art
    y = 0
    for line in lines:
        x = 0
        for char in line:
            if char != ' ':
                draw.text((x, y), char, fill='black', font=font)
            x += char_width
        y += char_height
    

# Create the image with a smaller scale
ascii_to_image(ascii_art, scale_factor=0.5)

print(ascii_art)