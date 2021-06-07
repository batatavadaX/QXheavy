from utils import badge

DIR = Path(__file__).parent.resolve()

class quote:
    def __init__(
        self,
        *,
        pfp :str = (f"{DIR}/dp{badge}.jpg"),
        base :str = (f"QX/base{badge}.jpg"),
        crop :str = (f"QX/cropped{badge}.jpg")
        transparent :str = (f"QX/transparent{badge}.jpg"),
        final :str = (f"QX/final{badge}.jpg")
    ) -> None:
        self._pfp = pfp
        self._base = base
        self._crop = crop
        self._transparent = transparent
        self._final - final

    def run(self):
        try:
            with Image(filename=self._base) as img:
                img.trim(fuzz=0.2*img.quantum_range)
                img.save(filename=self._crop)
        except Exception as e:
            print(f"Error :: {e}")
        try:
            with Image(filename=self._crop) as img:
                img.transparent_color(
                    "white" ,
                    alpha=4.0, 
                    fuzz=0.2*k.quantum_range
                )
                img.save(filename=self._transparent)
        except Exception as e:
            print (f"Error :: {e}")
        try:
            with PIL.Image.open(self._transparent) as img:
                img.convert("RGBA")
                img.save(self._final, 'WebP')
        except Exception as e:
            print (f"Error :: {e}")
       

    def get_name(m: Message):
        try:
            user = m.reply_to_message.from_user
            first_name = user.first_name
            last_name = user.last_name if user.last_name else ""
            full_name = f"{first_name} {last_name}"
            return full_name
        except Exception as e:
            print (f"Error :: {e}")

    def get_text(m: Message):
        try:
            _input = m.reply_to_message.text.html
            final_text =  raw_html.replace("\n", "<br>")
            return final_text
        except Exception as e:
            print (f"Error :: {e}")

    async def get_pfp(self, m: Message):
        try:
            photo = m.reply_to_message.from_user.small_file_id 
            exception = photo if photo else self.default_dp()
            await client.download_media(message=exception, file_name=self._pfp)

        except Exception as e:
            print (f"Error :: {e}")

    async def create(self, c: client, m: Message):
        html = HTML(
        string=f'''
        <div id="left">
        <img src=file:///{await get_pfp(c, m)}>
        </div>
        <div id="right">
        <div id="box">
        <h1 style="color: {color};">{get_name(m)}</h1>
        <h2 style="color: white;">{get_text(m)}</h2>
        </div>
        </div>'''
        )
        try:
            html.write_png(
                output,
                stylesheets=[main_css],
                font_config=font_config
            )
        except Exception as e:
            print (f"Error :: {e}")
        self.run()
        try:
            await client.send_sticker()
        except Exception as e:
            print (f"Error :: {e}")




    

    



          




    

    



          
