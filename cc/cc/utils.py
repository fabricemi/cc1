

def attr_class(form):
    """attribut au champ input la casse 'form-control'"""
    for f in form.fields.keys():
        form.fields[f].widget.attrs.update({
            "class":"form-control"
        })