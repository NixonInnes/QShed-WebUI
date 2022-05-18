import bootlets.boots as boots
import bootlets.html as html


class Breadcrumb(boots.Boot):
    def build(self):
        print(self.args)
        return html.Nav(
            html.Ol(
                boots.Container(
                    *[html.Li(arg, class_="breadcrumb-item") for arg in self.args[:-1]],
                    html.Li(self.args[-1], class_="breadcrumb-item active"),
                    _inline=True
                ),
                class_="breadcrumb"
            ),
            aria_label="breadcrumb"
        )

class PageTitle(boots.Boot):
    def build(self):
        return html.H(*self.args, _size=1, class_="display-5")

