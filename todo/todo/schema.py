import graphene

from main.schema import Query as tasks_query

class Query(tasks_query):
    pass

schema = graphene.Schema(query = Query)