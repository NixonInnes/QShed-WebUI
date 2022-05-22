from io import StringIO


def fig_to_str(fig):
    f = StringIO()
    fig.write_html(f, full_html=False)
    f.seek(0)
    return f.read()