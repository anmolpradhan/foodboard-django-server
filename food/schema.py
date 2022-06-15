import graphene
from graphene_django import DjangoObjectType

from .models import Category, Food, SizeGroup, Size, Variant


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = "__all__"


class FoodType(DjangoObjectType):
    class Meta:
        model = Food
        fields = "__all__"


class SizeGroupType(DjangoObjectType):
    class Meta:
        model = SizeGroup
        fields = "__all__"


class SizeType(DjangoObjectType):
    class Meta:
        model = Size
        fields = "__all__"


class VariantType(DjangoObjectType):
    class Meta:
        model = Variant
        fields = "__all__"


class Query(graphene.ObjectType):
    categories = graphene.List(CategoryType)
    foods = graphene.List(FoodType, category=graphene.ID())
    sizegroups = graphene.List(SizeGroupType)
    sizes = graphene.List(SizeType)
    variants = graphene.List(VariantType, food=graphene.ID(required=True))

    def resolve_categories(self, info):
        return Category.objects.all()

    def resolve_foods(self, info, **kwargs):
        if "category" in kwargs:
            category = kwargs.get("category")
            return Food.objects.filter(category_id=category)
        else:
            return Food.objects.all()

    def resolve_sizegroups(self, info):
        return SizeGroup.objects.all()

    def resolve_sizes(self, info):
        return Size.objects.all()

    def resolve_variants(self, info, food):
        return Variant.objects.filter(food_id=food)


class CreateCategory(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        status = graphene.Boolean()
        featured = graphene.Boolean()
        description = graphene.String()

    category = graphene.Field(CategoryType)

    def mutate(self, info, name, status, featured, description):
        category = Category(name=name, status=status, featured=featured, description=description)
        category.save()
        return CreateCategory(id=category.id, name=category.name, status=category.status,
                              featured=category.featured,
                              description=category.description)


class CreateFood(graphene.Mutation):
    class Arguments:
        category = graphene.ID()
        sizegroup = graphene.ID()
        name = graphene.String()
        status = graphene.Boolean()
        veg = graphene.Boolean()
        description = graphene.String()

    food = graphene.Field(FoodType)

    def mutate(self, info, name, category, sizegroup, status, veg, description):
        food = Food(name=name, category=category, sizegroup=sizegroup, status=status, veg=veg, description=description)
        food.save()
        return CreateFood(id=food.id, name=food.name, category=food.category, sizegroup=food.sizegroup,
                          status=food.status, veg=food.veg, description=food.description)


class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    create_food = CreateFood.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
