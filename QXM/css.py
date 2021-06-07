from weasyprint import CSS
from .utils import font_config

main_css = CSS(
string='''
#left
{
width: 100px;
float: left;
}
#right
{
margin-left: 80px;
}
#box
{
border-radius: 35px;
background: #000;
overflow: visible;
padding: 15px;
}
img
{
border-radius: 50%;
height: 70px;
width: 70px;
}
pre
{
font-family: Noto Color Emoji;
}
@font-face 
{
font-family: 'Noto Color Emoji';
src: url(https://gitcdn.xyz/repo/googlefonts/noto-emoji/master/fonts/NotoColorEmoji.ttf);
}
h2,h1 
{ 
font-family: Noto Color Emoji; 
}''', 
font_config=font_config
)
