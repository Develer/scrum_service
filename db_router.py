class DbRouter(object):
    """A router to control all database operations on models in
    the myapp application
    """
    def db_for_read(self, model, **hints):
        """Suggest the database that should be used for read operations
        for objects of type model.
        """
        if model._meta.app_label == "MyApp":
            return "second"
        return None

    def db_for_write(self, model, **hints):
        """Suggest the database that should be used for writes of objects
        of type Model.
        """
        if model._meta.app_label == "MyApp":
            return "second"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Deny any relation if a model in specialapp is involved"""
        if obj1._meta.app_label == "MyApp" or\
                obj2._meta.app_label == "MyApp":
            return False
        return None

    def allow_syncdb(self, db, model):
        """Deny sync db for the specialapp models"""
        if model._meta.app_label == "MyApp":
            return False
        if db == "second":
            return False
        return None