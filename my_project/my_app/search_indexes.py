from haystack import indexes

from my_project.my_app.models import Company


class CompanyIndex(indexes.RealTimeSearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(
        document=True,
        use_template=True,
    )
    name = indexes.CharField(
        model_attr='name',
        indexed=False,
        stored=True,
    )
    field = indexes.CharField(
        model_attr='field',
        indexed=False,
        stored=True,
    )

    def get_model(self):
        return Company
