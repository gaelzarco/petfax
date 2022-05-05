from flask import ( Blueprint, render_template )
import json

pets = json.load(open('pets.json'))
print(pets)

bp = Blueprint(
    'pet',
    __name__,
    url_prefix = "/pets"
)

@bp.route('/')
def index():
    return render_template('/pets/index.html', pets = pets)

@bp.route('/<int:index>')
def show_pet(index):
    return render_template('/pets/show.html', pet = pets[index - 1])

@bp.route('/new')
def new_pet():
    return render_template('/facts/new.html')