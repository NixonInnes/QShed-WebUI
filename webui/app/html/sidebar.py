import bootlets.boots as boots
import bootlets.html as html

from flask import url_for


class Sidebar(boots.Boot):
    def build(self):
        return html.Ul(
            # Logo
            html.A(
                html.Div(
                    html.Img(
                        alt="QShed",
                        src=url_for("static", filename="logo.png"),
                        height=90
                    ),
                    class_="sidebar-brand-icon"
                ),
                href=url_for("main.index"),
                class_="sidebar-brand d-flex align-items-center justify-content-center py-5"
            ),

            # Home
            html.Li(
                html.A(
                    html.I(class_="fas fa-fw fa-home"),
                    html.Span("Home"),
                    href=url_for("main.index"),
                    class_="nav-link"
                ),
                class_="nav-item active"
            ),

            # Sidebar title
            html.Div("Services", class_="sidebar-heading"),

            # Gateway
            html.Li(
                # Title
                html.A(
                    html.I(class_="fa fa-fw fa-network-wired"),
                    html.Span("Gateway"),
                    href="#",
                    data_bs_toggle="collapse",
                    data_bs_target="#collapseGateway",
                    aria_expanded="false",
                    aria_controls="collapseGateway",
                    class_="nav-link collapsed"
                ),
                html.Div(
                    html.Div(
                        html.H("Gateway", _size=6, class_="collapse-header"),
                        # Links
                        html.A("Something", href="#", class_="collapse-item"),
                        class_="bg-white py-2 collapse-inner rounded"
                    ),
                    id="collapseGateway",
                    aria_labelledby="headingGateway",
                    data_parent="#accordianSidebar",
                    class_="collapse"
                ),
                class_="nav-item"
            ),

            # Scheduler
            html.Li(
                # Title
                html.A(
                    html.I(class_="fa fa-fw fa-clock"),
                    html.Span("Scheduler"),
                    href="#",
                    data_bs_toggle="collapse",
                    data_bs_target="#collapseScheduler",
                    aria_expanded="false",
                    aria_controls="collapseScheduler",
                    class_="nav-link collapsed"
                ),
                html.Div(
                    html.Div(
                        html.H("Scheduler", _size=6, class_="collapse-header"),
                        # Links
                        html.A("List", href=url_for("scheduler.list_schedules") , class_="collapse-item"),
                        html.A("Add", href=url_for("scheduler.add_schedule") , class_="collapse-item"),
                        class_="bg-white py-2 collapse-inner rounded"
                    ),
                    id="collapseScheduler",
                    aria_labelledby="headingScheduler",
                    data_parent="#accordianSidebar",
                    class_="collapse"
                ),
                class_="nav-item"
            ),

            # Sidebar title
            html.Div("Databases", class_="sidebar-heading"),

            # NoSQL
            html.Li(
                # Title
                html.A(
                    html.I(class_="fa fa-fw fa-database"),
                    html.Span("NoSQL"),
                    href="#",
                    data_bs_toggle="collapse",
                    data_bs_target="#collapseNoSQL",
                    aria_expanded="false",
                    aria_controls="collapseNoSQL",
                    class_="nav-link collapsed"
                ),
                html.Div(
                    html.Div(
                        html.H("NoSQL", _size=6, class_="collapse-header"),
                        # Links
                        html.A("List", href=url_for("nosql.list_databases"), class_="collapse-item"),
                        class_="bg-white py-2 collapse-inner rounded"
                    ),
                    id="collapseNoSQL",
                    aria_labelledby="headingNoSQL",
                    data_parent="#accordianSidebar",
                    class_="collapse"
                ),
                class_="nav-item"
            ),

            # SQL
            html.Li(
                # Title
                html.A(
                    html.I(class_="fa fa-fw fa-database"),
                    html.Span("SQL"),
                    href="#",
                    data_bs_toggle="collapse",
                    data_bs_target="#collapseSQL",
                    aria_expanded="false",
                    aria_controls="collapseSQL",
                    class_="nav-link collapsed"
                ),
                html.Div(
                    html.Div(
                        html.H("SQL", _size=6, class_="collapse-header"),
                        # Links
                        html.A(
                            "Root Entities", 
                            href=url_for("sql.get_root_entities"), 
                            class_="collapse-item"
                        ),
                        html.A(
                            "Create Entity",
                            href=url_for("sql.create_entity"),
                            class_="collapse-item"
                        ),
                        class_="bg-white py-2 collapse-inner rounded"
                    ),
                    id="collapseSQL",
                    aria_labelledby="headingSQL",
                    data_parent="#accordianSidebar",
                    class_="collapse"
                ),
                class_="nav-item"
            ),

            # Timeseries
            html.Li(
                # Title
                html.A(
                    html.I(class_="fa fa-fw fa-database"),
                    html.Span("Timeseries"),
                    href="#",
                    data_bs_toggle="collapse",
                    data_bs_target="#collapseTimeseries",
                    aria_expanded="false",
                    aria_controls="collapseTimeseries",
                    class_="nav-link collapsed"
                ),
                html.Div(
                    html.Div(
                        html.H("Timeseries", _size=6, class_="collapse-header"),
                        # Links
                        html.A("List", href=url_for("timeseries.list"), class_="collapse-item"),
                        class_="bg-white py-2 collapse-inner rounded"
                    ),
                    id="collapseTimeseries",
                    aria_labelledby="headingTimeseries",
                    data_parent="#accordianSidebar",
                    class_="collapse"
                ),
                class_="nav-item"
            ),

            # Divider
            html.Hr(class_="sidebar-divider d-none d-md-block"),

            # Toggler
            html.Div(
                html.Button(
                    id="sidebarToggle",
                    class_="rounded-circle border-0"
                ),
                class_="text-center d-none d-md-inline"
            ),

            id="accordianSidebar",
            class_="navbar-nav bg-gradient-primary sidebar sidebar-dark accordion",
        )