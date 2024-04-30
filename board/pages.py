from flask import Blueprint,render_template


bp = Blueprint("pages",__name__)

@bp.route("/")
def home():
    return render_template("pages/base.html")


@bp.route("/about")
def about():
    return render_template("pages/about.html")

@bp.route("/create",methods=("GET","POST"))
def create():
    print('heyyy')
    return render_template("posts/create.html")

@bp.route("/posts")
def posts():
    posts = []
    return render_template("posts/post.html",posts=posts)
