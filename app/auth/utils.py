from flask_login import current_user
from flask import abort


def admin_required(f):
    if not current_user.is_admin:
        abort(403)