import bootlets.boots as boots
import bootlets.html as html

from flask import url_for


class SQLEntityHTML(boots.Boot):
    def init(self, entity):
        self.entity = entity

    def build(self):
        return boots.Card(
            boots.CardHeader(f"Entity: [{self.entity.id}] {self.entity.name}"),
            boots.CardBody(
                boots.DescriptionList(
                    ("id", 
                        html.A(
                            self.entity.id, 
                            href=url_for("sql.get_entity", id=self.entity.id)
                        )
                    ),
                    ("Name", self.entity.name),
                    ("Data", self.entity.data),
                    ("Parent", 
                        html.A(
                            self.entity.parent, 
                            href=url_for("sql.get_entity", id=self.entity.parent)
                        ) if self.entity.parent else "None" 
                    ),
                    ("Children",
                        boots.Container(
                            *[
                                html.A(
                                    child, 
                                    href=url_for("sql.get_entity", id=child)
                                ) for child in self.entity.children
                            ]
                        )
                    )

                )
            )
        )