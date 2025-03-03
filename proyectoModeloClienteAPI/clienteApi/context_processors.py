def usuario_autenticado(request):
    usuario = request.session.get("usuario", None)
    return {"usuario_sesion": usuario}
