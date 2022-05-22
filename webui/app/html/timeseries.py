import bootlets.boots as boots
import bootlets.html as html

import plotly.express as px

from flask import url_for

from webui.app.utils.plotting import fig_to_str


class TimeseriesRecordHTML(boots.Boot):
    def init(self, ts_record):
        self.ts_record = ts_record

    def build(self):
        return boots.Card(
            boots.CardHeader(f"Timeseries: [{self.ts_record.id}] {self.ts_record.name}"),
            boots.CardBody(
                boots.DescriptionList(
                    ("id", 
                        html.A(
                            self.ts_record.id, 
                            href=url_for("timeseries.plot", name=self.ts_record.name)
                        )
                    ),
                    ("Name", self.ts_record.name),
                )
            )
        )



class TimeseriesPlotHTML(boots.Boot):
    def init(self, df):
        self.df = df

    def build(self):
        fig = px.scatter(x=self.df.index, y=self.df[self.df.columns[0]])

        return html.Div(
            html.Div(
                TimeseriesDescribeHTML(self.df),
                class_="col-4"
            ),
            html.Div(
                fig_to_str(fig),
                class_="col-8"
            ),
            class_="row"
        )


class TimeseriesDescribeHTML(boots.Boot):
    def init(self, df):
        self.df = df

    def build(self):
        return boots.Card(
            boots.CardBody(
                boots.DescriptionList(
                    *list(self.df.describe().itertuples())
                )
            )
        )


