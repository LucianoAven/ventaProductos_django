from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from django.views import View

from product.models import ProductReview, Product
from product.repositories.product import ProductRepository
from product.repositories.product_reviews import ProductReviewRepository
from product.forms import ProductReviewForm

class ProductReviewView(View):

    def get(self, request, *args, **kwargs):
        repo = ProductReviewRepository()
        reviews = repo.get_all()
        return render(
            request,
            'product_reviews/list.html',
            dict(
                reviews=reviews
            )
        )

class ProductReviewCreateView(View):

    def get(self, request, *args, **kwargs):
        repo = ProductRepository()
        products = repo.get_all()

        return render(
            request,
            'product_reviews/create.html',
            dict(
                products=products
            )
        )

    def post(self, request):
        repo = ProductReviewRepository()

        product_id = request.POST.get('id_producto')
        review = request.POST.get('opinion')
        value = request.POST.get('valoracion')
        user = request.user

        repo.create(
            product_id=product_id,
            author=user,
            text=review,
            rating=value,
        )
        return redirect('product_reviews')

class ProductReviewDetailView(View):
    def get(self, request, id):
        review = get_object_or_404(ProductReview, id=id)
        return render(
            request,
            'product_reviews/detail.html',
            dict(
                review=review
            )
        )

class ProductReviewUpdateView(View):
    def get(self, request, id):
        review = get_object_or_404(ProductReview, id=id)
        form = ProductReviewForm(instance=review)
        form.initial["author"] = review.author.username
        return render(
            request,
            'product_reviews/update.html',
            dict(
                form=form
            )
        )
    
    def post(self, request, id):
        review = get_object_or_404(ProductReview, id=id)
        form = ProductReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('product_reviews')
        return render(
            request,
            'product_reviews/update.html',
            dict(
                form=form
            )
        )