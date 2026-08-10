function ProductCard({ product }) {
  return (
    <div className="product-card">

      <h3>{product.name}</h3>

      <p className="price">
        ₹{product.price}
      </p>

      <p>⭐ {product.rating}</p>

    </div>
  );
}

export default ProductCard;