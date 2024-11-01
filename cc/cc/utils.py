

def attr_class(form):
    for f in form.fields.keys():
        form.fields[f].widget.attrs.update({
            "class":"form-control"
        })