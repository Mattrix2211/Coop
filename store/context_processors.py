def user_is_admin(request):
    user = request.user
    is_admin = user.is_authenticated and (
        user.is_superuser or user.groups.filter(name='Admin').exists()
    )
    return {'user_is_admin': is_admin}
