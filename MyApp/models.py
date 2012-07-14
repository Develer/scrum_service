from django.db import models
from IEntityEngine import sql_processor

class scrum_db:

    @classmethod
    def get_all_tasks(cls):
        all_sql_processor = sql_processor()
        tasks = all_sql_processor.process("select * from tasks")
        tasks_fields = all_sql_processor.process("describe tasks")
        tasks_dict = cls.from_tuple_to_dictionary(tasks, tasks_fields)
        return tasks_dict

    @classmethod
    def get_all_bugs(cls):
        all_sql_processor = sql_processor()
        bugs = all_sql_processor.process("select * from bugs")
        bugs_fields = all_sql_processor.process("describe bugs")
        bugs_dict = cls.from_tuple_to_dictionary(bugs, bugs_fields)
        return bugs_dict

    @classmethod
    def from_tuple_to_dictionary(cls, dates, fields):
        fields_list = []
        for i in fields:
            fields_list.append(i[0])
        d = {}
        for date in dates:
            #key = j[0]
            dict_item = {}
            for i in range(len(fields_list)):
                dict_item[fields_list[i]] = date[i]
            d[date[0]] = dict_item
        return d

#    @classmethod
#    def add_item(cls, dates):
#        print("adding")
#        print(str(dates))
#        feat = sql_processor()
#        feat.process("insert into features(description, status, to_assert, entity_type) values" + str(dates))