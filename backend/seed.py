from .models import db, Result, Experiment

if __name__ == '__main__':
    db.create_all()
    Result.query.delete()
    Experiment.query.delete()
    db.session.commit()
