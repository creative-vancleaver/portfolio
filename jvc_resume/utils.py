def redirect_to_self(self):
    next = self.request.GET.get("next", None)

    if next and next != '':
        return next

    return "/resume/about"