function Recommendation({ recommendation }) {

  if (!recommendation || recommendation.error) {
    return (
      <div className="recommendation">
        <h2>⚠️ Recommendation unavailable</h2>
        <p>
          {recommendation?.error || "Something went wrong."}
        </p>
      </div>
    );
  }

  const { best_product, score, reason, pros, cons } = recommendation;

  return (
    <section className="recommendation">

      <div className="recommendation-header">
        <div>
          <span className="badge">🏆 AI'S TOP PICK</span>
          <h2>{best_product.name}</h2>
        </div>

        <div className="score">
          <strong>{score}</strong>
          <span>/10</span>
        </div>
      </div>

      <div className="product-meta">
        <span className="price">
          ₹{best_product.price}
        </span>

        <span className="rating">
          ⭐ {best_product.rating}
        </span>
      </div>

      <div className="reason">
        <h3>Why this product?</h3>
        <p>{reason}</p>
      </div>

      <div className="pros-cons">

        <div>
          <h3>✓ Pros</h3>

          <ul>
            {pros.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul>
        </div>

        <div>
          <h3>✕ Cons</h3>

          <ul>
            {cons.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul>
        </div>

      </div>

    </section>
  );
}

export default Recommendation;